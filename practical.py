#   python program that will find those numbers which are divisible by 7 and multiple of 5 between 1500 and 2700 both inclusive with 10 different ways
# give 10 other ways
numbers = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        numbers.append(i)

print(numbers)