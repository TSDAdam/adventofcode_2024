from copy import deepcopy
from collections import defaultdict
with open('./12.test') as file:
    data = [line.strip() for line in file]
R = len(data[0])
C = len(data)
regions = defaultdict(list)

def findregion(r, c, v):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    for dir in dirs:
        r2 = r + dir[0]
        c2 = c + dir[1]
        if 0 <= r2 < R and 0 <= c2 < C:
            if data[r2][c2] == v and ((r2, c2)) not in regions[v]:
                regions[v].append((r2,c2))
                findregion(r2, c2, v)
        else:
            break

for r, row in enumerate(data):
    for c, v in enumerate(row):
        if c not in regions:
            regions[v].append((r,c))
            findregion(r, c, v)
print(regions)