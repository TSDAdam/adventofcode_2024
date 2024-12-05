from collections import defaultdict
from copy import deepcopy
with open('./05.in') as file:
    data = [line.strip() for line in file]

splitpoint = 0
orders = []
instructions = []
# parse input
for i, row in enumerate(data):
    if row == '':
        splitpoint = i
        break
    orders.append([int(n) for n in row.split('|')])
for row in data[i+1:]:
    instructions.append([int(n) for n in row.split(',')])

before = defaultdict(list)
after = defaultdict(list)
validinstructions = []
invalidinstructions = []
t1 = 0

for order in orders:
    before[order[0]].append(order[1]) # for each value make a dictionary of values it's before...
    after[order[1]].append(order[0]) # ... and after.

# part 1
for instruction in instructions:
    valid = True
    for i, ins in enumerate(instruction[:-1]): # check to see if the current instruction value...
        for check in instruction[i+1:]:
            if check not in before[ins]: # ... appears in any of the later instructions 'before' dicitonary
                valid = False # if it does, this instruction is invalid.
    if valid:
        validinstructions.append(instruction)
    else:
        invalidinstructions.append(instruction)
print(validinstructions)
for v in validinstructions:
    t1 += v[int(len(v)/2)]
print(t1)

# part 2
fixedinstructions =[]
for x, invalidinstruction in enumerate(invalidinstructions):
    print(invalidinstruction)
    sorted = False
    while not sorted:
            i = 0
            while i < len(invalidinstruction)-1: # lazy bubble sorting?
                if invalidinstruction[i+1] in after[invalidinstruction[i]]:
                    temp = invalidinstruction[i+1]
                    invalidinstruction[i+1] = invalidinstruction[i]
                    invalidinstruction[i] = temp
                    i = 0
                else:
                    i += 1
            sorted = True
    fixedinstructions.append(invalidinstruction)

t2 = 0
for v in fixedinstructions:
    t2 += v[int(len(v)/2)]
print(t2)