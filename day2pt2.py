#!/usr/bin/env python3

from intcode.util import read
from intcode.IntCodeComputer import IntCodeComputer


def main():
    memory = read()
    for i in range(100):
        for j in range(100):
            intcode = IntCodeComputer(memory)
            intcode.memory[1] = i
            intcode.memory[2] = j
            intcode.run()
            if intcode.memory[0] == 19690720:  # additional input
                print(100 * i + j)  # output
                return


if __name__ == "__main__":
    main()
