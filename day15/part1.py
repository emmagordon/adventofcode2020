#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"
STOP = 30000000

if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [int(n) for n in f.readline().split(",")]
    
    turn = 1
    spoken = {}
    for num in puzzle_input:
        # print(f'turn: {turn}, num: {num}')
        spoken[num] = turn
        turn += 1

    prev_num = None
    while turn <= STOP:
        if prev_num in spoken:
            new_num = ((turn - 1) - spoken[prev_num])
        else:
            new_num = 0
        # print(f'turn: {turn}, num: {new_num}')
        spoken[prev_num] = (turn - 1)
        prev_num = new_num
        turn += 1
    
    print(prev_num)
