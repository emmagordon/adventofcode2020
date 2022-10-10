#!/usr/bin/env python3

import math
from typing import List

PUZZLE_INPUT = "input.txt"

class Instruction:
    def __init__(self, instruction: str) -> None:
        self.command = instruction[0]
        self.number = int(instruction[1:])
    
    def __repr__(self):
        return f"{self.command} {self.number}"


class Boat:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0  # angle above/below the x-axis (where -180 is along x-axis in opposite direction)
        self.commands = {
            "N": self.go_north,
            "S": self.go_south,
            "E": self.go_east,
            "W": self.go_west,
            "L": self.turn_left,
            "R": self.turn_right,
            "F": self.go_forward
        }
    
    @property
    def theta_in_radians(self) -> float:
        # 2pi rad = 360deg
        # so 1 deg = pi/180 rad
        return (math.pi / 180) * self.theta

    def reset_to_start(self) -> None:
        self.x = 0
        self.y = 0
        self.theta = 0

    def manhattan_distance_from_start(self) -> None:
        return abs(self.x) + abs(self.y)

    def execute_command(self, instruction: Instruction) -> None:
        self.commands[instruction.command](instruction.number)

    def go_north(self, n: int) -> None:
        self.y += n
    
    def go_south(self, n: int) -> None:
        self.y -= n
    
    def go_east(self, n: int) -> None:
        self.x += n
    
    def go_west(self, n: int) -> None:
        self.x -= n
    
    def turn_right(self, n: int) -> None:
        self.theta -= n

    def turn_left(self, n: int) -> None:
        self.theta += n

    def go_forward(self, n: int) -> None:
        # have theta and h
        # find a and o using trig
        # add to x and y respectively
        self.x += (n * math.cos(self.theta_in_radians))
        self.y += (n * math.sin(self.theta_in_radians))

    def __repr__(self):
        return f"({self.x}, {self.y}) at {self.theta} deg from x-axis"


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [Instruction(line.rstrip()) for line in f.readlines()]
    
    boat = Boat()
    # print(boat)
    for instruction in puzzle_input:
        boat.execute_command(instruction)
        # print(boat)
    
    print(boat.manhattan_distance_from_start())
