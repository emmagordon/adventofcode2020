#!/usr/bin/env python3

from collections import namedtuple
from typing import List, Tuple

PUZZLE_INPUT = "input.txt"
ACTIVE = '#'
INACTIVE = '.'

CoOrd = namedtuple("CoOrd", "x y z")
Range = namedtuple("Range", "lower upper")


class Game:
    def __init__(self, init_state: List[str]) -> None:
        z = 0
        self.active_cells = [
            CoOrd(x, y, z)
            for y, line in enumerate(init_state)
            for x, c in enumerate(line)
            if c == ACTIVE
        ]
        self.cycle = 0
    
    @property
    def num_active_cells(self):
        return len(self.active_cells)

    def tick(self):
        next_gen_active_cells = [] 
        xr, yr, zr = self.get_bounds()
        for i in range(xr.lower, (xr.upper + 1)):
            for j in range(yr.lower, (yr.upper + 1)):
                for z in range(zr.lower, (zr.upper + 1)):
                    loc = CoOrd(i, j, z)
                    ns = self.neighbours(loc)
                    if self.becomes_or_stays_alive(loc, ns):
                        next_gen_active_cells.append(loc)
        self.active_cells = next_gen_active_cells
        self.cycle += 1

    def becomes_or_stays_alive(self, cell: CoOrd, neighbours: List[CoOrd]):
        num_active_neighbours = len([
            n for n in neighbours
            if n in self.active_cells
        ])
        if cell in self.active_cells:
            return num_active_neighbours in [2, 3]
        return num_active_neighbours == 3

    def neighbours(self, cell: CoOrd) -> List[CoOrd]:
        return [
            CoOrd(x, y, z)
            for x in [cell.x-1, cell.x, cell.x+1]
            for y in [cell.y-1, cell.y, cell.y+1]
            for z in [cell.z-1, cell.z, cell.z+1]
            if not (x == cell.x and y == cell.y and z == cell.z)
        ]

    def get_bounds(self) -> Tuple[Range, Range, Range]:
        xs = {c.x for c in self.active_cells}
        ys = {c.y for c in self.active_cells}
        zs = {c.z for c in self.active_cells}

        return (
            Range(min(xs)-1,max(xs)+1),
            Range(min(ys)-1,max(ys)+1),
            Range(min(zs)-1,max(zs)+1)
        )

    def __repr__(self) -> str:
        xr, yr, zr = self.get_bounds()
        output = []
        for z in range(zr.lower, (zr.upper + 1)):
            output.append(f"z={z}")
            for y in range(yr.lower, (yr.upper + 1)):
                output.append("".join(
                    (ACTIVE if CoOrd(x, y, z) in self.active_cells else INACTIVE)
                    for x in range(xr.lower, (yr.lower + 1))
                ))
            output.append("")
        return "\n".join(output)


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    game = Game(puzzle_input)
    for _ in range(6):
        game.tick()
    
    print(game.num_active_cells)
