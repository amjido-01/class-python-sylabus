def contains_dup(arr):
    hash_map = {}
    for num in arr:
        if num in hash_map:
            return True
        hash_map[num] = True
    return False

arr = [1, 2, 3, 4, 3, 5, 3, 3, 0]
res = contains_dup(arr)
print(res)

def print_goodbye_msg():
    print("Thank you for testing our program")

print_goodbye_msg()