array = [1, 2, 3, 4, 3, 5, 3, 3, 0];
def count_occurrences(array, value):
    count = 0

    for i in array:
        if i == value:
            count += 1
    return count


result = count_occurrences(array, 3)
print(result)

def print_goodbye_msg():
    print("Thank you for testing our program")

print_goodbye_msg()