#!/usr/bin/env python3

import math
from typing import List

PUZZLE_INPUT = "input.txt"

ROW_LOW = 0
ROW_HIGH = 127
COLUMN_LOW = 0
COLUMN_HIGH = 7

BINARY_MAPPING = {
    "F": "0",
    "B": "1",
    "L": "0",
    "R": "1"
}


def decode(binary_location: str, low: int, high: int):
    if low == high:
        return low
    
    mid = (low + high) / 2
    head, tail = binary_location[0], binary_location[1:]

    if head == "0":
        return decode(tail, low, math.floor(mid))
    elif head == "1":
        return decode(tail, math.ceil(mid), high)
    else:
        raise ValueError("Should never hit this!")


class BoardingPass:
    def __init__(self, seat_location: str):
        self.seat_location = seat_location
        binary_location = "".join(BINARY_MAPPING[c] for c in seat_location)
        self.row = decode(binary_location[:7], ROW_LOW, ROW_HIGH)
        self.column = decode(binary_location[7:], COLUMN_LOW, COLUMN_HIGH)
    
    @property
    def uid(self):
        return (self.row * 8) + self.column

    def __repr__(self):
        return f"{self.seat_location}: row {self.row}, column {self.column}, seat ID {self.uid}"


def find_empty_seat_id(boarding_passes: List[BoardingPass]) -> int:
    sorted_seat_ids = sorted([b.uid for b in boarding_passes])
    prev_id = sorted_seat_ids[0]
    for _id in sorted_seat_ids[1:]:
        if _id == (prev_id + 1):
            prev_id = _id
        else:
            return (prev_id + 1)
    
    raise ValueError("Should never hit this!")


if __name__ == "__main__":
    with open(PUZZLE_INPUT) as f:
        boarding_passes = [BoardingPass(line.rstrip()) for line in f.readlines()]
    
    # print(max(boarding_passes, key=lambda x: x.uid))
    print(find_empty_seat_id(boarding_passes))
