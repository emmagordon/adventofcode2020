#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"


def count_trees(puzzle_input, slope):
    X = len(puzzle_input[0])
    num_trees = 0
    x, y = 0, 0
    while True:
        x += slope[0]
        y += slope[1]
        if y >= len(puzzle_input):
            break
        if puzzle_input[y][x % X] == "#":
            num_trees += 1
    return num_trees

if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [row.strip() for row in f.readlines()]

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] 
    product = 1
    for slope in slopes:
        product *= count_trees(puzzle_input, slope)
    
    print(product)
