from intcode.util import read
from intcode.IntCodeComputer import IntCodeComputer


def main():
    memory = read()
    intcode = IntCodeComputer(memory)
    intcode.run()
    i = 0
    counter = 0
    while not intcode.output.empty():
        value = intcode.output.get()
        if i % 3 == 2 and value == 2:
            counter += 1
        i += 1
    print(counter)


if __name__ == "__main__":
    main()
