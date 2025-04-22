operation = 0
flag = 0
carry_flag = 0
parity_flag = 0
zero_flag = 0
memory = [0] * 1000000
operand1 = 0
operand2 = 0
registers = [0,0,0,0,0,0,0,0]

instruct_1 = input("Enter instruction")
instruct_2 = input("Enter instruction")
instruct_3 = input("Enter instruction")

if instruct_1 == "LOAD R1":
    operand1 = int(input("Enter operand 1:"))
elif instruct_1 == "STORE R1 MEM":
    operand1 = int(input("Enter operand 1:"))
    memory.append(operand1)

if instruct_2 == "LOAD R2":
    operand2 = int(input("Enter operand 2:"))
elif instruct_2 == "STORE R2 MEM":
    operand2 = int(input("Enter operand 2:"))
    memory.append(operand2)

if instruct_3 == "ADD":
    operand1 = operand1 + operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation
    print("Result stored inside memory at 0 address")
    print(operand1)

if instruct_3 == "SUB":
    operand1 = operand1 - operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation    
    print("Result stored inside memory at 0 address")
    print(operand1)

if instruct_3 == "AND":
    operand1 = operand1 and operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation
    print("Result stored inside memory at 0 address")
    print(operand1)

if instruct_3 == "OR":
    operand1 = operand1 or operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation
    print("Result stored inside memory at 0 address")
    print(operand1)

if instruct_3 == "XOR":
    operand1 = operand1 ^ operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation
    print("Result stored inside memory at 0 address")
    print(operand1)

# Flag calculations
zero_flag = 1 if operand1 == 0 else 0
flag = 1 if operand1 != 0 else 0
carry_flag = 1 if operand1 >= 10 else 0
parity_flag = 1 if operand1 % 2 == 0 else 0

print(memory[0])
