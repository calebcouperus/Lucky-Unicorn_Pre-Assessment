"""Component 2 (How much) v4
putting v3 into a function"""


def num_check(question, low, high):
    error = "That was not a valid input\nPlease enter a number between {} and {}\n".format(low, high)

    # Keep asking until a valid number amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # Check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine
user_balance = num_check("How much would you like to play with?: ", 1, 10)
print(f"You are playing with ${user_balance}")
