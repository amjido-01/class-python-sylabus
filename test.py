x = [1,3,5,69,4,7,9];
print(x[0:4])

def myfunc(arg):
    higherVal = arg[0];
    for num in arg:
        if num > higherVal:
            higherVal = num
    print(higherVal)
    
    
myfunc(x)


def control_unit(instruction):
    opcode = instruction[0:4]
    if opcode == "000000":
        # Handle R-type instruction
        pass
    elif opcode == "100011":
        # Handle lw instruction
        pass
    elif opcode == "101011":
        # Handle sw instruction
        pass
    else:
        # Handle other instructions
        pass
    
result = control_unit(x)

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum(x))