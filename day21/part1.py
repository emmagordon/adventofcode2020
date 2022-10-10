#!/usr/bin/env python3

from collections import namedtuple
import re
from typing import Dict, List

PUZZLE_INPUT = "input.txt"

Food = namedtuple("Food", "ingredients allergens")


def get_algn_to_ingr_map(foods: List[Food]) -> Dict[str, str]:
    ps_of_elim = {}
    for food in foods:
        ingr_set = set(food.ingredients)
        for algn in food.allergens:
            ps_of_elim[algn] = (
                ingr_set
                if algn not in ps_of_elim else
                ps_of_elim[algn].intersection(ingr_set)
            )

    final_map = {}
    while True:
        for algn, ingrs in ps_of_elim.items():
            if len(ingrs) == 1:
                final_map[algn] = list(ingrs)[0]

        known_allergens = set(final_map.keys())
        known_ingredients = set(final_map.values())
        ps_of_elim = {
            algn: (set(ingrs) - known_ingredients)
            for algn, ingrs in ps_of_elim.items()
            if algn not in known_allergens
        }
        if not ps_of_elim:
            break

    return final_map


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]

    foods = []
    for line in puzzle_input:
        parts = line.split("(")
        ingrs = parts[0].rstrip().split()
        algns = parts[1][9:].rstrip(")").split(", ")
        foods.append(Food(ingrs, algns))

    _map = get_algn_to_ingr_map(foods)
    foods_containing_allergens = set(_map.values())

    # Part 1
    print(sum(
        sum(
            1 for i in food.ingredients
            if i not in foods_containing_allergens
        )
        for food in foods
    ))

    # Part 2
    print(",".join([
        ingr for (algn, ingr) in sorted(_map.items(), key=lambda item: item[0])])
    )
