#!/usr/bin/env python3

import math
from typing import List

PUZZLE_INPUT = "input.txt"


class Tile:
    def __init__(self, uid: int, image: List[str]) -> None:
        self.uid = uid
        self.image = image

    @property
    def top(self) -> str:
        return self.image[0]
    
    @property
    def bottom(self) -> str:
        return self.image[-1]
    
    @property
    def left(self) -> str:
        return "".join(row[0] for row in self.image)
    
    @property
    def right(self) -> str:
        return "".join(row[-1] for row in self.image)

    @property
    def edges(self) -> List[str]:
        return [self.top, self.right, self.bottom, self.left]
    
    def flip(self, axis: str) -> None:
        if axis == "y":
            self.image = [row[::-1] for row in self.image]
        elif axis == "x":
            self.image = self.image[::-1]
        else:
            raise RuntimeError('should never hit this!')

    def rotate_90_deg_clockwise(self) -> None:
        tile_size = len(self.image)
        columns = ["".join(row[i] for row in self.image) for i in range(tile_size)]
        self.image = [col[::-1] for col in columns]

    def __repr__(self):
        return "\n".join(row for row in self.image)


class Puzzle:
    def __init__(self, tiles: List[Tile]) -> None:
        self.tiles = tiles
        self.corners = []
        self.grid_size = int(math.sqrt(len(self.tiles)))
        self.grid = [([None] * self.grid_size) for i in range(self.grid_size)]

    def solve(self) -> None:
        self.corners = self.find_corner_pieces()
        self.rotate_top_left_corner_into_position()
        self.fill_out_top_row()
        for i in range(1, self.grid_size):
            self.fill_out_row(i)
    
    @property
    def unused_tiles(self) -> List[Tile]:
        used_tile_ids = [
            tile.uid
            for row in self.grid for tile in row
            if (tile is not None)
        ]
        return [
            t for t in self.tiles
            if not (t.uid in used_tile_ids)
        ]

    def find_corner_pieces(self) -> List[Tile]:
        return [
            t for t in self.tiles
            if self.find_num_matching_edges(t) == 2
        ]

    def find_num_matching_edges(self, tile: Tile) -> int:
        return len([
            edge for edge in tile.edges
            if self.edge_matches_any_other_tile_edge(edge, tile)
        ])

    def edge_matches_any_other_tile_edge(self, edge: str, tile: Tile) -> bool:
        other_tiles = [t for t in self.tiles if t.uid != tile.uid]
        return any(
            edge in [other_edge, other_edge[::-1]]
            for other in other_tiles
            for other_edge in other.edges
        )

    def rotate_top_left_corner_into_position(self) -> None:
        tile = self.corners[0]  # doesn't matter which one we pick
        i = 0
        while True:
            if i > 3:
                raise RuntimeError('should never hit this!')
            if not (self.edge_matches_any_other_tile_edge(tile.top, tile) or self.edge_matches_any_other_tile_edge(tile.left, tile)):
                self.grid[0][0] = tile
                return
            tile.rotate_90_deg_clockwise()
            i += 1

    def fill_out_top_row(self) -> None:
        # Fucking hell... I am seriously judging myself for this code...
        for i in range(1, self.grid_size):
            for tile in self.unused_tiles:
                for _ in range(4):
                    if (tile.left == self.grid[0][i-1].right) and (not self.edge_matches_any_other_tile_edge(tile.top, tile)):
                        self.grid[0][i] = tile
                        break
                    tile.flip("y")
                    if (tile.left == self.grid[0][i-1].right) and (not self.edge_matches_any_other_tile_edge(tile.top, tile)):
                        self.grid[0][i] = tile
                        break
                    tile.flip("y")
                    tile.flip("x")
                    if (tile.left == self.grid[0][i-1].right) and (not self.edge_matches_any_other_tile_edge(tile.top, tile)):
                        self.grid[0][i] = tile
                        break
                    tile.flip("x")
                    tile.rotate_90_deg_clockwise()
                else:
                    continue
                break
            else:
                raise RuntimeError('should never hit this!')

    def fill_out_row(self, row_num: int) -> None:
        # Fucking hell... I am seriously judging myself (EVEN MORE!) for this code...

        # fill in left most tile (top matches bottom of above tile + left is an edge)
        for tile in self.unused_tiles:
            for _ in range(4):
                if (not self.edge_matches_any_other_tile_edge(tile.left, tile)) and (tile.top == self.grid[row_num-1][0].bottom):
                    self.grid[row_num][0] = tile
                    break
                tile.flip("y")
                if (not self.edge_matches_any_other_tile_edge(tile.left, tile)) and (tile.top == self.grid[row_num-1][0].bottom):
                    self.grid[row_num][0] = tile
                    break
                tile.flip("y")
                tile.flip("x")
                if (not self.edge_matches_any_other_tile_edge(tile.left, tile)) and (tile.top == self.grid[row_num-1][0].bottom):
                    self.grid[row_num][0] = tile
                    break
                tile.flip("x")
                tile.rotate_90_deg_clockwise()
            else:
                continue
            break
        else:
            raise RuntimeError('should never hit this!')

        # then fill in rest of row:
        for i in range(1, self.grid_size):
            for tile in self.unused_tiles:
                for _ in range(4):
                    if (tile.left == self.grid[row_num][i-1].right) and (tile.top == self.grid[row_num-1][i].bottom):
                        self.grid[row_num][i] = tile
                        break
                    tile.flip("y")
                    if (tile.left == self.grid[row_num][i-1].right) and (tile.top == self.grid[row_num-1][i].bottom):
                        self.grid[row_num][i] = tile
                        break
                    tile.flip("y")
                    tile.flip("x")
                    if (tile.left == self.grid[row_num][i-1].right) and (tile.top == self.grid[row_num-1][i].bottom):
                        self.grid[row_num][i] = tile
                        break
                    tile.flip("x")
                    tile.rotate_90_deg_clockwise()
                else:
                    continue
                break
            else:
                raise RuntimeError('should never hit this!')

    def __repr__(self) -> str:
        try:
            tile_size = len(self.grid[0][0].image)
        except AttributeError:
            return 'An unsolved puzzle...'
        
        output = []
        output.append("-" * (1 + (self.grid_size * (tile_size + 1))))
        for row in self.grid:
            for i in range(tile_size):
                output.append(f"|{'|'.join(tile.image[i] for tile in row)}|")
            output.append("-" * (1 + (self.grid_size * (tile_size + 1))))
        
        return "\n".join(output)


def parse_input() -> List[Tile]:
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]
 
    tiles = []
    tile_id = None
    tile_image = []
    for line in puzzle_input:
        if not line:
            tiles.append(Tile(tile_id, tile_image))
            tile_id = None
            tile_image = []
        elif line.startswith('Tile'):
            tile_id = int(line.split()[1].rstrip(":"))
        else:
            tile_image.append(line)
    
    tiles.append(Tile(tile_id, tile_image))
    return tiles


if __name__ == "__main__":
    tiles = parse_input()
    puzzle = Puzzle(tiles)
    puzzle.solve()
    print(puzzle)

    mul = 1
    for c in puzzle.corners:
        mul *= c.uid
    print(f'Part1 = {mul}')

    # mul = 1
    # corners = [puzzle.grid[0][0], puzzle.grid[0][-1], puzzle.grid[-1][0], puzzle.grid[-1][-1]]
    # for c in puzzle.corners:
    #     mul *= c.uid
    # print(f'Part1 = {mul}')