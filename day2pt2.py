#!/usr/bin/env python3

import copy
from intcode.util import read
from intcode.util import run


def main():
    memory = read()
    mem_copy = copy.deepcopy(memory)
    for i in range(100):
        for j in range(100):
            memory[1] = i
            memory[2] = j
            run(memory)
            if memory[0] == 19690720:  # additional input
                print(100 * i + j)  # output
                return
            memory = copy.deepcopy(mem_copy)


if __name__ == "__main__":
    main()
