myList = [10, 30, 5, 100, 56]
# print(max(myList))
# print(len(myList))
# print(myList[::-1])
# print(myList[  :2  ][::-1])
print(myList[  2:  ])
def highestValue(arg):
    biggestValue = arg[0]
    for num in arg:
        if num > biggestValue:
            biggestValue = num
    print(biggestValue)
            
        
        
# highestValue(myList)