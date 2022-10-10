#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"

class Password:
    def __init__(self, entry):
        pwd = entry.split()
        self.password = pwd[2]
        self.char = pwd[1][0]
        self.pos1 = int(pwd[0].split("-")[0]) - 1
        self.pos2 = int(pwd[0].split("-")[1]) - 1
    
    @property
    def is_valid(self):
        valid_chars = [
            c for c in [self.password[self.pos1], self.password[self.pos2]]
            if c == self.char
        ]
        return len(valid_chars) == 1

    def __repr__(self):
        return f"{self.password}, policy={self.char}[{self.pos1}|{self.pos2}]"


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [Password(s) for s in f.readlines()]
    
    print(len([p for p in puzzle_input if p.is_valid]))
