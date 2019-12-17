#!/usr/bin/env python3

from intcode.util import read
from intcode.util import run


def main():
    memory = read()
    run(memory)
    print(memory[0])  # output


if __name__ == "__main__":
    main()
