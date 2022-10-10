#!/usr/bin/env python3

from collections import namedtuple
import re
from typing import List

PUZZLE_INPUT = "input.txt"

Range = namedtuple("Range", "lower upper")


def parse_input():
    rules = []
    our_ticket = None
    nearby_tickets = []
    with open(PUZZLE_INPUT) as f:
        line = f.readline().rstrip()
        while line:
            rules.append(Rule(line))
            line = f.readline().rstrip()
        
        f.readline().rstrip()
        our_ticket = [int(n) for n in f.readline().rstrip().split(',')]

        f.readline().rstrip()
        f.readline().rstrip()
        line = f.readline().rstrip()
        while line:
            nearby_tickets.append([int(n) for n in line.split(',')])
            line = f.readline().rstrip()
    
    return rules, our_ticket, nearby_tickets


class Rule:
    def __init__(self, rule: str) -> None:
        g = re.match(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$', rule).groups()
        self.name = g[0]
        self.r1 = Range(int(g[1]), int(g[2]))
        self.r2 = Range(int(g[3]), int(g[4]))
        self.rule = rule
    
    def in_range(self, num: int) -> bool:
        return (self.r1.lower <= num <= self.r1.upper) or (self.r2.lower <= num <= self.r2.upper) 

    def __repr__(self):
        return f'{self.name}: {self.r1.lower}-{self.r1.upper} or {self.r2.lower}-{self.r2.upper}'
        # return self.rule

def is_valid(ticket: List[int], rules: List[Rule]) -> bool:
    for num in ticket:
        if not any(r.in_range(num) for r in rules):
            return False
    return True


if __name__ == "__main__":
    rules, our_ticket, nearby_tickets = parse_input()
    valid_nearby_tickets = [t for t in nearby_tickets if is_valid(t, rules)]
    all_tickets = valid_nearby_tickets + [our_ticket]
    
    labels = [None] * len(rules)
    while True:
        for i, label in enumerate(labels):
            if label is not None:
                continue
            nums = [t[i] for t in all_tickets]
            remaining_rules = [r for r in rules if (not r.name in labels)]
            matching_rules = [
                rule for rule in remaining_rules
                if all(rule.in_range(n) for n in nums)
            ]
            if len(matching_rules) == 1:
                labels[i] = matching_rules[0].name

        if all((l is not None) for l in labels):
            break
    
    # print(labels)

    mul = 1
    for i, label in enumerate(labels):
        if label.startswith('departure'):
            mul *= our_ticket[i]
    
    print(mul)

