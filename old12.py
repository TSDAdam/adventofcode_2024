from copy import deepcopy
from collections import defaultdict
with open('./12.test2') as file:
    data = [line.strip() for line in file]
R = len(data[0])
C = len(data)
regions = defaultdict(list)
tested = set()

def findregion(r, c, v):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    for dir in dirs:
        r2 = r + dir[0]
        c2 = c + dir[1]
        if 0 <= r2 < R and 0 <= c2 < C:
            tested.add((r2, c2))
            if data[r2][c2] == v and ((r2, c2)) not in regions[v]:
                regions[v].append((r2,c2))
                findregion(r2, c2, v)

def checkedges(r, c, v, t):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    for dir in dirs:
        r2 = r + dir[0]
        c2 = c + dir[1]
        if (r2 >= R or r2 < 0) or (c2 >= C or c2 < 0):
            t += 1
        elif data[r2][c2] != v:
            t += 1
        else:
            continue
    return t

def countcorners(region):
    left = set()
    right = set()
    up = set()
    down = set()
    for (r, c) in region:
        if (r-1, c) not in region:
            up.add((r, c))
        if (r+1, c) not in region:
            down.add((r, c))
        if (r, c+1) not in region:
            right.add((r, c))
        if (r, c-1) not in region:
            left.add((r, c))
        # print(up, down, left, right)
    corners = 0
    for (r, c) in up:
        if (r, c) in left:
            corners += 1
        if (r, c) in right:
            corners += 1
        if (r, c) in right and (r, c) not in left:
            corners += 1
        if (r, c) in left and (r, c) not in right:
            corners += 1

    for (r, c) in down:
        if (r, c) in left:
            corners += 1
        if (r, c) in right:
            corners += 1
        if (r, c) in right and (r, c) not in left:
            corners += 1
        if (r, c) in left and (r, c) not in right:
            corners += 1
    return corners


for r, row in enumerate(data):
    for c, v in enumerate(row):
        if ((r, c)) not in regions[v]:
            regions[v].append((r,c))
            findregion(r, c, v)
print(regions)

edges = defaultdict(int)
for region, locs in regions.items():
    for loc in locs:
        edges[region] += checkedges(loc[0], loc[1], region, 0)


# part one
price = 0
for region in regions.keys():
    print('region ', region, ' has an area of ', str(len(regions[region])), ' and a perimeter of ', edges[region])
    price += edges[region] * len(regions[region])
print(price)

# part two
p2 = 0
for region, locs in regions.items():
    cc = countcorners((locs))
    print(region, cc)
    p2 += len(regions[region]) * cc
print(p2)