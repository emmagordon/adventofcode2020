#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"
        
if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [int(line.rstrip()) for line in f.readlines()]
        sorted_jolts = sorted(puzzle_input)
        counter = {1: 0, 3: 1}  # always 1 threee (for built-in highest adpater)
        val = 0
        for j in sorted_jolts:
            counter[(j - val)] += 1
            val = j
        print(counter[1] * counter[3])
