from intcode.util import read
from intcode.IntCodeComputer import IntCodeComputer


def read_input(intcode, ipt):
    for ch in ipt:
        intcode.read(ord(ch))
    intcode.run()
    while not intcode.output.empty():
        # print(chr(intcode.output.get()), end="")
        print(intcode.output.get())


def main():
    memory = read()
    memory[0] = 2
    intcode = IntCodeComputer(memory)
    routine = "A,A,B,C,B,C,B,C,B,A\n"
    function_A = "L,10,L,8,R,8,L,8,R,6\n"
    function_B = "R,6,R,8,R,8\n"
    function_C = "R,6,R,6,L,8,L,10\n"
    continuous = "n\n"
    read_input(intcode, routine + function_A +
               function_B + function_C + continuous)


if __name__ == "__main__":
    main()

# L 10 L 8 R 8 L 8 R 6 A
# L 10 L 8 R 8 L 8 R 6 A
# R 6 R 8 R 8          B
# R 6 R 6 L 8 L 10     C
# R 6 R 8 R 8          B
# R 6 R 6 L 8 L 10     C
# R 6 R 8 R 8          B
# R 6 R 6 L 8 L 10     C
# R 6 R 8 R 8          B
# L 10 L 8 R 8 L 8 R 6 A
