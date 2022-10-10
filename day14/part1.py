#!/usr/bin/env python3

from collections import namedtuple, defaultdict
import re

PUZZLE_INPUT = "input.txt"
INTEGER_SIZE = 36

Instruction = namedtuple("Instruction", "mem_addr num")


def masked_num(num: int, mask: str) -> int:
    bin_num_str = format(num, 'b').zfill(INTEGER_SIZE)
    output = "".join(
        m if m != "X" else n
        for (n, m) in zip(bin_num_str, mask)
    )
    return int(output, 2)


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    mask = None
    memory = defaultdict(int)

    for line in puzzle_input:
        if line.startswith("mask"):
            mask = re.match(r'^mask = ([X10]*$)', line).groups()[0]
        else:
            instr = Instruction(*[
                int(n) for n in 
                re.match(r'^mem\[(\d+)\] = (\d+)$', line).groups()
            ])
            memory[instr.mem_addr] = masked_num(instr.num, mask)

    print(sum(memory.values()))
