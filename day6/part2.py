from enum import Enum

with open("input") as f:
    table = [[i for i in l.strip()] for l in f.readlines()]


def find_cursor():
    for i, l in enumerate(table):
        for j, c in enumerate(l):
            if c == "^":
                return i, j


def surrounds_repeated(curr_pos: tuple[int, int], visited: list[tuple[int, int]]):
    first = None
    # no no no no yes [no no no] yes [no no no]
    visited = visited[visited.index(curr_pos) + 1 :]
    # [no no no] yes [no no no]
    while curr_pos in visited:
        first = visited[: visited.index(curr_pos)]
        visited = visited[visited.index(curr_pos) + 1 :]
    return first == visited


class dir(Enum):
    up = lambda pos: (pos[0] - 1, pos[1])
    down = lambda pos: (pos[0] + 1, pos[1])
    left = lambda pos: (pos[0], pos[1] - 1)
    right = lambda pos: (pos[0], pos[1] + 1)


order = [dir.up, dir.right, dir.down, dir.left]
len_x = len(table)
len_y = len(table[0])


def run(curr_block, curr_pos, curr_dir):
    print(curr_block)
    visited = []
    while True:
        next_pos = curr_dir(curr_pos)
        if (
            next_pos[0] < 0
            or next_pos[0] >= len_y
            or next_pos[1] < 0
            or next_pos[1] >= len_x
        ):
            return False
        if next_pos == curr_block or table[next_pos[0]][next_pos[1]] == "#":
            curr_dir = order[(order.index(curr_dir) + 1) % len(order)]
        else:
            if visited.count(curr_pos) >= 2 and surrounds_repeated(curr_pos, visited):
                return True
            visited.append(curr_pos)
            curr_pos = next_pos


curr_pos = find_cursor()
curr_dir = dir.up
sum = 0

for i, l in enumerate(table):
    for j, c in enumerate(l):
        if c != ".":
            continue
        curr_block = i, j
        if run(curr_block, curr_pos, curr_dir):
            sum += 1

print(sum)
