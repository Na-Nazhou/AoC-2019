from intcode.util import read
from intcode.IntCodeComputer import IntCodeComputer


def main():
    memory = read()
    memory[0] = 2
    intcode = IntCodeComputer(memory)
    ball_x = -1
    paddle_x = -1
    score = -1
    while not intcode.completed:
        intcode.run()
        while not intcode.output.empty():
            x = intcode.output.get()
            y = intcode.output.get()
            tile_id = intcode.output.get()
            if x == -1 and y == 0:
                score = tile_id
            if tile_id == 3:
                paddle_x = x
            elif tile_id == 4:
                ball_x = x
        if paddle_x < ball_x:
            ipt = 1
        elif paddle_x > ball_x:
            ipt = -1
        else:
            ipt = 0
        intcode.read(ipt)
    print(score)


if __name__ == "__main__":
    main()
