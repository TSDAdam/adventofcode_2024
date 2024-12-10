input = []
with open("./09.in", "r") as f:
    for line in f:
        if len(line.strip()) > 0:
            input = [int(c) for c in line.strip()]

# prep for part 2, before I destroy it with my part 1 implementation
in_p2 = []
block = 0
empty = False
for b in input:
    if empty:
        in_p2.append([-1, b])
        empty = False
    else:
        in_p2.append([block, b])
        block += 1
        empty = True
# end of prep for part 2

last_block = len(input)//2
current_block = 0
index = 0
empty = False
total = 0

while(len(input)) > 0:
    if empty:
        if(input[0] >= input[-1]):
            total += (input[-1] * (2 * index + input[-1] - 1) // 2) * last_block
            index += input[-1]
            input[0] -= input[-1]
            last_block -= 1
            input.pop()
            input.pop()
        else:
            total += (input[0] * (2 * index + input[0] - 1) // 2) * last_block
            index += input[0]
            input[-1] -= input[0]
            input.pop(0)
            empty = False
            current_block += 1
    else:
        total += (input[0] * (2 * index + input[0] - 1) // 2) * current_block
        index += input[0]
        input.pop(0)
        empty = True

print(total)

i = len(in_p2) - 1
while i > 0:
    if in_p2[i][0] >= 0:
        for j in range(i):
            if in_p2[j][0] == -1 and in_p2[j][1] >= in_p2[i][1]:
                t = in_p2.pop(i)
                in_p2.insert(i, [-1, t[1]])
                in_p2.insert(j, t)
                in_p2[j+1][1] -= t[1]
                i += 2
                break
    i -= 1

sum = 0
index = 0
for t in in_p2:
    if t[0] > 0:
        sum += (t[1] * (2 * index + t[1] - 1) // 2) * t[0]
    index += t[1]

print(sum)