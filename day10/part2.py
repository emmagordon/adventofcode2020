#!/usr/bin/env python3

from typing import List, Optional, Tuple

PUZZLE_INPUT = "input.txt"
VALID_JUMPS = [1, 2, 3]
MAX_JUMP = 3


def find_num_arrangements(sorted_jolts: List[int]) -> int:
    counter = 1
    last_val = 0
    i = 0
    while i < len(sorted_jolts):
        if ((i+3) < len(sorted_jolts)) and (sorted_jolts[i+3] <= (last_val + 4)):
            last_val = sorted_jolts[i+3]
            i += 4
            counter *= 7
        if ((i+2) < len(sorted_jolts)) and (sorted_jolts[i+2] <= (last_val + 3)):
            last_val = sorted_jolts[i+2]
            i += 3
            counter *= 4
        elif ((i+1) < len(sorted_jolts)) and (sorted_jolts[i+1] <= (last_val + 3)):
            last_val = sorted_jolts[i+1]
            i += 2
            counter *= 2
        else:
            last_val = sorted_jolts[i]
            i += 1
    return counter


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [int(line.rstrip()) for line in f.readlines()]
        sorted_jolts = sorted(puzzle_input)
        sorted_jolts.append(sorted_jolts[-1] + 3)

        print(find_num_arrangements(sorted_jolts))