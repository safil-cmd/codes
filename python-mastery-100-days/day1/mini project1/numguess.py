# import random
# secret_number = random.randint(1,10)
# attempts = 3
# print("welcome take a guess")
# while attempts > 0:
#     guess =int(input("enter num:"))
#     if guess == secret_number:
#         print("u win")
#     elif guess < secret_number:
#         print("too low")
#     else: 
#         print("to high try again")
#         attempts -=1

#         if attempts == 0:
#             print("try again, attempts left:", attempts,secret_number)
        
import random
number_to_guess = random.randint(1, 10)
attempts = 3  # ← Define it before using

print("Welcome! Take a guess between 1 and 10.")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number_to_guess:
        print("Congratulations! You guessed it right.")
        break
    else:
        attempts -= 1
        print(f"Wrong guess. Attempts left: {attempts}")

if attempts == 0:
    print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
