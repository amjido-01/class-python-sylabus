myList = [10, 30, 5, 100, 56]
# s = slice(3)
# print(myList[s])
# for x in myList:
#     print(x)
# print(max(myList))
# print(len(myList))
# print(myList[::-1])
# print(myList[  :2  ][::-1])
# print(myList[  2:  ])
# print(myList[-1])

def get_highest_value(arg):
    highestVal = arg[0]
    for num in arg:
        if num > highestVal:
            highestVal = num
    print(highestVal)
            


get_highest_value(myList)
# y = 'str'
# print(type(int('6')))
# print(range(10))
# print('hello world')