import re
import functools

# part 1
with open("input") as f:
    print(functools.reduce(lambda x, y: x + y, map(lambda x: int(x[0]) * int(x[1]), re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", f.read()))))

# part 2
with open("input") as f:
    fs = f.read()
    # fs = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    s = ""
    while (True):
        end = fs.find("don't()")
        if (end == -1):
            s += fs
            break
        s += fs[0:end]
        start = fs[end + len("don't()"):].find("do()") + len("don't()") + end
        if (start == -1):
            break
        fs = fs[start + len("do()"):]
    print(functools.reduce(lambda x, y: x + y, map(lambda x: int(x[0]) * int(x[1]), re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", s))))
