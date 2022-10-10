#!/usr/bin/env python3

import copy
from typing import List, Tuple

PUZZLE_INPUT = "input.txt"

OCCUPIED_SEAT = "#"
EMPTY_SEAT = "L"
FLOOR = "."
UNOCCUPIED = [FLOOR, EMPTY_SEAT]


def empty_seat_rule(visible_seats: List[str]) -> str:
    return (
        EMPTY_SEAT if any(s == OCCUPIED_SEAT for s in visible_seats)
        else OCCUPIED_SEAT
    )


def occupied_seat_rule(visible_seats: List[str]) -> str:
    num_adj_occupied = len([s for s in visible_seats if s == OCCUPIED_SEAT])
    return (
        OCCUPIED_SEAT if (num_adj_occupied < 5)
        else EMPTY_SEAT
    )


def floor_rule(visible_seats: List[str]) -> str:
    return FLOOR


RULES = {
    EMPTY_SEAT: empty_seat_rule,
    OCCUPIED_SEAT: occupied_seat_rule,
    FLOOR: floor_rule
}


def transition(layout: List[str]) -> List[str]:
    new_layout = copy.deepcopy(layout)
    for x, row in enumerate(layout):
        for y, _ in enumerate(row):
            seat = layout[x][y]
            vis_seats = visible_seats(layout, (x, y))
            new_layout[x][y] = RULES[seat](vis_seats)
    return new_layout


def visible_seats(layout: List[str], co_ord: Tuple[int, int]) -> List[str]:
    directions = [(-1,0),(-1,+1),(0,+1),(+1,+1),(+1,0),(+1,-1),(0,-1),(-1,-1)]
    vis_seats = []
    for (delta_x, delta_y) in directions:
        pos = co_ord
        while True:
            pos = (pos[0]+delta_x, pos[1]+delta_y)
            x, y = pos
            if (x < 0) or (y < 0):
                break
            try:
                seat = layout[x][y]
                if seat in [OCCUPIED_SEAT, EMPTY_SEAT]:
                    vis_seats.append(seat)
                    break
            except IndexError:
                break
    return vis_seats


def num_occupied_seats(layout: List[str]) -> int:
    return sum([1 for row in layout for s in row if s == OCCUPIED_SEAT])


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        seat_layout = [[c for c in line.rstrip()] for line in f.readlines()]

    prev_num_occupied = num_occupied_seats(seat_layout)
    # for row in seat_layout:
    #     print("".join(row))
    # print(prev_num_occupied)

    while True:
        seat_layout = transition(seat_layout)
        # print('------------------------------------------------')
        # for row in seat_layout:
        #     print("".join(row))
        num_occupied = num_occupied_seats(seat_layout)
        if num_occupied == prev_num_occupied:
            break
        prev_num_occupied = num_occupied

    print(num_occupied)
