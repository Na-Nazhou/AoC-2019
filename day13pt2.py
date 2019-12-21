from intcode.util import read
from intcode.IntCodeComputer import IntCodeComputer


def main():
    memory = read()
    # memory[0] = 2
    intcode = IntCodeComputer(memory)
    screen = {}
    min_x = 10e9
    min_y = 10e9
    max_x = -10e9
    max_y = -10e9
    while not intcode.completed:
        intcode.run()
        while not intcode.output.empty():
            x = intcode.output.get()
            y = intcode.output.get()
            tile_id = intcode.output.get()
            screen[(x, y)] = tile_id
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    for j in range(min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            if screen[(i, j)] == 0:
                print(" ", end="")
            elif screen[(i, j)] == 1:
                print("w", end="")
            elif screen[(i, j)] == 2:
                print("b", end="")
            elif screen[(i, j)] == 3:
                print("_", end="")
            elif screen[(i, j)] == 4:
                print("*", end="")
        print()


if __name__ == "__main__":
    main()
