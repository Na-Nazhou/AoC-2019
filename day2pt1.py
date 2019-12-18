#!/usr/bin/env python3

from intcode.util import read
from intcode.machine import IntCodeComputer


def main():
    memory = read()
    intcode = IntCodeComputer(memory)
    intcode.run()
    print(intcode.memory[0])  # output


if __name__ == "__main__":
    main()
