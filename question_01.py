def divisible_by_7_and_multiple_of_5(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 == 0:
            result.append(i)
    return result

result = divisible_by_7_and_multiple_of_5(1500, 2700)
print(result)
