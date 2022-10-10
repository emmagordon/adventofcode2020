#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"


def find_numbers_that_sum_to(target: int, numbers: List[int]) -> List[int]:
    """n.b. assumes that these values are in the input!"""
    nums = set(numbers)
    for n in nums:
        m = target - n
        if m in nums:
            return [n, m]
    raise ValueError(f"Input didn't contain 2 values that sum to {target}!")


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [int(s) for s in f.readlines()]
    
    n, m = find_numbers_that_sum_to(2020, puzzle_input)
    print(n * m)
