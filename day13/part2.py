#!/usr/bin/env python3

from collections import namedtuple
import itertools
import math
import sys
from typing import List

PUZZLE_INPUT = "input.txt"

Bus = namedtuple("Bus", "id idx")


def earliest_sequence_start(buses: List[Bus]) -> int:
    # Use Chinese Remainder Theorme to solve
    # (see https://www.youtube.com/watch?v=ru7mWZJlRQg ).

    if not all_coprime([b.id for b in buses]):
        raise ValueError("Can't apply Chinese Remainder Theorem!")

    x = 0
    for i, bus in enumerate(buses):
        n = math.prod(b.id for b in (buses[:i] + buses[(i+1):]))
        # TODO - non-brute-force method to find j
        j = 1
        while True:
            if (((j * n) + bus.idx) % bus.id) == 0:
                x += (j * n)
                break
            j += 1

    mul = math.prod([b.id for b in buses])
    while x > mul:
        x -= mul
    return x


def all_coprime(arr: List[int]) -> bool:
    return all(
        math.gcd(x, y) == 1
        for x, y in itertools.combinations(arr, 2)
    )


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]
 
    buses = [
        Bus(int(_id), i)
        for (i, _id) in enumerate(puzzle_input[1].split(","))
        if _id != "x"
    ]

    print(earliest_sequence_start(buses))
