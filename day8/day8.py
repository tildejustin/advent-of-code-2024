# find annatenna of a type
# go through every pair of every time and collect antinode positions within bounds

with open("input") as f:
    board = [list(l.strip()) for l in f.readlines()]

anntennas = {}
for y, l in enumerate(board):
    for x, c in enumerate(l):
        if c == ".":
            continue
        anntennas.setdefault(c, set()).add((y, x))

antinodes = set()
for locations in anntennas.values():
    for first in locations:
        for second in locations:
            if first == second:
                continue
            # x2 + (x2 - x1), y2 + (y2 - y1)
            y = second[0] + (second[0] - first[0])
            x = second[1] + (second[1] - first[1])
            if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
                continue
            antinodes.add((y, x))
print(len(antinodes))

antinodes = set()
for locations in anntennas.values():
    for first in locations:
        for second in locations:
            if first == second:
                continue
            antinodes.add(second)
            diffy = second[0] - first[0]
            diffx = second[1] - first[1]
            y = second[0]
            x = second[1]
            while (True):
                y += diffy
                x += diffx
                if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
                    break
                antinodes.add((y, x))

print(len(antinodes))

# for y in range(len(board)):
#     for x in range(len(board[0])):
#         if (y, x) in antinodes:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print("")
