#!/usr/bin/env python3

import re

PUZZLE_INPUT = "input_part1.txt"


def is_integer(num: str) -> bool:
    try:
        int(num)
    except ValueError:
        return False
    return True


class Rule:
    def __init__(self, rule: str) -> None:
        self.num = int(rule.split(":")[0])
        self.rule = rule.split(":")[1].strip()

    def regex(self, rules) -> str:
        if re.match('"[a-zA-Z]{1}"', self.rule):
            return self.rule[1]

        options = [
            f'({"".join(rules[int(n)].regex(rules) for n in opt.split())})'
            for opt in self.rule.split("|")
        ]
        rgx = f'({"|".join(options)})'
        return (r'^' + rgx + r'$') if (self.num == 0) else rgx
        

    def __repr__(self):
        return f"{self.rule}"


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    rules = {}
    messages = []
    for line in puzzle_input:
        if not line:
            continue
        elif is_integer(line[0]):
            rule = Rule(line)
            rules[rule.num] = rule
        else:
            messages.append(line)
    
    # for rule in rules.values():
    #     print(f'{rule.num}: {rule.regex(rules)}')
    print(sum(1 for m in messages if re.match(rules[0].regex(rules), m)))
