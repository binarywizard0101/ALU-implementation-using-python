# ALU-implementation-using-python
As a passionate learner of computer architecture, I created this project to explore how basic instruction processing, arithmetic operations, and flag handling work in a simulated environment. This project helps visualize how a CPU handles addition, subtraction, bitwise operations, and flag setting in a simple register-based system.
# Features
✅ Supports basic arithmetic operations (ADD, SUB) 
✅ Includes bitwise operations (AND, OR, XOR) 
✅ Implements flag handling (Carry, Zero, Parity) 
✅ Simulates memory storage for results

![ALU] (https://ibb.co/WN0Whm4S)

# Instructions
The ALU accepts three instructions sequentially:

Loading Values

LOAD R1: Loads a value into register R1

LOAD R2: Loads a value into register R2

Storing Values

STORE R1 MEM: Stores the value of R1 into memory

STORE R2 MEM: Stores the value of R2 into memory

Arithmetic and Logic Operations

ADD: Adds values in R1 and R2

SUB: Subtracts R2 from R1

AND: Performs bitwise AND between R1 and R2

OR: Performs bitwise OR between R1 and R2

XOR: Performs bitwise XOR between R1 and R2

Flags are set based on the result:

Carry Flag (carry_flag): Set if the result exceeds a defined limit

Zero Flag (zero_flag): Set if the result is 0

Parity Flag (parity_flag): Set if the result is even
# Future Improvements
🔹 Adding multiplication & division operations 
🔹 Implementing overflow detection 
🔹 Enhancing memory management and addressing 
🔹 Extending support for more instructions
