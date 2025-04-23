operation = 0
flag = 0
carry_flag = 0
parity_flag = 0
zero_flag = 0
memory = [0] * 1000000
operand1 = None
operand2 = None

instruct_1 = input("Enter instruction:\n")
instruct_2 = input("Enter instruction:\n")
instruct_3 = input("Enter instruction:\n")

if instruct_1 == "LOAD R1":
    operand1 = int(input("Enter operand 1:\n"))
elif instruct_1 == "STORE R1 MEM":
    operand1 = int(input("Enter operand 1:\n"))
    memory[0] = operand1

if instruct_2 == "LOAD R2":
    operand2 = int(input("Enter operand 2:\n"))
elif instruct_2 == "STORE R2 MEM":
    operand2 = int(input("Enter operand 2:\n"))
    memory[1] = operand2
if operand1 == None or operand2 == None:
    print("One of the operand is not loaded")
    exit()
    
if instruct_3 == "ADD":
    operation = operand1 + operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation
    print("\nResult stored inside memory at 0 address")
    print(operation)

if instruct_3 == "SUB":
    operation = operand1 - operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation    
    print("\nResult stored inside memory at 0 address")
    print(operation)

if instruct_3 == "AND":
    operation = operand1 and operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation
    print("\nResult stored inside memory at 0 address")
    print(operation)

if instruct_3 == "OR":
    operation= operand1 or operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation
    print("\nResult stored inside memory at 0 address")
    print(operation)

if instruct_3 == "XOR":
    operation = operand1 ^ operand2
    memory[0] = operand1
    memory[1] = operand2
    memory[2] = operation
    print("\nResult stored inside memory at 0 address")
    print(operation)


zero_flag = 1 if operand1 == 0 else 0
flag = 1 if operand1 != 0 else 0
carry_flag = 1 if operand1 >= 10 else 0
parity_flag = 1 if operand1 % 2 == 0 else 0

print("\nFlag status")
print("Carry Flag:", carry_flag)
print("Zero Flag:", zero_flag)
print("Parity Flag:", parity_flag)
print("General Flag:", flag)
    
print("\nContents in memory")
print("Address 0:", memory[0])
print("Adress 1:", memory[1])
print("Address 2:",memory[2])

