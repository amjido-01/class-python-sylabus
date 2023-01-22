myList = [10, 30, 5, 100, 56]
def highestValue(arg):
    biggestValue = arg[0]
    for num in arg:
        if num > biggestValue:
            biggestValue = num
    print(biggestValue)
            
        
        
highestValue(myList)