#!/usr/bin/env python3

import operator
from typing import Dict

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
            assert len(opens) > 0
            matching_open_loc = opens.pop()
            lookup[matching_open_loc] = i
    
    assert len(opens) == 0
    return lookup


def evaluate(expr: str) -> int:
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
        # elif expr[i] == ")":
        #     break
        elif is_integer(expr[i]):
            stack.append(int(expr[i]))  # assumes numbers all single-digit
            i += 1
        else:
            raise RuntimeError('should never hit this!')
    
    calc = stack
    while True:
        if len(calc) == 1:
            return calc[0]
        elif len(calc) < 3:
            raise RuntimeError('should never hit this!')
        calc = [calc[1](calc[0], calc[2])] + calc[3:]


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    _sum = 0
    for line in puzzle_input:
        res = evaluate(line)
        print(f'{line} = {res}')
        _sum += res

    print('---')
    print(_sum)
