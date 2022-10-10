#!/usr/bin/env python3

PUZZLE_INPUT = "input.txt"


def parse_groups(puzzle_input):
    groups = []
    group_answers = ""
    for line in puzzle_input:
        if line:
            group_answers += line
        else:
            groups.append(group_answers)
            group_answers = ""
    
    if group_answers:
        groups.append(group_answers)
    
    return groups


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    groups = parse_groups(puzzle_input)

    count = sum([len(set(group_answers)) for group_answers in groups])
    print(count)
    