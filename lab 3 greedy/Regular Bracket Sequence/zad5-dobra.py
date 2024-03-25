line = input()

counterP = 0
counter_D = 0
for c in line:
    if c == '(':
        counterP += 1
    elif counterP == 0:
        counter_D += 1
    else:
        counterP -= 1
print(len(line) - counter_D - counterP)
