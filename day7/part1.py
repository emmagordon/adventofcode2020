#!/usr/bin/env python3

import re
from typing import Dict

PUZZLE_INPUT = "input.txt"


class Rule:
    def __init__(self, rule: str) -> None:
        colour, contains = rule.split(" bags contain ")
        self.colour = colour
        self.contains = {}
        if "no other bags" in contains:
            return
        for s in contains.split(","):
            m = re.match(r"[ ]*(\d+) (.*) bag[s]*[\.]*", s).groups()
            self.contains[m[1]] = int(m[0])
    
    def __repr__(self):
        return f"'{self.colour}' contains {self.contains}"


def find_num_that_can_contain(rules: Dict[str, Rule], colour: str) -> int:
    return sum(
        rule_can_contain_colour(rules, rule, colour)
        for rule in rules.values()
    )


def rule_can_contain_colour(rules: Dict[str, Rule], rule: Rule, colour: str) -> bool:
    if not rule.contains:
        return False
    
    contains_colours = rule.contains.keys()

    if colour in contains_colours:
        return True
    
    return any([
        rule_can_contain_colour(rules, rules[col], colour)
         for col in contains_colours
    ])


def num_bags_inside(rules: Dict[str, Rule], colour: str) -> int:
    rule = rules[colour]

    if not rule.contains:
        return 0
    
    return sum([
        (bag_count * (1 + num_bags_inside(rules, bag_colour)))
        for bag_colour, bag_count in rule.contains.items()
    ])


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [Rule(line) for line in f.readlines()]
    
    rules = {rule.colour: rule for rule in puzzle_input}
    
    print(find_num_that_can_contain(rules, "shiny gold"))
    print(num_bags_inside(rules, "shiny gold"))
