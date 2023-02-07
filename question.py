numbers = []
def finding_numbers(begin, end):
    for x in range(begin, end+1):
        if x % 7 == 0 and x % 5 == 0:
            numbers.append(x)
    print(numbers)

finding_numbers(1500, 2700)
