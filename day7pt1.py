#!/usr/bin/env python3

import itertools
from intcode.util import read
from intcode.machine import IntCodeComputer


def main():
    memory = read()
    perms = list(itertools.permutations(range(5)))
    max_signal = -10e9
    for perm in perms:
        output = 0
        for idx, phase in enumerate(perm):
            amplifier = IntCodeComputer(memory)
            amplifier.read(phase)
            amplifier.read(output)
            amplifier.run()
            output = amplifier.output.get()
        max_signal = max(output, max_signal)
    print(max_signal)  # output


if __name__ == "__main__":
    main()
