import re

# part 1
# assumes len on x and len on y is constant
with open("input") as f:
    sum = 0
    # (y, x)
    board = [s.strip() for s in f.readlines()]
    len_x = len(board[0]) - 1
    len_y = len(board) - 1
    effective_len = min(len_x, len_y)
    for i in range(len(board)):
        pattern = "XMAS"
        s = [
            # forward
            board[i],
            # reverse
            board[i][::-1],
            # down
            "".join(x[i] for x in board),
            # up
            "".join(x[i] for x in board[::-1]),
        ]
        if i != 0 and i != effective_len:
            s.extend(
                [
                    # left to top
                    "".join(board[i - j][j] for j in range(i + 1)),
                    # left to bottom
                    "".join(board[i + j][j] for j in range(effective_len - i + 1)),
                    # right to top
                    "".join(board[i - j][effective_len - j] for j in range(i + 1)),
                    # right to bottom
                    "".join(
                        board[i + j][effective_len - j]
                        for j in range(effective_len - i + 1)
                    ),
                ]
            )
        if i != effective_len:
            s.extend(
                [
                    # top to right
                    "".join(board[j][i + j] for j in range(effective_len - i + 1)),
                    # bottom to right
                    "".join(
                        board[effective_len - j][i + j]
                        for j in range(effective_len - i + 1)
                    ),
                ]
            )
        if i != 0:
            s.extend(
                [
                    # top to left
                    "".join(board[j][i - j] for j in range(i + 1)),
                    # bottom to left
                    "".join(board[effective_len - j][i - j] for j in range(i + 1)),
                ]
            )
        sum += len(re.findall(pattern, " ".join(s)))
    print(sum)

    # part 2
    # with open("input") as f:
    sum = 0
    # board = [s.strip() for s in f.readlines()]
    # for each pos in 1, -1 of bounds, check -1, -1 and 1, -1 for M, 0, 0 for A, -1, 1 and 1, 1 for S
    for i in range(1, len(board) - 1):
        for j in range(1, len(board[i]) - 1):
            reverse_char = lambda c: "S" if c == "M" else "M"
            if (
                board[i][j] == "A"
                and (c := board[i - 1][j - 1]) in ["M", "S"]
                and board[i + 1][j + 1] == reverse_char(c)
                and (c := board[i + 1][j - 1]) in ["M", "S"]
                and board[i - 1][j + 1] == reverse_char(c)
            ):
                sum += 1
    print(sum)
