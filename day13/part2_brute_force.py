#!/usr/bin/env python3

from collections import namedtuple
from typing import List, Tuple

PUZZLE_INPUT = "input.txt"

BusId = namedtuple("BusId", "value rel_idx")


def munge_input(bus_ids: List[int]) -> Tuple[List[BusId], int, int]:
    largest = bus_ids[0]
    largest_idx = 0
    for i, _id in enumerate(bus_ids):
        if _id > largest:
            largest = _id
            largest_idx = i
    
    rel_ids = []
    for i, _id in enumerate(bus_ids):
        if _id == -1:
            continue
        rel_ids.append(BusId(_id, (i - largest_idx)))

    return rel_ids, largest, largest_idx


def solve(bus_ids: List[BusId], largest: int) -> int:
    n = largest
    while True:
        if all(((n + _id.rel_idx) % _id.value) == 0 for _id in bus_ids):
            return n
        n += largest


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]
 
    bus_ids = [
        int(i) if i != "x" else -1
        for i in puzzle_input[1].split(",")
    ]

    rel_ids, largest, largest_idx = munge_input(bus_ids)
    print(solve(rel_ids, largest) - largest_idx)
