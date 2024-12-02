with open("input") as f:
    a = []
    b = []
    for l in f.readlines():
        c = l.split()
        a.append(int(c[0]))
        b.append(int(c[1]))

a.sort()
b.sort()
sum = 0
for d in zip(a, b):
    sum += abs(d[0] - d[1])
print(sum)

# part 2
with open("input") as f:
    # set shouldn't work but there are no duplicates in the left list
    a = set()
    b = []
    for l in f.readlines():
        c = l.split()
        a.add(int(c[0]))
        b.append(int(c[1]))

sum = 0
for d in a:
    sum += d * b.count(d)
print(sum)
