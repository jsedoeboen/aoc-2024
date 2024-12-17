# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

class Register:
    a, b, c = None, None, None

register = Register()

program_input = []

for line in lines:
    if line.startswith("Register A:"):
        register.a = int(line.split(": ")[-1])
    if line.startswith("Register B:"):
        register.b = int(line.split(": ")[-1])
    if line.startswith("Register C:"):
        register.c = int(line.split(": ")[-1])
    if line.startswith("Program:"):
        program_input = [int(x) for x in line.split(": ")[1].split(",")]

def decode_combo(operand):
    if operand <= 3: return operand
    elif operand == 4: return register.a
    elif operand == 5: return register.b
    elif operand == 6: return register.c

def adv(operand):
    register.a = int(register.a / (2 ** decode_combo(operand)))

def bxl(operand):
    register.b = register.b ^ operand

def bst(operand):
    register.b = decode_combo(operand) % 8

def bxc():
    register.b = register.b ^ register.c

def bdv(operand):
    register.b = int(register.a / (2 ** decode_combo(operand)))

def cdv(operand):
    register.c = int(register.a / (2 ** decode_combo(operand)))

def run_program(program):
    out = []
    i = 0
    while i < len(program):
        next_i = i + 2
        opcode = program[i]
        operand = program[i+1]

        if opcode == 0:
            adv(operand)
        elif opcode == 1:
            bxl(operand)
        elif opcode == 2:
            bst(operand)
        elif opcode == 3: # jnz
            if register.a != 0:
                next_i = operand
        elif opcode == 4:
            bxc()
        elif opcode == 5: # out
            out.append(decode_combo(operand) % 8)
        elif opcode == 6:
            bdv(operand)
        elif opcode == 7:
            cdv(operand)

        i = next_i
    return out

# output = run_program()
# print(",".join(str(x) for x in output))

step = 0
# while i < len(program):
# out = [5, 5, 7, 5, 5, 5, 3, 3, 0, 1, 5, 5, 5, 5, 7, 4]
i = 190384609431823
stop = 2000000000000000
t = 0
while True:
    register.a = i
    register.b = 0
    register.c = 0
    out = run_program(program_input)

    if out[-8:] == [0,3,1,7,5,5,3,0]:
    # if out[-6:] == [1,7,5,5,3,0]:
    # if out[:6] == [2,4,1,2,7,5]:
        print(i, "\t", i-t, "\t",  out)
        t = i
    if out == program_input:
        print("out is input for i:", i)
        break

    if len(out) > len(program_input):
        print("out is longer than input for i:", i)
        break

    diff = len(program_input)-len(out)

    # if diff == 0:
    #     print("diff is 0 at i:", i)
    #     break

    if i > stop:
        print("i is greater than stop:", i)
        break

    i = i + 1
    step += 1



