# variable 
        #data type
        #string
        #float
        #int
        #eval
        #7j 5i
        #list = [1, "str", True]
        
user_name_b = []
user_name_greater_four = []
users = ["umar", "bala", "kalid", "bashir", "bukhari"]
for user in users:
    if len(user) > 5:
        user_name_greater_four.append(user)

print(user_name_greater_four)
# function 

# loopng

# variable is like a container that holds a particular data type.

#python Naming convention


#camel
myNameIs ='umar'

#pascal 
MyAgeIs = 20

#snake
my_name_is = 'bala'



# block of code that execute when called
#1500 -> 2700
#multiple of five and divisble of 7

# for x in range(20, 30+1):
#     print(x)

# print(10 % 3)

numbers = []
def nums_divisible_multple(start, end):
    for number in range(start, end + 1):
        if number % 7 == 0 and number % 5 == 0:
            numbers.append(number)
    print(numbers)
nums_divisible_multple(1500, 2700)