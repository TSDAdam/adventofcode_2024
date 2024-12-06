from copy import deepcopy
with open('./06.test') as file:
    data = [line.strip() for line in file]

R = len(data[0])
C = len(data)
dirs = [[0, -1], [+1, 0], [0, +1], [-1, 0]] # up, right, down, left - follows 90 deg turn order.
visited = []

obstacles = []
position = [0,0]
for y in range(R):
    for x in range(C):
        if data[y][x] == '^':
            startposition = [x,y]
        elif data[y][x] == '#':
            obstacles.append([x,y])
print(obstacles)
d = 0 # index for directions - 0=up, 1=right, 2=down, 3=left
nextpos = [0,0]
exited = False
position = startposition
while not exited:
    c = len(visited)
    nextpos[0] = deepcopy(position[0]) + dirs[d][0]
    nextpos[1] = deepcopy(position[1]) + dirs[d][1]
    if nextpos in obstacles:
        if position not in visited:
            visited.append(position)
        if d == 3:
            d = 0
        else:
            d += 1
    else:
        if position not in visited:
            visited.append(position)
        position = deepcopy(nextpos)
    if (nextpos[0] < 0 or nextpos[0] > R) or (nextpos[1] < 0 or nextpos[1] > C):
        exited = True
# part 1
print(len(visited) -1 )

# part 2
position = startposition
loopcount = 0
for loc in visited:
    visitedwithdir = []
    looped = False
    obstacles.append(loc)
    print(obstacles)
    while not looped:
        d = 0 # index for directions - 0=up, 1=right, 2=down, 3=left
        nextpos = [0,0]
        exited = False
        while not exited:
            nextpos[0] = deepcopy(position[0]) + dirs[d][0]
            nextpos[1] = deepcopy(position[1]) + dirs[d][1]
            if nextpos in obstacles: # if we're going to hit an obstacle, change direction
                visitstring = str(position) + str(d) # combine x,y and direction
                if visitstring not in visitedwithdir: # have we not been here before?
                    visitedwithdir.append(visitstring)
                else:
                    loopcount += 1
                    obstacles = obstacles[:-1]
                    looped = True
                if d == 3:
                    d = 0
                else:
                    d += 1
            else:
                visitstring = str(position) + str(d)
                if visitstring not in visitedwithdir:
                    visitedwithdir.append(visitstring)
                else:
                    loopcount += 1
                    obstacles = obstacles[:-1]
                    looped = True
                position = deepcopy(nextpos)
            if (nextpos[0] < 0 or nextpos[0] > R) or (nextpos[1] < 0 or nextpos[1] > C): # check to see whether left bounds
                exited = True
                looped = True
                obstacles = obstacles[:-1]

print(loopcount)