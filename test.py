x = [1,3,5,69,4];
def myfunc(arg):
    higherVal = arg[0];
    for num in arg:
        if num > higherVal:
            higherVal = num
    print(higherVal)
    
    
myfunc(x)
