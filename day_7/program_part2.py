import operator

# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

concatFunc = lambda x, y: int(str(x) + str(y))
operators = [operator.mul, operator.add, concatFunc]

def solvable(result, inputs):
    if len(inputs) == 1 or result < inputs[0]:
        return result == inputs[0]

    for op in operators:
        if solvable(result, [op(inputs[0], inputs[1])] + inputs[2:]):
            return True
    return False


sum = 0
for line in lines:
    result, input = line.split(': ')
    result = int(result)
    inputs = [int(x) for x in input.split()]

    solved = solvable(result, inputs)
    print(f"{result} = {inputs} -> {solved}")
    if solved:
        sum += result


print(sum)