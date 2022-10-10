#!/usr/bin/env python3

from collections import namedtuple, defaultdict
from itertools import combinations_with_replacement, permutations
import re
from typing import List, Set, Tuple

PUZZLE_INPUT = "input.txt"
INTEGER_SIZE = 36

Instruction = namedtuple("Instruction", "mem_addr num")


def masked_mem_addrs(mem_addr: int, mask: str) -> List[int]:
    bin_mem_addr = format(mem_addr, 'b').zfill(INTEGER_SIZE)
    masked_addr = "".join(
        m if m != "0" else n
        for (n, m) in zip(bin_mem_addr, mask)
    )
    num_xs_in_mask = sum(1 for c in mask if c.upper() == 'X')
    x_substitutions = {
        p
        for c in combinations_with_replacement('10', num_xs_in_mask)
        for p in permutations(c)
    }
    return [
        int(substitute(masked_addr, x_sub), 2)
        for x_sub in x_substitutions
    ]


def substitute(masked_addr: str, x_substitutions: Tuple[str]) -> str:
    i = 0
    output = []
    addr_bits = [b for b in masked_addr]
    for bit in addr_bits:
        if bit.upper() == "X":
            output.append(x_substitutions[i])
            i += 1
        else:
            output.append(bit)
    return "".join(output)


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    mask = None
    memory = defaultdict(int)

    for i, line in enumerate(puzzle_input):
        print(i)
        if line.startswith("mask"):
            mask = re.match(r'^mask = ([X10]*$)', line).groups()[0]
        else:
            instr = Instruction(*[
                int(n) for n in 
                re.match(r'^mem\[(\d+)\] = (\d+)$', line).groups()
            ])
            masked_addrs = masked_mem_addrs(instr.mem_addr, mask)
            for mem_addr in masked_addrs:
                memory[mem_addr] = instr.num

    print(sum(memory.values()))
