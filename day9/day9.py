with open("input") as f:
    line = map(int, f.readline().strip())

l = []
id = 0
free = False
for c in line:
    l.extend([id if not free else "."] * int(c))
    if not free:
        id += 1
    free = not free

# backfill
ln = len(l)
rn = range(ln)
print(ln - l.count("."))
for i in rn:
    if l[i] == ".":
        done = False
        # optimization: store last backfill idx to avoid long iters at the end
        for j in rn:
            if ln - j <= i:
                done = True
                break
            jr = j * -1 - 1
            if l[jr] != ".":
                if i % 1000 == 0:
                    print(i)

                l[i], l[jr] = l[jr], l[i]
                break
        if done:
            break
print(sum([i * c for i, c in enumerate(l) if type(c) == int]))
