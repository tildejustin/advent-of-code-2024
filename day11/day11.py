with open("input") as f:
    stones = [int(x) for x in f.read().strip().split(" ")]

for _ in range(25):
    i = 0
    while i < len(stones):
        stone = stones[i]
        stone_str = str(stone)
        stone_len = len(stone_str)
        if stone == 0:
            stones[i] = 1
        elif stone_len % 2 != 0:
            stones[i] = stones[i] * 2024
        else:
            first = int(stone_str[: stone_len // 2])
            second = int(stone_str[stone_len // 2 :])
            stones[i] = first
            stones.append(second)
            i += 1
        i += 1

print(len(stones))
