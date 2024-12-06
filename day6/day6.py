from enum import Enum

with open("input") as f:
    table = [[i for i in l.strip()] for l in f.readlines()]


def find_cursor():
    for i, l in enumerate(table):
        for j, c in enumerate(l):
            if c == "^":
                return i, j


class dir(Enum):
    up = lambda pos: (pos[0] - 1, pos[1])
    down = lambda pos: (pos[0] + 1, pos[1])
    left = lambda pos: (pos[0], pos[1] - 1)
    right = lambda pos: (pos[0], pos[1] + 1)


order = [dir.up, dir.right, dir.down, dir.left]
len_x = len(table)
len_y = len(table[0])
visited: set[tuple[int, int]] = set()
curr_pos = find_cursor()
curr_dir = dir.up

while True:
    visited.add(curr_pos)
    next_pos = curr_dir(curr_pos)
    if (
        next_pos[0] < 0
        or next_pos[0] >= len_y
        or next_pos[1] < 0
        or next_pos[1] >= len_x
    ):
        break
    if table[next_pos[0]][next_pos[1]] == "#":
        curr_dir = order[(order.index(curr_dir) + 1) % len(order)]
    else:
        curr_pos = next_pos

print(len(visited))
