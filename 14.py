from collections import defaultdict
with open('./14.in') as file:
    data = [line.strip() for line in file]
# p=0,4 v=3,-3
robots = []
W = 101 # width and height constants. 11, 7 for test, 101, 103 for input
H = 103
T = 100
for robot in data:
    px = int(robot[2:robot.find(',')])
    py = int(robot[robot.find(',')+1: robot.find(' ')])
    vx = int(robot[robot.find(' ')+3: robot.find(',', robot.find(' '))])
    vy = int(robot[robot.find(',', robot.find(' '))+1:])
    robots.append([(px, py), (vx, vy)])

# part 1
finalpositions = []
q1, q2, q3, q4 = 0, 0, 0, 0
for robot in robots:
    px1 = robot[0][0] + (robot[1][0] * T)
    py1 = robot[0][1] + (robot[1][1] * T)
    px1 = px1 % W
    py1 = py1 % H
    xmid = W // 2
    ymid = H // 2
    if px1 < xmid and py1 < ymid:
        q1 += 1
    elif px1 < xmid and py1 > ymid:
        q2 += 1
    elif px1 > xmid and py1 < ymid:
        q3 += 1
    elif px1 > xmid and py1 > ymid:
        q4 += 1
print(q1, q2, q3, q4)
print(q1 * q2 * q3 * q4)

# part 2

for t in range(500):
    positions = []
    for y in range(H+1):
        row = []
        for x in range(W+1):
            row.append('.')
        positions.append(row)
    for i, robot in enumerate(robots):
        px1 = robot[0][0] + robot[1][0]
        py1 = robot[0][1] + robot[1][1]
        if px1 >= W or px1 < 0:
            px1 = px1 % W
        if py1 >= H or py1 < 0:
            py1 = py1 % H
        #print(px1, py1)
        robots[i] = [(px1, py1), (robot[1][0], robot[1][1])]
        positions[py1][px1] = 'X'
    for i in positions:
        thisrow = ''
        for j in i:
            thisrow = thisrow + j
        with open ('./output.txt', 'a') as f:
            print(thisrow, file=f)
    with open('./output.txt', 'a') as f:
        print(t, file=f)
   #_ = input() 