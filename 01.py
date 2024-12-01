with open('./01.in') as file:
    data = [line.strip() for line in file]

l, r = [], []
for row in data:
    splitrow = row.split('   ') # split the line and convert strings to integers
    l.append(int(splitrow[0]))
    r.append(int(splitrow[1]))

l = sorted(l) # python's handy in-place sort
r = sorted(r)

# part one 
t = 0
for i in range(len(l)):
    t += abs(l[i]-r[i]) # using the absolute means even a negative is a positive, so it doesn't matter which side we subtract.
print(t)

# part two
t2 = 0
for x in l:
    if x in r:
        t2 += x * r.count(x)
print(t2)