# range 1500 - 2700
# range(10, 20, 2)
# function 
# looping -> 
# if statement
# divisble 

numbers = []
def find_values(start, end):
    for x in range(start, end + 1):
        if x % 7 == 0 and x % 5 == 0:
            numbers.append(x)
    print(numbers)


find_values(1500, 2700)