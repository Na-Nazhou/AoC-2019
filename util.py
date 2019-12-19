def update(curr, direction):
    if direction == 'U':
        curr[1] += 1
    if direction == 'D':
        curr[1] -= 1
    if direction == 'R':
        curr[0] += 1
    if direction == 'L':
        curr[0] -= 1


def draw(predicate):
    if predicate is True:
        print("*", end="")
    else:
        print(" ", end="")
