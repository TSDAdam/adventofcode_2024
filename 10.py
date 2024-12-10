from copy import deepcopy
with open('./10.in') as file:
    d = [line.strip() for line in file]

data = []
for r in d:
    thisrow = []
    for c in r:
        thisrow.append(int(c))
    data.append(thisrow)

R = len(data[0])
C = len(data)
trails = 0
validpaths = []
dirs = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

def tracepath(r, c, height, score, found9s):
    global trails
    for dir in dirs:
        rx = r + dir[0]
        cx = c + dir[1]
        if 0 <= rx < R and 0 <= cx < C:
            if data[rx][cx] == height + 1:
                if data[rx][cx] == 9:
                    if (rx, cx) not in found9s:
                        found9s.append((rx, cx))
                        trails = trails + 1
                        score += 1
                    else:
                        trails = trails + 1
                else:
                    score += tracepath(rx, cx, height + 1, 0, found9s)

    return score


for r ,row in enumerate(data):
    for c, col in enumerate(row):
        found9 = []
        if col == 0:
            validpaths.append(tracepath(r, c, col, 0, found9)) # row, col, value, 0 score, empty list
print(sum( x for x in validpaths))
print(trails)