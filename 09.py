from copy import deepcopy
with open('./09.test') as file:
    data = [line.strip() for line in file]
data = data[0]

files = [] # (id, length)
files2 = []
gaps = []
id = 0
i = 0
while i < len(data):
    if i % 2 == 0: # even == file
        files.append((id, int(data[i]))) # add a file with id and its number of blocks
        files2.append((id, int(data[i])))
        id += 1 # increment the id
    else:
        gaps.append(int(data[i]))
        files2.append(('.', int(data[i])))
    i += 1

print(files, gaps)

# part one
expanded = []

totalgaps = 0
for g in gaps:
    totalgaps += g
for i, f in enumerate(files):
    for x in range(f[1]):
        expanded.append(f[0])
    if i < len(gaps):
        for y in range(gaps[i]):
            expanded.append('.')
p2expanded = deepcopy(expanded)
moved = 0

while '.' in expanded:
    expanded[expanded.index('.')] = expanded.pop(-1)
    
for _ in range(totalgaps + 1):
    expanded.append('.')
t1 = 0
for i in range(expanded.index('.')):
    t1 += (expanded[i] * i)
print(t1)

print(files2)

# part two
couldmove = True
stuckcounter = 0
'''while couldmove:
    for i, f in enumerate(files[::-1]): # (id, length)
        for j, gap in enumerate(gaps):
            filledagap = False
            if f[1] <= gap:
                gaps[j] = gap - f[1]
                for k, g in enumerate(files2):
                    if g[0] == '.' and g[1] == gap:
                        files2[k] = ('.', g[1] - f[1])
                        break
                sortedfiles = []
                sortedfiles2 = []
                a = files[:k]
                b = [files.pop(-(1 + stuckcounter))]
                c = files[j+1:] 
                a2 = files2[:k]
                b2 = [files.pop(-(1 + stuckcounter))]
                c2 = files2[k+1:] 
                i += 1
                sortedfiles = a + b + c
                sortedfiles2 = a2 + b2 + c2
                files = sortedfiles
                files2 = sortedfiles2
                filledagap = True
                break
        if not filledagap:
            stuckcounter += 1'''
cantmove = []

def reducegaps(thesefiles):
    reduced = False
    for z in range(len(thesefiles)):
        if thesefiles[z][0] == '.' and z < len(thesefiles)-1:
            if thesefiles[z+1][0] == '.':
                thesefiles[z] = ('.', thesefiles[z][1] + thesefiles[z+1][1])
                thesefiles[z+1] = ('.', 0)
    for i, f in enumerate(thesefiles):
        if f[0] == '.' and f[1] == 0:
           del thesefiles[i]
           reduced = True
    return(thesefiles, reduced)

while couldmove:
    changes = 0
    for i, f in enumerate(files2[::-1]):
        newfiles2 = []
        moved = False
        if f not in cantmove:
            if str(f[0]).isdigit():
                for j, g in enumerate(files2):
                    if g[0] == '.' and g[1] >= f[1]: # found a gap and it's at least as big as the file
                        files2[j] = ('.', g[1] - f[1])
                        newfiles2 = files2[:j] # first part of files is unchanged
                        newfiles2.append(files2.pop(files2.index(f)))
                        for x in files2[j:]:
                            newfiles2.append(x)
                        newfiles2.insert(len(files2)-i, ('.',f[1]))
                        moved = True
                        reduction = True
                        while reduction:
                            newfiles, reduction = reducegaps(newfiles2)
                        
                        files2 = deepcopy(newfiles2)
                        changes += 1
                        break
                if not moved:
                    cantmove.append(f)
            else:
                continue
    if changes == 0:
        couldmove = False
print(files2)
