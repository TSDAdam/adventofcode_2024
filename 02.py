from copy import deepcopy
with open('./02.in') as file:
    data = [line.strip() for line in file]

# Function to check a given level
def checkLevel(level):
    safe = True
    if all(level[i] < level[i+1] for i in range(len(level)-1)) or all(level[i] > level[i+1] for i in range(len(level)-1)): # do they all ascend or descend?
        for x in range(len(level)-1):
            if not abs(level[x] - level[x+1]) < 4: # make sure no gap is bigger than 3
                safe = False
    else:
        safe = False
    return safe

levels = []
for row in data: # parse the data and make lists of integers
    thislevel = []
    for num in row.split():
        thislevel.append(int(num))
    levels.append(thislevel)

t1, t2  = 0, 0
 # Part 1
for level in levels: # for part one just check the levels as they are
    if checkLevel(level):
        t1 += 1
print(t1)

# Part 2
for level in levels:
    if checkLevel(level): # for part two, first check all levels again
        t2 += 1
    else: # but where one fails...
        nowsafe = False
        for n in range(len(level)): 
            templevel = deepcopy(level) # ...copy the original level...
            del templevel[n] # ...remove the current entry from the level...
            if checkLevel(templevel): # ...and see if it works now.
                nowsafe = True
        if nowsafe:
            t2 += 1            

print(t2)
