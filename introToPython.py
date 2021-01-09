# Welcome user to game
print("Welcome to the Random Number Guesser")

# Prompt user to enter the minimum and maximum boundaries to define the range of the random numbers
# Store these values in their corresponding variables

# Create two strings to hold the error messages
error1 = "Invalid boundaries!" + "\n" + "Values for boundaries must be integers." + "\n" + "Please try again!"
error2 = "Error. Only integers are allowed"

# Define a function that takes a prompt and error as input


def get_input(message, error):
    while True:

        # Try to turn the string into an integer
        try:
            user_input = int(input(message))

        # If ValueError, continue to print error message
        except ValueError:
            print(error)
            continue

        # If success, return the string inputted as an integer
        else:
            return user_input
            break


# Use the get_input function to prompt users to enter boundary values,
# display error message and prompt user to try again if entries are not integers
lower_bound = get_input("Enter an integer to define the lower bound of the range of numbers: ", error1)
upper_bound = get_input("Enter an integer to define the upper bound of the range of numbers: ", error1)

# While the lower bound is more than or equal to upper bound, prompt the user to reenter values
# Repeat until the lower bound is less than the upper bound
while lower_bound >= upper_bound:
    print("Invalid boundaries!")
    print("The upper bound value must be larger than the lower bound value.")
    print("Please try again!")
    print("\n")
    lower_bound = get_input("Enter an integer to define the lower bound of the range of numbers: ", error1)
    upper_bound = get_input("Enter an integer to define the upper bound of the range of numbers: ", error1)


# Generate a random number using the boundaries inputted by the user
import random
random_number = random.randint(lower_bound, upper_bound)

# Prompt the user to guess a number, and store this number in the variable "guess"
guess = get_input("Guess a number within the range: ", error2)

# While the guess is incorrect, run this loop
while guess != random_number:

    # If the guess is correct, break out of the while loop, the larger while loop also ends
    if random_number == guess:
        break

        # If the number is higher, prompt the user to make a higher guess,
        # and break out of the current while loop to restart the larger loop
    if random_number > guess:
        print("Incorrect. The number is higher")
        guess = get_input("Guess a number within the range: ", error2)

    # If the number is lower, prompt the user to make a lower guess,
    # and break out of the current while loop to restart the larger loop
    if random_number < guess:
        print("Incorrect. The number is lower")
        guess = get_input("Guess a number within the range: ", error2)

# Congratulate the user if the the guess is correct
print("Congratulations! You guessed the number")

