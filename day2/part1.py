#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = "input.txt"

class Password:
    def __init__(self, entry):
        pwd = entry.split()
        self.password = pwd[2]
        self.char = pwd[1][0]
        self.min_count = int(pwd[0].split("-")[0])
        self.max_count = int(pwd[0].split("-")[1])
    
    @property
    def is_valid(self):
        relevant_chars = [c for c in self.password if c == self.char]
        return self.min_count <= len(relevant_chars) <= self.max_count

    def __repr__(self):
        return f"{self.password}, policy={self.char}[{self.min_count}-{self.max_count}]"


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [Password(s) for s in f.readlines()]
    
    print(len([p for p in puzzle_input if p.is_valid]))
