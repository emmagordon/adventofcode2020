#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"


def find_numbers_that_sum_to(target: int, numbers: List[int]) -> List[int]:
    """n.b. assumes that these values are in the input!"""
    nums = set(numbers)
    for i, n in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            m = numbers[j]
            p = target - (n + m)
            if p in nums:
                return n, m, p
    raise ValueError(f"Input didn't contain 3 values that sum to {target}!")


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [int(s) for s in f.readlines()]
    
    n, m, p = find_numbers_that_sum_to(2020, puzzle_input)
    print(n * m * p)
