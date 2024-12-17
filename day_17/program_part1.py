file = open("example_input.txt", 'r')
# file =  open("input.txt", 'r')
lines = file.readlines()

class Register:
    a, b, c = None, None, None

register = Register()

program = []

for line in lines:
    if line.startswith("Register A:"):
        register.a = int(line.split(": ")[-1])
    if line.startswith("Register B:"):
        register.b = int(line.split(": ")[-1])
    if line.startswith("Register C:"):
        register.c = int(line.split(": ")[-1])
    if line.startswith("Program:"):
        program = [int(x) for x in line.split(": ")[1].split(",")]

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

def run_program():
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

output = run_program()
print(",".join(str(x) for x in output))