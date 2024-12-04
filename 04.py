with open('./04.in') as file:
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


# Part 1
for x, row in enumerate(data):
    for y, c in enumerate(row):
        if c == word[0]:
            currentword = word[0]
            total += checkletters(x, y, currentword, 1, 0)

print(total)

# Part 2
