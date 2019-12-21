import queue
import copy


class IntCodeComputer:
    def __init__(self, memory):
        self.memory = copy.deepcopy(memory)
        self.input = queue.Queue()
        self.output = queue.Queue()
        self.pc = 0
        self.base = 0
        self.completed = False

    def get_param_idx(self, idx, mode):
        if mode in [0, 2]:
            if mode == 0:
                offset = 0
            elif mode == 2:
                offset = self.base
            return self.memory.get(idx, 0) + offset
        elif mode == 1:
            return idx

    def get_param(self, idx, mode):
        param_idx = self.get_param_idx(idx, mode)
        return self.memory.get(param_idx, 0)

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

    def read(self, value):
        self.input.put(value)

    def copy(self):
        copy = IntCodeComputer(self.memory)
        copy.input = self.input
        copy.output = self.output
        copy.pc = self.pc
        copy.base = self.base
        copy.completed = self.completed
        return copy

    def run(self):
        while not self.completed:
            opcode = self.memory[self.pc]
            DE = opcode % 100
            C = (opcode // 100) % 10
            B = (opcode // 1000) % 10
            A = opcode // 10000
            if DE == 99:
                self.pc += 1
                self.completed = True
            if DE in [1, 2, 7, 8]:
                param1 = self.get_param(self.pc + 1, C)
                param2 = self.get_param(self.pc + 2, B)
                result = self.get_result(param1, param2, DE)
                param_idx = self.get_param_idx(self.pc + 3, A)
                self.memory[param_idx] = result
                self.pc += 4
            if DE == 3:
                if self.input.empty():
                    break
                param_idx = self.get_param_idx(self.pc + 1, C)
                self.memory[param_idx] = self.input.get()
                self.pc += 2
            if DE == 4:
                param1 = self.get_param(self.pc + 1, C)
                self.output.put(param1)
                self.pc += 2
            if DE in [5, 6]:
                param1 = self.get_param(self.pc + 1, C)
                if self.get_jump(param1, DE):
                    param2 = self.get_param(self.pc + 2, B)
                    self.pc = param2
                else:
                    self.pc += 3
            if DE == 9:
                param1 = self.get_param(self.pc + 1, C)
                self.base += param1
                self.pc += 2
