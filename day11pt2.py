#!/usr/bin/env python3

from intcode.util import read
from intcode.util import update
from intcode.machine import IntCodeComputer


def main():
    memory = read()
    intcode = IntCodeComputer(memory)
    white_tiles = set()
    painted = set()
    curr = [0, 0]
    white_tiles.add(tuple(curr))
    turn_to_paint = True
    face = 0
    directions = ['U', 'R', 'D', 'L']
    min_x = 10e9
    min_y = 10e9
    max_x = -10e9
    max_y = -10e9
    while not intcode.completed:
        intcode.run()

        while not intcode.output.empty():
            value = intcode.output.get()
            if turn_to_paint:
                if value == 1:
                    white_tiles.add(tuple(curr))
                elif value == 0 and tuple(curr) in white_tiles:
                    white_tiles.remove(tuple(curr))
                painted.add(tuple(curr))
                min_x = min(min_x, curr[0])
                min_y = min(min_y, curr[1])
                max_x = max(max_x, curr[0])
                max_y = max(max_y, curr[1])
            else:
                if value == 1:
                    face = (face + 5) % 4
                elif value == 0:
                    face = (face + 3) % 4
                update(curr, directions[face])
            turn_to_paint = not turn_to_paint

        intcode.read(int(tuple(curr) in white_tiles))

    for j in range(max_y, min_y - 1, -1):
        for i in range(min_x, max_x + 1):
            if (i, j) in white_tiles:
                print("*", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()
