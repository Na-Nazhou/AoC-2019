#!/usr/bin/env python3

import sys
import copy
import itertools


class Amplifier:
    def __init__(self, arr, phase):
        self.arr = copy.deepcopy(arr)
        self.i = 0
        self.phase = phase
        self.isFirst = True

    def get_param(self, i, mode):
        if mode == 0:
            return self.arr[self.arr[i]]
        elif mode == 1:
            return self.arr[i]

    def get_result(self, param1, param2, DE):
        if DE == 1:
            return param1 + param2
        elif DE == 2:
            return param1 * param2
        elif DE == 7:
            return int(param1 < param2)
        elif DE == 8:
            return int(param1 == param2)

    def get_jump(self, param, DE):
        if DE == 5:
            return param != 0
        elif DE == 6:
            return param == 0

    def get_output(self, ipt):
        while self.i < len(self.arr):
            opcode = self.arr[self.i]
            DE = opcode % 100
            C = (opcode // 100) % 10
            B = (opcode // 1000) % 10
            A = opcode // 10000
            if DE == 99:
                self.i += 1
                return None
            if DE in [1, 2, 7, 8]:
                param1 = self.get_param(self.i + 1, C)
                param2 = self.get_param(self.i + 2, B)
                result = self.get_result(param1, param2, DE)
                self.arr[self.arr[self.i + 3]] = result
                self.i += 4
            if DE == 3:
                result = ipt
                if self.isFirst:
                    result = self.phase
                    self.isFirst = False
                self.arr[self.arr[self.i + 1]] = result
                self.i += 2
            if DE == 4:
                param1 = self.get_param(self.i + 1, C)
                self.i += 2
                return param1
            if DE in [5, 6]:
                param1 = self.get_param(self.i + 1, C)
                if self.get_jump(param1, DE):
                    param2 = self.get_param(self.i + 2, B)
                    self.i = param2
                else:
                    self.i += 3


def main():
    arr = [int(x) for x in sys.stdin.readline().strip().split(",")]
    perms = list(itertools.permutations(range(5, 10)))
    max_signal = -10e9

    for perm in perms:
        amplifers = []
        isFirst = True

        for i in range(5):
            amplifers.append(Amplifier(arr, perm[i]))

        while True:
            for i in range(5):
                if isFirst:
                    output = amplifers[i].get_output(0)
                    isFirst = False
                else:
                    output = amplifers[i].get_output(output)
                if output is None:
                    break
            if output is None:
                break
            final_output = output

        max_signal = max(final_output, max_signal)
    print(max_signal)  # output


if __name__ == "__main__":
    main()
