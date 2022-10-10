#!/usr/bin/env python3

import copy
from typing import List

PUZZLE_INPUT = "input.txt"


class InfiniteLoop(Exception):
    pass


class TooFar(Exception):
    pass


class Instruction:
    def __init__(self, line: str) -> None:
        self.line = line
        self.op = line.split()[0]
        self.num = int(line.split()[1])
    
    def __repr__(self):
        return f"{self.op} {self.num}"


def run_boot_code(instructions: List[Instruction]) -> int:
    acc = 0
    line = 0
    visited = []

    while True:
        if line == len(instructions):
            return acc
        elif (line < 0) or (line > len(instructions)):
            raise TooFar

        instruction = instructions[line]

        if line in visited:
            raise InfiniteLoop
        else:
            visited.append(line)

        if instruction.op == "acc":
            acc += instruction.num
            line += 1
        elif instruction.op == "jmp":
            line += instruction.num
        elif instruction.op == "nop":
            line += 1
        else:
            raise ValueError("should never hit this!")


def find_acc_after_fix(instructions: List[Instruction]) -> int:
    for i, instr in enumerate(instructions):
        if instr.op == "acc":
            continue
        
        new_instrutions = copy.copy(instructions)
        if instr.op == "jmp":
            new_instrutions[i] = Instruction(instr.line.replace("jmp", "nop"))
        elif instr.op == "nop":
            new_instrutions[i] = Instruction(instr.line.replace("nop", "jmp"))
        else:
            raise ValueError("should never hit this!")

        try:
            acc = run_boot_code(new_instrutions)
        except (InfiniteLoop, TooFar):
            continue
        else:
            return acc


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        instructions = [Instruction(line.rstrip()) for line in f.readlines()]

    print(find_acc_after_fix(instructions))
