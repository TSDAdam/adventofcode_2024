with open('./07.in') as file:
    data = [line.strip() for line in file]

totals = []
digits = []

for row in data: # parse input
    t, ds = row.split(':')
    totals.append(int(t))
    thesedigits = []
    for d in ds.split():
        thesedigits.append(int(d))
    digits.append(thesedigits)

def checkrow(total, nums, p2 = False): # p2 flag whether to include || or not
    operators = ['+', '*']
    if p2:
        operators.append('||')
    results = [nums[0]] # start with the first number...
    for i, num in enumerate(nums[1:]): # ...then work through the rest
        new_results = [] # create a new list to collect the results
        for result in results:
            for op in operators:
                new_result = result
                if op == '+':
                    new_result += num
                if op == '*':
                    new_result *= num
                if op == '||':
                    new_result = int(str(new_result) + str(num))
                if new_result <= total: # no point in keeping it if it's already too big
                    new_results.append(new_result)
                if new_result == total and i == len(nums) - 2: # if this result matches, and we're at the last number
                    return(True)
        results = new_results # important! copy the new results over the old ones. otherwise infinity!
    return False            
# part one
t1 = 0
for i, t in enumerate(totals):
    if checkrow(t, digits[i]):
        t1 += t
print(t1)

# part two
t2 = 0
for i, t in enumerate(totals):
    if checkrow(t, digits[i], True):
        t2 += t
print(t2)