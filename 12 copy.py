from copy import deepcopy
from collections import defaultdict
with open('./12.in') as file:
    data = [line.strip() for line in file]
R = len(data[0])
C = len(data)
regions = defaultdict(list)
tested = set()

def findregion(r, c, v, thisregion):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    tested.add((r,c))
    for dir in dirs:
        r2 = r + dir[0]
        c2 = c + dir[1]
        if 0 <= r2 < R and 0 <= c2 < C:
            if data[r2][c2] == v and ((r2, c2)) not in thisregion:
                thisregion.append((r2,c2))
                findregion(r2, c2, v, thisregion)


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
        if ((r, c)) not in tested:
            thisregion = []
            thisregion.append((r,c))
            
            findregion(r, c, v, thisregion)
            regions[v].append(thisregion)
print(regions)

edges = defaultdict(list)
for region, locs in regions.items():

    for thisset in locs:
        t=0
        for loc in thisset:
            t +=(checkedges(loc[0], loc[1], region, 0))
        edges[region].append(t)

print(edges)

# part one
price = 0
for region in regions.keys():
    for i, area in enumerate(regions[region]):
        # print('region ', region, ' has an area of ', str(len(area)), ' and a perimeter of ', edges[region][i])
        price += edges[region][i] * len(regions[region][i])
print(price)

p2 = 0
for region in regions.keys():
    for i, area in enumerate(regions[region]):
        cc = countcorners(area)
        p2 += len(regions[region][i]) * cc
print(p2)