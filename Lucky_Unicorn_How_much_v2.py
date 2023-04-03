"""Component 2 (how much) v2
Fix crashing issue when a float or string is entered"""


error = "Please enter a whole number between 1 and 10\n"
valid = False

# Keep asking amount until a valid amount (1-10) is entered
while not valid:
    try:
        # Ask user for input
        user_balance = int(input("How much would you like to play with?: $"))

        # Check if the amount is too high/low
        if 0 < user_balance <= 10:
            print(f"you are playing with ${user_balance}")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)
