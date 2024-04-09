import random

def guess_number():
    target_number = random.randint(1, 9)
    
    while True:
        guess = int(input("Guess a number between 1 and 9: "))
        
        if guess == target_number:
            print("Well guessed!")
            break
        else:
            print("Wrong guess. Try again.")

guess_number()

def print_goodbye_msg():
    print("Thank you for testing our program")

print_goodbye_msg()