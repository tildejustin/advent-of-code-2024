with open("input") as f:
    line = map(int, f.readline().strip())

l = []
currid = 0
free = False
for c in line:
    l.extend([currid if not free else "."] * int(c))
    if free:
        currid += 1
    free = not free

for id in range(currid, -1, -1):
    starti = l.index(id)
    endi = len(l) - l[::-1].index(id)
    targetlen = endi - starti
    currlen = 0
    for i, c in enumerate(l):
        if i >= starti:
            break
        if c == ".":
            currlen += 1
        else:
            currlen = 0
        if currlen != targetlen:
            continue
        for j in range(starti, endi):
            l[j] = "."
        for j in range(i - targetlen + 1, i + 1):
            l[j] = id
        break

print(sum([i * c for i, c in enumerate(l) if type(c) == int]))
