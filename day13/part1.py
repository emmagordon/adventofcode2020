#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"


def solve(bus_ids: List[int], departure_time: int) -> int:
    wait = 0
    while True:
        for _id in bus_ids:
            if ((departure_time + wait) % _id) == 0:
                return (_id * wait)
        wait += 1


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]
 
    departure_time = int(puzzle_input[0])
    bus_ids = [int(i) for i in puzzle_input[1].split(",") if i != "x"]

    print(solve(bus_ids, departure_time))
