from copy import deepcopy
with open('./06.test') as file:
    data = [line.strip() for line in file]

R = len(data[0])
C = len(data)
dirs = [(0, -1), (+1, 0), (0, +1), (-1, 0)] # up, right, down, left - follows 90 deg turn order.
visited = set()

obstacles = set()
position = (0,0)
for y in range(R):
    for x in range(C):
        if data[y][x] == '^':
            startposition = (x,y)
        elif data[y][x] == '#':
            obstacles.add((x,y))
print(obstacles)
d = 0 # index for directions - 0=up, 1=right, 2=down, 3=left
nextpos = (0,0)
exited = False
position = startposition
while not exited:
    c = len(visited)
    nextpos = ((position[0] + dirs[d][0]), (position[1] + dirs[d][1]))
    if nextpos in obstacles:
        if position not in visited:
            visited.add(position)
        if d == 3:
            d = 0
        else:
            d += 1
    else:
        if position not in visited:
            visited.add(position)
        position = nextpos
    if (nextpos[0] < 0 or nextpos[0] > R) or (nextpos[1] < 0 or nextpos[1] > C):
        exited = True
# part 1
print(len(visited) -1 )

# part 2

loopcount = 0
for i, loc in enumerate(visited):
    print('testing ',i, ' of ', len(visited))
    position = startposition
    visitedwithdir = set()
    looped = False
    obstacles.add(loc)
    d = 0 # index for directions - 0=up, 1=right, 2=down, 3=left
    nextpos = [0,0]
    exited = False

    while not exited and not looped:
        nextpos = ((position[0] + dirs[d][0]), (position[1] + dirs[d][1]))
        if nextpos in obstacles: # if we're going to hit an obstacle, change direction
            visitstring = (position[0], position[1], d) # combine x,y and direction
            if visitstring not in visitedwithdir: # have we not been here before?
                visitedwithdir.add(visitstring)
            else:
                loopcount += 1
                obstacles.remove(loc)
                looped = True
            if d == 3:
                d = 0
            else:
                d += 1
        else:
            visitstring = (position[0], position[1], d)
            if visitstring not in visitedwithdir:
                visitedwithdir.add(visitstring)
            else:
                loopcount += 1
                obstacles.remove(loc)
                looped = True
            position = nextpos
        if (nextpos[0] < 0 or nextpos[0] > R) or (nextpos[1] < 0 or nextpos[1] > C): # check to see whether left bounds
            exited = True
            obstacles.remove(loc)

print(loopcount)