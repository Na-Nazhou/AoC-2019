from .util import read
from .IntCodeComputer import IntCodeComputer


def launch():
    memory = read()
    ipt = int(input())  # input
    intcode = IntCodeComputer(memory)
    intcode.read(ipt)
    intcode.run()
    while not intcode.output.empty():
        print(intcode.output.get())  # output
