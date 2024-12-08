from functools import reduce

ternary_cache = {}

def to_ternary(num) -> str:
    if num == 0:
        return "0"
    result = ""
    while num >= 3:
        result = str(num % 3) + result
        num = num // 3
    return str(num) + result

def apply_2(terms, solution) -> bool:
    length = len(terms) - 1
    perms = 2 ** length
    # reduce to a reduce
    for i in range(perms):
        perm = bin(i)[2:].zfill(length)
        result = int(terms[0])
        for i, term in enumerate(terms[1:]):
            match perm[i]:
                case "0":
                    result += int(term)
                case "1":
                    result *= int(term)
        if result == solution:
            return True
    return False

def apply_3(terms, solution) -> bool:
    length = len(terms) - 1
    perms = 3 ** length
    # reduce to a reduce
    for i in range(perms):
        perm = ternary_cache.get(i)
        if perm is None:
            perm = to_ternary(i)
            ternary_cache[i] = perm
        perm = perm.zfill(length)
        result = int(terms[0])
        for i, term in enumerate(terms[1:]):
            match perm[i]:
                case "0":
                    result += int(term)
                case "1":
                    result *= int(term)
                case "2":
                    result = int(str(result) + term)
        if result == solution:
            return True
    return False


with open("input") as f:
    result2 = 0
    print(sum(map(lambda x: x[0], filter(lambda x: apply_2(x[1], x[0]), [(int(line.split(":")[0]), line.split(":")[1].strip().split(" ")) for line in f.readlines()]))))
    f.seek(0)
    for line in f.readlines():
        solution = int(line.split(":")[0])
        terms = line.split(":")[1].strip().split(" ")
        # make every combination of 0|1 for list of len n
        # which is also just the digits of a binary number of len n?
        if apply_3(terms, solution):
            result2 += solution
    print(result2)
