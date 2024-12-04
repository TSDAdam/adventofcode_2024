with open('./04.test') as file:
    data = [line.strip() for line in file]
word = 'XMAS'
total = 0

xs = [-1, 0, 1]
ys = [-1, 0, 1]


def checkletters(xx, yy, currstring, wordindex, t):
    if currstring == word:
        return 1
    for x1 in xs:
        if xx + x1 < 0 or xx + x1 > len(data[0])-1:
            continue
        for y1 in ys:
            if yy + y1 < 0 or yy + y1 > len(data)-1:
                continue
            if data[xx + x][yy + y] == word[wordindex]:
                currstring += data[xx + x1][yy + y1]
                t += checkletters(xx + x1, yy + y1,
                                  currstring, wordindex + 1, t)
            else:
                continue
    return 0


for x, row in enumerate(data):
    for y, c in enumerate(row):
        if c == word[0]:
            currentword = word[0]
            total += checkletters(x, y, currentword, 1, 0)

print(total)
