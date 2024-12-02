from copy import deepcopy
with open('./02.in') as file:
    data = [line.strip() for line in file]


def checkLevel(level):
    safe = True
    if all(level[i] < level[i+1] for i in range(len(level)-1)) or all(level[i] > level[i+1] for i in range(len(level)-1)):
        for x in range(len(level)-1):
            if not abs(level[x] - level[x+1]) < 4:
                safe = False
    else:
        safe = False
    return safe

levels = []
for row in data:
    thislevel = []
    for num in row.split():
        thislevel.append(int(num))
    levels.append(thislevel)

t1, t2  = 0, 0
 # Part 1
for level in levels:
    if checkLevel(level):
        t1 += 1
print(t1)

# Part 2
for level in levels:
    if checkLevel(level):
        t2 += 1
    else:
        nowsafe = False
        for n in range(len(level)):
            templevel = deepcopy(level)
            del templevel[n]
            if checkLevel(templevel):
                nowsafe = True
        if nowsafe:
            t2 += 1            

print(t2)
