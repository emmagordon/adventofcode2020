#!/usr/bin/env python3

import operator
from typing import Dict, List, Union, Callable

PUZZLE_INPUT = "input.txt"

OPERATORS = {
    "+": operator.add,
    "*": operator.mul
}


def is_integer(num: str) -> bool:
    try:
        int(num)
    except TypeError:
        return False
    return True


def closing_paren_lookup(expr: str) -> Dict[int, int]:
    lookup = {}
    opens = []
    for i, c in enumerate(expr):
        if c == "(":
            opens.append(i)
        elif c == ")":
            matching_open_loc = opens.pop()
            lookup[matching_open_loc] = i
    return lookup


def evaluate(expr: str) -> int:  # assumes input expr format is valid!
    if len(expr) == 0:
        return 0

    close_paren_locs = closing_paren_lookup(expr)
    stack = []
    i = 0
    while i < len(expr):
        if expr[i] == " ":
            i += 1
        elif expr[i] in ['+', '*']:
            stack.append(OPERATORS[expr[i]])
            i += 1
        elif expr[i] == "(":
            c = close_paren_locs[i]
            stack.append(evaluate(expr[(i+1):c]))
            i = (c + 1)
        elif is_integer(expr[i]):
            stack.append(int(expr[i]))  # assumes numbers all single-digit
            i += 1
    
    return calculate(stack)


def calculate(stack: List[Union[int, Callable]]) -> int:  # assumes an input of alernating ints and +/* operators
    calc1 = stack
    calc2 = []
    # 1st pass - do additions
    while True:
        if len(calc1) == 1:
            calc2 += calc1
            break
        elif calc1[1] == operator.mul:
            calc2 += calc1[:2]
            calc1 = calc1[2:]
        else:
            calc1 = [calc1[1](calc1[0], calc1[2])] + calc1[3:]

    # 2nd pass - do multiplications
    while True:
        if len(calc2) == 1:
            return calc2[0]
        calc2 = [calc2[1](calc2[0], calc2[2])] + calc2[3:]


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    print(sum(evaluate(line) for line in puzzle_input))
