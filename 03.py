import re
with open('./03.in') as file:
    data = [line.strip() for line in file]

t = 0
validInstructions = ''
calculations = []

for row in data:
    for c in row:
        validInstructions += c

def testInstruction(instruction):
    regexpattern = re.compile(r"mul\([0-9]+,[0-9]+\)", re.IGNORECASE)
    if regexpattern.match(instruction):
        calculations.append(instruction)
    return len(instruction) - 1

while len(validInstructions) > 0:
    if validInstructions[0:4] != 'mul(': # if the next 4 chars aren't 'mul('...
        validInstructions = validInstructions[1:] # ...take the first char off the string and try again
    else:
        if (validInstructions.find('(', 4) < validInstructions.find(')')) and validInstructions.find('(',4) > 0: # if it finds another ( before ) then the instruction is invalid
            validInstructions = validInstructions[1:]
        else:    
            thisInstruction = validInstructions[0:validInstructions.find(')') + 1]
            validInstructions = validInstructions[testInstruction(thisInstruction):]

# part one
for calc in calculations:
    x = int(calc[calc.find('(')+1:calc.find(',')])
    y = int(calc[calc.find(',')+1:calc.find(')')])
    t += x * y
print(t)
print(len(calculations))

# part two - I really should refactor this to save doing it all twice, but...

calculations = []
t = 0
validInstructions = ''
for row in data:
    for c in row:
        validInstructions += c

process = True
while len(validInstructions) > 0:
    if validInstructions[0:7] == "don't()":
        process = False
    elif validInstructions[0:4] == "do()":
        process = True
    if validInstructions[0:4] != 'mul(': # if the next 4 chars aren't 'mul('...
        validInstructions = validInstructions[1:] # ...take the first char off the string and try again
    else:
        if (validInstructions.find('(', 4) < validInstructions.find(')')) and validInstructions.find('(',4) > 0: # if it finds another ( before ) then the instruction is invalid
            validInstructions = validInstructions[1:]
        else:
            if process:   # same as before, but only process if the flag is true
                thisInstruction = validInstructions[0:validInstructions.find(')') + 1]
                validInstructions = validInstructions[testInstruction(thisInstruction):]
            else:   # else chop off the lead char and carry on.
                validInstructions = validInstructions[1:]

for calc in calculations:
    x = int(calc[calc.find('(')+1:calc.find(',')])
    y = int(calc[calc.find(',')+1:calc.find(')')])
    t += x * y
print(t)
print(len(calculations))