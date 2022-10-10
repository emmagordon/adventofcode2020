#!/usr/bin/env python3

# PUZZLE_INPUT = '389125467'  # example
PUZZLE_INPUT = '598162734'  # actual
MOVES = 100

if __name__ == "__main__":
    circle = [int(n) for n in PUZZLE_INPUT]

    for _ in range(MOVES):
        current = circle[0]
        picked_up = circle[1:4]
        circle = [circle[0]] + circle[4:]
        destination = (current - 1)
        if destination < 1:
            destination = 9
        while (destination in picked_up):
            destination -= 1
            if destination < 1:
                destination = 9
        dest_idx = circle.index(destination)
        circle = circle[:(dest_idx + 1)] + picked_up + circle[(dest_idx + 1):]
        cur_idx = circle.index(current) + 1
        circle = circle[cur_idx:] + circle[:cur_idx]

    print(''.join(''.join(str(n) for n in circle).split('1')[::-1]))
    
