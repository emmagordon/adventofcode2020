#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"

PREAMBLE_LEN = 25


def first_invalid_num(nums: List[int], preamble_len: int) -> int:
    for j, num in enumerate(nums[preamble_len:]):
        i = j + preamble_len
        if not is_valid(nums[i], nums[(i-preamble_len):i]):
            return nums[i]

    raise ValueError("should never hit this!")


def is_valid(num: int, prev_nums: List[int]) -> bool:
    nums = set(prev_nums)
    for n in nums:
        target = num - n
        if target in (nums - {n}):
            return True
    return False


def find_contiguous_nums_that_sum_to(num: int, nums: List[int]) -> List[int]:
    contiguous_nums = []
    for n in nums:
        contiguous_nums.append(n)
        total = sum(contiguous_nums)
        while total > num:
            contiguous_nums = contiguous_nums[1:]
            total = sum(contiguous_nums)
        if total == num:
            return contiguous_nums
    
    raise ValueError("should never hit this!")
        

if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [int(line.rstrip()) for line in f.readlines()]

    invalid_num = first_invalid_num(puzzle_input, PREAMBLE_LEN)
    sum_nums = find_contiguous_nums_that_sum_to(invalid_num, puzzle_input)
    print(min(sum_nums) + max(sum_nums))
