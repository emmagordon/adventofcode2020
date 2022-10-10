#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"

if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [row.strip() for row in f.readlines()]

    X = len(puzzle_input[0]) 

    num_trees = 0
    x, y = 0, 0
    while True:
        x += 3
        y += 1
        if y >= len(puzzle_input):
            break
        if puzzle_input[y][x % X] == "#":
            num_trees += 1
    
    print(num_trees)
