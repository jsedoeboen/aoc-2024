file =  open("example_input.txt", 'r')
# file =  open("input.txt", 'r')
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

def sort(rules, update):
    rule_map = {}
    for a, b in rules:
        key = tuple(sorted([a, b]))
        rule_map[key] = (a, b)

    correctly_ordered = []

    for page in update:
        placed = False
        for i, page2 in enumerate(correctly_ordered):
            key = tuple(sorted([page, page2]))
            if key in rule_map and rule_map[key] == (page, page2):
                correctly_ordered.insert(i, page)
                placed = True
                break
        if not placed:
            correctly_ordered.append(page)

    return correctly_ordered

sum = 0
for update in pages:
    notInOrder = False

    for p1, p2 in rules:
        if p1 in update and p2 in update:
            if update.index(p1) > update.index(p2):
                notInOrder = True
                break

    if notInOrder:
        sorted_update = sort(rules, update)
        sum += sorted_update[len(sorted_update) // 2]

print(sum)