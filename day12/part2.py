#!/usr/bin/env python3

import math
from typing import Union

PUZZLE_INPUT = "input.txt"


def degs_to_rads(theta: float) -> float:
    # 2pi rads = 360 degs, so 1 deg = pi/180 rads
    return (math.pi / 180) * theta


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

        self.waypoint_x = 10
        self.waypoint_y = 1

        self.commands = {
            "N": self.north,
            "S": self.south,
            "E": self.east,
            "W": self.west,
            "L": self.left,
            "R": self.right,
            "F": self.forward
        }

    def reset_to_start(self) -> None:
        self.x = 0
        self.y = 0

        self.waypoint_x = 10
        self.waypoint_y = 1

    def manhattan_distance_from_start(self) -> None:
        return abs(self.x) + abs(self.y)

    def execute_command(self, instruction: Instruction) -> None:
        self.commands[instruction.command](instruction.number)

    def north(self, n: int) -> None:
        self.waypoint_y += n
    
    def south(self, n: int) -> None:
        self.waypoint_y -= n
    
    def east(self, n: int) -> None:
        self.waypoint_x += n
    
    def west(self, n: int) -> None:
        self.waypoint_x -= n
    
    def right(self, n: int) -> None:
        new_angle = (degs_to_rads(n) - self.waypoint_angle_rads)
        self.waypoint_x = (self.waypoint_distance * math.cos(new_angle))
        self.waypoint_y = (self.waypoint_distance * math.sin(new_angle))


    def left(self, n: int) -> None:
        new_angle = (degs_to_rads(n) + self.waypoint_angle_rads)
        self.waypoint_x = (self.waypoint_distance * math.cos(new_angle))
        self.waypoint_y = (self.waypoint_distance * math.sin(new_angle))
    
    # def right(self, n: int) -> None:
    #     d = {
    #         90: (self.waypoint_y, -self.waypoint_x),
    #         180: (-self.waypoint_x, - self.waypoint_y),
    #         270: (-self.waypoint_y, self.waypoint_x)
    #     }
    #     self.waypoint_x, self.waypoint_y = d[n]

    # def left(self, n: int) -> None:
    #     d = {
    #         270: (self.waypoint_y, -self.waypoint_x),
    #         180: (-self.waypoint_x, - self.waypoint_y),
    #         90: (-self.waypoint_y, self.waypoint_x)
    #     }
    #     self.waypoint_x, self.waypoint_y = d[n]

    @property
    def waypoint_distance(self) -> float:
        return math.sqrt(self.waypoint_x**2 + self.waypoint_y**2)

    @property
    def waypoint_angle_rads(self) -> float:
        return math.atan2(self.waypoint_y, self.waypoint_x)

    def forward(self, n: int) -> None:
        self.x += (n * self.waypoint_x)
        self.y += (n * self.waypoint_y)

    def __repr__(self):
        return f"({self.x}, {self.y}) with (rel) waypoint at ({self.waypoint_x}, {self.waypoint_y}) with dist {self.waypoint_distance} and angle {self.waypoint_angle_rads}"


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [Instruction(line.rstrip()) for line in f.readlines()]
    
    boat = Boat()
    print(boat)
    for instruction in puzzle_input:
        boat.execute_command(instruction)
        print(boat)
    
    print(boat.manhattan_distance_from_start())
