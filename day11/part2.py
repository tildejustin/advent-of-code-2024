import functools

with open("input") as f:
    stones = [int(x) for x in f.read().strip().split(" ")]

next = {}


# recursive solution
def get_next(stone: int, iter: int) -> int:
    print(iter)
    if iter == 0:
        return 1
    result = next.get((stone, iter))
    if result is not None:
        return result
    result = 0
    stone_str = str(stone)
    stone_len = len(stone_str)
    if stone == 0:
        result += get_next(1, iter - 1)
    elif stone_len % 2 != 0:
        result += get_next(stone * 2024, iter - 1)
    else:
        first = int(stone_str[: stone_len // 2])
        second = int(stone_str[stone_len // 2 :])
        result += get_next(first, iter - 1)
        result += get_next(second, iter - 1)
    next[(stone, iter)] = result
    return result


result = 0
for stone in stones:
    result += get_next(stone, 75)
print(result)
