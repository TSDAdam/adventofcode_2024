from copy import deepcopy
with open('./11.in') as file:
    data = [line.strip() for line in file]

def split(stones):
    newstones = []
    for stone in stones:
        if stone == '0':
            newstones.append('1')
        elif int(len(stone)) % 2 == 0:
            mid = int(len(stone) / 2)
            l = stone[:mid]
            r = stone[mid:]
            l = int(l)
            r = int(r)
            newstones.append(str(l))
            newstones.append(str(r))
        else:
            newstones.append(str(int(stone) * 2024))
    return newstones
stones = data[0].split(' ')

t2 = 0
for stone in stones:
    if stone == '0':
        pass
    elif stone =='1':
        pass
    else:
        t += 2^

for i in range(75):
    stones = split(stones)
   #print(stones)
print(len(stones))
