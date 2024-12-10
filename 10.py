from copy import deepcopy
with open('./10.test') as file:
    d = [line.strip() for line in file]

data = []
for r in d:
    thisrow = []
    for c in r:
        thisrow.append(int(c))
    data.append(thisrow)

R = len(data[0])
C = len(data)
validpaths = []
dirs = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

def tracepath(r, c, height, score, found9s):
    for dir in dirs:
        rx = r + dir[0]
        cx = c + dir[1]
        if 0 <= rx < R and 0 <= cx < C:
            print(data[rx][cx])
            if data[rx][cx] == height + 1:
                if data[rx][cx] == 9:
                    if (rx, cx) not in found9s:
                        found9s.append((rx, cx))
                        return score + 1
                    else:
                        return score
                else:
                    score += tracepath(rx, cx, height + 1, 0, found9s)

    return score


for r ,row in enumerate(data):
    for c, col in enumerate(row):
        found9 = []
        if col == 0:
            validpaths.append(tracepath(r, c, col, 0, found9))
print(validpaths)
print(sum( x for x in validpaths))