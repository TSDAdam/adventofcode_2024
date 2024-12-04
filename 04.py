with open('./04.test') as file:
    data = [line.strip() for line in file]
word = 'XMAS'
total = 0

xs = [-1, 0, 1]
ys = [-1, 0, 1]


def checknext(xx, yy, xdir, ydir, currentstring, index, found):
    if index > len(word) - 1:
        found = True
    if found:
        return 1
    if xx + xdir >= 0 and xx + xdir < len(data[0]):
        if yy + ydir >= 0 and yy + ydir < len(data):
            if data[xx + xdir][yy + ydir] == word[index]:
                currentstring += data[xx + xdir][yy + ydir]
                t = checknext(xx + xdir, yy + ydir, xdir, ydir,
                              currentstring, index + 1, found)
                if t == 1:
                    return 1
    return 0


def checkletters(xx, yy, currstring, wordindex, t):
    for x1 in xs:
        if xx + x1 >= 0 and xx + x1 < len(data[0]):
            for y1 in ys:
                if yy + y1 >= 0 and yy + y1 < len(data):
                    t += checknext(xx, yy, x1, y1, currstring,
                                   wordindex, False)
    return t


def checkmas(x, y):
    validwords = ('SAM', 'MAS')
    words = []
    if 0 <= x <= len(data[0]) and 0 <= y <= len(data):
        for xx in -1, 1:
            words.append(data[x + xx][y-1] + 'A' + data[x + xx][y+1])
            words.append(data[x + xx][y+1] + 'A' + data[x + xx][y-1])
            print(words)
            if words[0] in validwords and words[1] in validwords:
                if words[2] == 'SAM' or words[3
    else:
        return 0


# Part 1
for x, row in enumerate(data):
    for y, c in enumerate(row):
        if c == word[0]:
            currentword = word[0]
            total += checkletters(x, y, currentword, 1, 0)

print(total)
t2 = 0
# Part 2
for x, row in enumerate(data):
    for y, c in enumerate(row):
        if c == 'A':
            print(x, y)
            t2 += checkmas(x, y)
