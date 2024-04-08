196# give 10 other ways
numbers = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        numbers.append(i)

print(numbers)


#sql
def divisible_by_7_and_multiple_of_5(start, end):
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 == 0:
            yield i

result = list(divisible_by_7_and_multiple_of_5(1500, 2700))
print(result)

###############################33

def divisible_by_7_and_multiple_of_5(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 == 0:
            result.append(i)
    return result

result = divisible_by_7_and_multiple_of_5(1500, 2700)
print(result)

###################################################

result = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)
print(result)





