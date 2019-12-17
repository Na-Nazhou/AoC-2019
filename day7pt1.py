#!/usr/bin/env python3

import copy
import itertools
from intcode.util import read
from intcode.util import get_param_idx
from intcode.util import get_param
from intcode.util import get_result
from intcode.util import get_jump


def get_output(mem_copy, input1, input2):
    memory = copy.deepcopy(mem_copy)
    i = 0
    base = 0
    isFirst = True
    while True:
        opcode = memory[i]
        DE = opcode % 100
        C = (opcode // 100) % 10
        B = (opcode // 1000) % 10
        A = opcode // 10000
        if DE == 99:
            i += 1
            break
        if DE in [1, 2, 7, 8]:
            param1 = get_param(memory, i + 1, C, base)
            param2 = get_param(memory, i + 2, B, base)
            result = get_result(param1, param2, DE)
            param_idx = get_param_idx(memory, i + 3, A, base)
            memory[param_idx] = result
            i += 4
        if DE == 3:
            result = input2
            if isFirst:
                result = input1
                isFirst = False
            param_idx = get_param_idx(memory, i + 1, C, base)
            memory[param_idx] = result
            i += 2
        if DE == 4:
            param1 = get_param(memory, i + 1, C, base)
            i += 2
            return param1
        if DE in [5, 6]:
            param1 = get_param(memory, i + 1, C, base)
            if get_jump(param1, DE):
                param2 = get_param(memory, i + 2, B, base)
                i = param2
            else:
                i += 3


def main():
    memory = read()
    perms = list(itertools.permutations(range(5)))
    max_signal = -10e9
    for perm in perms:
        for idx, ipt in enumerate(perm):
            if idx == 0:
                output = get_output(memory, ipt, 0)
            else:
                output = get_output(memory, ipt, output)
        max_signal = max(output, max_signal)
    print(max_signal)  # output


if __name__ == "__main__":
    main()
