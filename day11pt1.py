#!/usr/bin/env python3

from intcode.util import read
from intcode.util import update
from intcode.util import IntCodeComputer


def main():
    memory = read()
    intcode = IntCodeComputer(memory)
    white_tiles = set()
    painted = set()
    curr = [0, 0]
    turn_to_paint = True
    face = 0
    directions = ['U', 'R', 'D', 'L']
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
            else:
                if value == 1:
                    face = (face + 5) % 4
                elif value == 0:
                    face = (face + 3) % 4
                update(curr, directions[face])
            turn_to_paint = not turn_to_paint

        intcode.read(int(tuple(curr) in white_tiles))

    print(len(painted))  # output


if __name__ == "__main__":
    main()
