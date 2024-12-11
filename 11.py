from copy import deepcopy
from collections import Counter, defaultdict
with open('./11.in') as file:
    data = [line.strip() for line in file]

stones = map(int, (x for x in data[0].split(' ')))

def split(c1):
    r = defaultdict(int)
    for stonetype, count in c1.items():
        if stonetype == 0:
            r[1] += c1[0]
        elif len(str(stonetype)) % 2 == 0:
            s = str(stonetype)
            s1 = int(s[:len(s) // 2])
            s2 = int(s[len(s) // 2:])
            r[s1] += c1[stonetype]
            r[s2] += c1[stonetype]
        else:
            r[stonetype * 2024] += c1[stonetype]
    return r

c = Counter(stones)
for i in range(75):
    c = split(c)
print(sum(c.values()))