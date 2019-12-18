#!/usr/bin/env python3

import itertools
from intcode.util import read
from intcode.machine import IntCodeComputer


def main():
    memory = read()
    perms = list(itertools.permutations(range(5, 10)))
    max_signal = -10e9

    for perm in perms:
        amplifers = []
        isFirst = True
        halted = False

        for phase in perm:
            amplifier = IntCodeComputer(memory)
            amplifier.read(phase)
            amplifers.append(amplifier)

        output = 0
        while True:
            for amplifier in amplifers:
                amplifier.read(output)
                amplifier.run()
                if amplifier.output.empty():
                    halted = True
                    break
                output = amplifier.output.get()
            if halted:
                break
            final_output = output
        max_signal = max(final_output, max_signal)
    print(max_signal)  # output


if __name__ == "__main__":
    main()
