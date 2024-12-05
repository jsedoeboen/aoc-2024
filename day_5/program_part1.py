# file =  open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

rules = []
pages = []
switchMode = False
for line in lines:
    line = line.strip()
    if line == "":
        switchMode = True
        continue
    if not switchMode:
        rules.append(tuple(int(i) for i in line.split("|")))
    else:
        pages.append([int(y) for y in line.split(',')])

print(rules)
print(pages)

sum = 0
for update in pages:
    notInOrder = False

    for p1, p2 in rules:
        if p1 in update and p2 in update:
            if update.index(p1) > update.index(p2):
                notInOrder = True
                break

    if not notInOrder:
        sum += update[len(update) // 2]

print(sum)