#!/usr/bin/env python3

PUZZLE_INPUT = "input.txt"


def parse_groups(puzzle_input):
    count = 0
    group_answers = set()
    reset_group_answers = True

    for line in puzzle_input:
        if reset_group_answers:
            group_answers = set(line)
            reset_group_answers = False
        elif line:
            group_answers = group_answers.intersection(set(line))
        else:
            count += len(group_answers)
            reset_group_answers = True
    
    if group_answers:
        count += len(group_answers)
    
    return count


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    print(parse_groups(puzzle_input))
    