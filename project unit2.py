import random

print("Welcome to the Number Guessing Game!")
print("---------------------------------------")

# computer chooses a random number between 1 and 100
secret_number = random.randint(1, 1000)

# to count number of attempts
attempts = 0

print("I have chosen a number between 1 and 1000.")
print("Try to guess it!")

while True:
    try:
        # take user input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # check conditions
        if guess == secret_number:
            print("Congratulations! You guessed correctly.")
            print("Total attempts:", attempts)
            break
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

    except ValueError:
        print("Please enter a valid number!")

print("Game Over. Thanks for playing!")
