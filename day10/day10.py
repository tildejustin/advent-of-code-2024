trailheads = set()
peaks = set()

with open("input") as f:
    board = [[int(c) if c != "." else "." for c in l.strip()] for l in f.readlines()]

# nesw order
def surrounds(pos: tuple[int, int]) -> list[tuple[int, int]]:
    val = board[pos[0]][pos[1]]
    result = []
    if pos[0] + 1 < len(board) and board[pos[0] + 1][pos[1]] == val + 1:
        result.append((pos[0] + 1, pos[1]))
    if pos[1] + 1 < len(board[0]) and board[pos[0]][pos[1] + 1] == val + 1:
        result.append((pos[0], pos[1] + 1))
    if pos[0] - 1 >= 0 and board[pos[0] - 1][pos[1]] == val + 1:
        result.append((pos[0] - 1, pos[1]))
    if pos[1] - 1 >= 0 and board[pos[0]][pos[1] - 1] == val + 1:
        result.append((pos[0], pos[1] - 1))
    return result


def count_trails(start) -> int:
    # check recursively clockwise, stopping when hitting a 9 or can go no more directions
    queue = []
    found = set()
    next = surrounds(start)
    if len(next) == 0:
        return 0
    queue.append((start[0], start[1], next))
    while True:
        working = queue[-1]
        while len(working[2]) == 0:
            queue.pop()
            if len(queue) == 0:
                print(found)
                print(len(found))
                return len(found)
            working = queue[-1]
        next = working[2].pop()
        if board[next[0]][next[1]] == 9:
            found.add(next)
            continue
        queue.append((next[0], next[1], surrounds(next)))
        print(queue)

def count_trails_2(start) -> int:
    queue = []
    found = []
    next = surrounds(start)
    if len(next) == 0:
        return 0
    queue.append((start[0], start[1], next))
    while True:
        working = queue[-1]
        while len(working[2]) == 0:
            queue.pop()
            if len(queue) == 0:
                return len(found)
            working = queue[-1]
        next = working[2].pop()
        if board[next[0]][next[1]] == 9:
            found.append(next)
            continue
        queue.append((next[0], next[1], surrounds(next)))


for y, line in enumerate(board):
    for x, height in enumerate(line):
        if height == 0:
            trailheads.add((y, x))
        elif height == 9:
            peaks.add((y, x))

print(sum(map(count_trails, trailheads)))

print(sum(map(count_trails_2, trailheads)))
