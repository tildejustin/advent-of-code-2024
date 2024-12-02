def is_safe(report):
    pos = report[1] > report[0]
    last = report[0]
    for num in report[1:]:
        if pos:
            if num < last:
                return False
        else:
            if num > last:
                return False
        if num == last:
            return False
        if abs(num - last) > 3:
            return False
        last = num
    return True


# part 1

with open("input") as f:
    sum = 0
    for line in f.readlines():
        if is_safe(line):
            sum += 1
    print(sum)

# part 2
with open("input") as f:
    sum = 0
    for line in f.readlines():
        report = [int(num) for num in line.split()]
        if is_safe(report):
            sum += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1:]):
                    sum += 1
                    break
            
    print(sum)

