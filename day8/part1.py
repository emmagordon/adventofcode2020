#!/usr/bin/env python3

from collections import namedtuple

PUZZLE_INPUT = "input.txt"

ACC = "acc"
JMP = "jmp"
NOP = "nop"


class InfiniteLoop(Exception):
    pass


class Instruction:
    def __init__(self, line: str) -> None:
        self.op = INSTRUCTIONS[line.split()[0]]
        self.num = int(line.split()[1])
    
    def __repr__(self):
        return f"{self.op} {self.num}"

acc = 0
line = 0
visited = []


def _acc(num: int) -> None:
    global line
    global acc
    acc += num
    line += 1

def jmp(num: int) -> None:
    global line
    line += num


def nop(num: int) -> None:
    global line
    line += 1


INSTRUCTIONS = {
    ACC: _acc,
    JMP: jmp,
    NOP: nop
}


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        instructions = [Instruction(line.rstrip()) for line in f.readlines()]

    while True:
        instruction = instructions[line]
        if line in visited:
            break
        else:
            visited.append(line)
            instruction.op(instruction.num)
    
    print(acc)
