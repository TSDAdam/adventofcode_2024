from copy import deepcopy
from collections import defaultdict
with open('./08.in') as file:
    data = [line.strip() for line in file]

R = len(data[0])
C = len(data)
antenodes = set()
p2antenodes = set()
antennatypes = defaultdict(list)
for y, row in enumerate(data): # parse input
    for x, c in enumerate(row):
        if c != '.':
            antennatypes[c].append((int(y), int(x))) 

for k, v in antennatypes.items():
    print(k)
    for i, loc in enumerate(v):
        p2antenodes.add((loc[0], loc[1])) # Current locations count too, Adam!
        for l in range(i+1, len(v)):
            diffy = abs(loc[0] - v[l][0])
            diffx = abs(loc[1] - v[l][1])
            if loc[0] < v[l][0]: # if this node is smaller Y
                y1 = loc[0] - diffy # make the antenode have minus the difference
                y2 = v[l][0] + diffy # and the opposite have positive
                stepy1 = -diffy
                stepy2 = +diffy
            elif loc[0] > v[l][0]: # as above, but the opposite way around
                y1 = loc[0] + diffy
                y2 = v[l][0] - diffy
                stepy1 = +diffy
                stepy2 = -diffy
            else:
                y1 = loc[0]
                y2 = loc[0]
                stepy1 = 0
                stepy2 = 0
            if loc[1] < v[l][1]:
                x1 = loc[1] - diffx # same as the Y co-ords, but X
                x2 = v[l][1] + diffx
                stepx1 = -diffx
                stepx2 = +diffx
            elif loc[1] > v[l][1]:
                x1 = loc[1] +diffx
                x2 = v[l][1] - diffx
                stepx1 = +diffx
                stepx2 = -diffx
            else:
                x1 = loc[1]
                x2 = loc[1]
                stepx1 = 0
                stepx2 = 0

            if 0 <= y1 < R and 0 <= x1 < C: # if antenode isn't OOB
                antenodes.add((y1, x1))
                while 0 <= y1 < R and 0 <= x1 < C:
                    p2antenodes.add((y1, x1))
                    y1 += stepy1
                    x1 += stepx1
            if 0 <= y2 < R and 0 <= x2 < C:
                antenodes.add((y2, x2))
                while 0 <= y2 < R and 0 <= x2 < C:
                    p2antenodes.add((y2, x2))
                    y2 += stepy2
                    x2 += stepx2
# part one
print(len(antenodes))
# part two
print(len(p2antenodes))
