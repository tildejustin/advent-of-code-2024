with open("input") as f:
    lines = list(map(str.strip, f.readlines()))

rules: dict[int, dict[int, bool]] = {}
for rule in lines:
    if "|" in rule:
        nums = rule.split("|")
        first = int(nums[0])
        second = int(nums[1])
        # true -> after
        rules.setdefault(first, dict())[second] = True
        rules.setdefault(second, dict())[first] = False

sum = 0
for line in lines:
    if "," in line:
        dataset = list(map(int, line.split(",")))
        # print(set)
        fail = False
        for i, num in enumerate(dataset):
            num_rules = rules.get(num)
            # print(num, num_rules)
            if num_rules is None:
                continue
            for j, num2 in enumerate(dataset):
                rule = num_rules.get(num2)
                if rule is None:
                    continue
                # print(num, num2, rule, j > i, rule ^ (j > i))
                assert i != j
                if (j > i) ^ rule:
                    fail = True
                    break
            if fail:
                break
        if not fail:
            assert (len(dataset) - 1) % 2 == 0
            sum += dataset[(len(dataset) - 1) // 2]

print(sum)


# part 2

# for each wrong value, i need to know if the values making it wrong are all the same, in other words if they could all be satisfied by moving the value in a single direction
# for each interation, i should take the leftmost value that is able to be moved in a single direction, and move it in such until satisfied,
# and then recheck the invalid values and what makes them invalid

def checkvalid(dataset):
    # idx to movement allowed by invalidating nums
    incorrect: dict[int, int] = {}
    for i, num in enumerate(dataset):
        num_rules = rules.get(num)
        if num_rules is None:
            continue
        # print(num, num_rules)
        for j, num2 in enumerate(dataset):
            rule = num_rules.get(num2)
            if rule is None:
                continue
            # print(num, num2, rule, j > i, rule ^ (j > i))
            assert i != j
            if (j > i) ^ rule:
                if incorrect.get(i) is None:
                    incorrect[i] = 0
                # 01 to go left, 10 to go right
                incorrect[i] |= 0b10 if i < j else 0b01
    return incorrect

def s_i(i):
    a = list(i.items())
    a.sort(key=lambda j: min(j[0], len(i) - 1 - j[0]))
    return a

sum = 0
for line in lines:
    if "," in line:
        dataset = list(map(int, line.split(",")))
        incorrect = checkvalid(dataset)
        if len(incorrect) == 0:
            continue
        # print(dataset, incorrect)
        while (incorrect := checkvalid(dataset)):
            # print(dataset, incorrect)
            for x, y in s_i(incorrect):
                if y == 0b11 or y == 0:
                    continue
                elif y == 0b01:
                    while True:
                        # print(x, dataset, incorrect)
                        dataset.insert(x - 1, dataset.pop(x))
                        x -= 1
                        if x not in (incorrect := checkvalid(dataset)).keys() or x == 1:
                            break
                    break
                elif y == 0b10:
                    while True:
                        # print(x, dataset, incorrect)
                        dataset.insert(x + 1, dataset.pop(x))
                        x += 1
                        if x not in (incorrect := checkvalid(dataset)).keys() or x == len(dataset) - 1:
                            break
                    break
        # print(dataset)  
        assert (len(dataset) - 1) % 2 == 0
        sum += dataset[(len(dataset) - 1) // 2]

print(sum)
