from copy import deepcopy
with open('./13.in') as file:
    data = [line.strip() for line in file]

M = []
A = ()
B = ()
C = ()
for line in data: # parse input
    if line == '':
        continue
    if line[7] == 'A':
        ax = int(line[line.find('X+')+2: line.find(',')])
        ay = int(line[line.find('Y+')+2:])
        A = (ax, ay)
    elif line[7] == 'B':
        bx = int(line[line.find('X+')+2: line.find(',')])
        by = int(line[line.find('Y+')+2:])
        B = (bx, by)
    elif line[0] == 'P':
        cx = int(line[line.find('X=')+2: line.find(',')])
        cy = int(line[line.find('Y=')+2:])
        C = (cx, cy)
        M.append([A, B, C])
    else:
        continue

def counttokens(wins):
    t = 0
    for a, b in wins:
        t += a * 3 + b * 1
    print(t)

def checkforprizes(machines, parttwo=False): # part two adds a huge number to the prize locations
    winprize = []
    added = 0
    if parttwo:
        added = 10000000000000
    for machine in machines:
        a1 = machine[0][0]
        a2 = machine[0][1]
        b1 = machine[1][0]
        b2 = machine[1][1]
        c1 = machine[2][0] + added
        c2 = machine[2][1] + added
        A = (b2 * c1 - b1 * c2) / (b2 * a1 - b1 * a2) # totally 'borrowed' a linear algebra equation
        B = (c1 - a1 * A) / b1
        if A == int(A) and B == int(B): # has to be an exact match
            winprize.append((int(A), int(B)))
    counttokens(winprize)

p1 = checkforprizes(M)
p2 = checkforprizes(M, True)