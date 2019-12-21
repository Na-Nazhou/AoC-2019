import queue
from intcode.util import read
from intcode.IntCodeComputer import IntCodeComputer


def bfs(memory):
    walls = set()
    visited = set()
    q = queue.Queue()
    intcode = IntCodeComputer(memory)
    q.put(((0, 0), intcode))

    while not q.empty():
        u, intcode = q.get()
        neighbors = [(u[0], u[1] + 1), (u[0], u[1] - 1),
                     (u[0] - 1, u[1]), (u[0] + 1, u[1])]
        for idx, neighbor in enumerate(neighbors):
            if neighbor not in visited:
                visited.add(neighbor)
                copy = intcode.copy()
                copy.read(idx + 1)
                copy.run()
                while not copy.output.empty():
                    status = copy.output.get()
                    if status == 0:
                        walls.add(neighbor)
                    elif status == 2:
                        dest = neighbor
                        q.put((neighbor, copy))
                    elif status == 1:
                        q.put((neighbor, copy))
    return (dest, walls)


def main():
    memory = read()
    dest, walls = bfs(memory)
    count = -1
    next_q = queue.Queue()
    next_q.put(dest)
    oxygen = set()
    oxygen.add(dest)
    while not next_q.empty():
        count += 1
        curr_q = next_q
        next_q = queue.Queue()
        while not curr_q.empty():
            u = curr_q.get()
            neighbors = [(u[0], u[1] + 1), (u[0], u[1] - 1),
                         (u[0] - 1, u[1]), (u[0] + 1, u[1])]
            for neighbor in neighbors:
                if neighbor not in walls and neighbor not in oxygen:
                    next_q.put(neighbor)
                    oxygen.add(neighbor)

    print(count)


if __name__ == "__main__":
    main()
