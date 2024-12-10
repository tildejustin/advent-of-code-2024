# this is the much cooler version and 4x as fast but unfortunately i could not get blank spaces to merge correctly

from functools import reduce

with open("sample") as f:
    line = map(int, f.readline().strip())

l = []
id = 0
free = False
for c in line:
    if c == "." or int(c) != 0:
        l.append((id if not free else ".", c))
    if not free:
        id += 1
    free = not free

print(l)
ln = len(l)
rn = range(ln)
done = False
for i in rn:
    if i * -1 <= -len(l):
        break
    f = l[i * -1 - 1]
    if f[0] == ".":
        continue
    print("moving", f)
    for j in range(len(l)):
        if j >= len(l) - i - 1:
            # done = True
            break
        # print(i * -1 - 1, j)
        # if j >= len(l) - 1:
        #     done = True
        #     break
        s = l[j]
        if s[0] != "." or s[1] < f[1]:
            continue
        print("chosen", j, s)
        l[j], l[i * -1 - 1] = l[i * -1 - 1], (".", f[1])
        print(l)

        # check left and right of popped to see if can be combined
        # print(i * -1 - 1, l[i * -1 - 2], l[i * -1 - 1])
        if l[i * -1 - 2][0] == "." and l[i * -1 - 1][0] == ".":
            l[i * -1 - 2] = (".", l[i * -1 - 2][1] + l[i * -1 - 1][1])
            l.pop(i * -1 - 1)
            i -= 1
            print(l)

        if l[i * -1 - 2][0] == "." and l[i * -1 - 1][0] == ".":
            l[i * -1 - 2] = (".", l[i * -1 - 2][1] + l[i * -1 - 1][1])
            l.pop(i * -1 - 1)
            print(l)

        # if not fully replacing the empty space, add the remaining space to the left, combining when necessary
        if s[1] != f[1]:
            if l[j + 1][0] == ".":
                l[j + 1] = (".", s[1] - f[1])
            else:
                l.insert(j + 1, (".", s[1] - f[1]))
            print(l)
        input()
        break
    if done:
        break

print(l)
# expand
s = reduce(lambda x, y: x + y, ["".join([str(i)] * ln) for i, ln in l])
# print(s)


print(sum([i * int(c) for i, c in enumerate(s) if c != "."]))
