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
        result = terms[0]
        for i, term in enumerate(terms[1:]):
            match perm[i]:
                case "0":
                    result += term
                case "1":
                    result *= term
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
        result = terms[0]
        for i, term in enumerate(terms[1:]):
            match perm[i]:
                case "0":
                    result += term
                case "1":
                    result *= term
                case "2":
                    result = int(str(result) + str(term))
        if result == solution:
            return True
    return False


with open("input") as f:
    result = 0
    result2 = 0
    for line in f.readlines():
        solution = int(line.split(":")[0])
        terms = list(map(int, line.split(":")[1].strip().split(" ")))
        # make every combination of 0|1 for list of len n
        # which is also just the digits of a binary number of len n?
        # sum(filter(lambda x: apply(x, result), terms))
        if apply_2(terms, solution):
            result += solution
        if apply_3(terms, solution):
            print(solution)
            result2 += solution
    print(result)
    print(result2)
