#!/usr/bin/env python3

from typing import List

PUZZLE_INPUT = '389125467'  # example
# PUZZLE_INPUT = '598162734'  # actual
MOVES = 10_000_000
PICK_UP = 3


class Cup:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"Cup({self.value})"


class Circle:
    def __init__(self, cups: List[Cup]) -> None:
        cups.extend(Cup(i) for i in range(10, 1_000_001))
        for (i, cup) in enumerate(cups[:-1]):
            cup.next = cups[(i + 1)]
        cups[-1].next = cups[0]

        self.current = cups[0]
        self.min = min(c.value for c in cups)
        self.max = max(c.value for c in cups)

    def move(self) -> None:
        picked_up = self.current.next
        self.current.next = picked_up.next.next.next  # re-form the circle
        picked_up.next.next.next = None  # only take 3 cups

        cup = picked_up
        picked_up_values = []
        while cup is not None:
            picked_up_values.append(cup.value)
            cup = cup.next
        # print(picked_up_values)

        # find destination cup to insert after
        destination = (self.current.value - 1)
        if destination < self.min:
            destination = self.max
        while (destination in picked_up_values):
            destination -= 1
            if destination < self.min:
                destination = self.max
        # print(destination)

        # re-insert cups
        cup = self.current
        while cup.value != destination:
            cup = cup.next
        tmp = cup.next
        cup.next = picked_up
        while cup.next is not None:
            cup = cup.next
        cup.next = tmp

        # rotate current cup clockwise by 1
        self.current = self.current.next

    def next_value_after_cup(self, n: int) -> int:
        cup = self.current
        while cup.value != n:
            cup = cup.next
        next_cup = cup.next
        return next_cup.value

    def __repr__(self) -> str:
        output = []
        cup = self.current
        while True:
            s = f"({cup.value})" if cup == self.current else str(cup.value)
            output.append(s)
            cup = cup.next
            if cup == self.current:
                break
        return " ".join(output)


if __name__ == "__main__":
    cups = [Cup(int(n)) for n in PUZZLE_INPUT]
    circle = Circle(cups)
    # print(circle)
    for i in range(MOVES):
        # if (i % 1000) == 0:
        #     print(i)
        circle.move()
        # print(circle)
    
    n = circle.next_value_after_cup(1)
    m = circle.next_value_after_cup(n)
    print(n * m)
