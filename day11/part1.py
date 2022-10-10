#!/usr/bin/env python3

import copy
from typing import List, Tuple

PUZZLE_INPUT = "input.txt"

OCCUPIED_SEAT = "#"
EMPTY_SEAT = "L"
FLOOR = "."
UNOCCUPIED = [FLOOR, EMPTY_SEAT]


def empty_seat_rule(adj_seats: List[str]) -> str:
    return (
        EMPTY_SEAT if any(s == OCCUPIED_SEAT for s in adj_seats)
        else OCCUPIED_SEAT
    )


def occupied_seat_rule(adj_seats: List[str]) -> str:
    num_adj_occupied = len([s for s in adj_seats if s == OCCUPIED_SEAT])
    return (
        OCCUPIED_SEAT if (num_adj_occupied < 4)
        else EMPTY_SEAT
    )


def floor_rule(adj_seats: List[str]) -> str:
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
            adj_seats = adjacent_seats(layout, (x, y))
            seat = layout[x][y]
            new_layout[x][y] = RULES[seat](adj_seats)
    return new_layout


def adjacent_seats(layout: List[str], co_ord: Tuple[int, int]) -> List[str]:
    x, y = co_ord
    locs = [
        (x-1,y-1), (x-1,y), (x-1,y+1),
        (x,y-1), (x,y+1),
        (x+1,y-1), (x+1,y), (x+1,y+1)
    ]
    adj_seats = []
    for (i, j) in locs:
        if (i < 0) or (j < 0):
            continue
        try:
            adj_seats.append(layout[i][j])
        except IndexError:
            pass
    return adj_seats


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
