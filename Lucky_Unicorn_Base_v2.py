"""Lucky Unicorn base component
Components added after they have been created and tested
"""
import random


# Yes/No checking function
def yes_no(question_text):
    while True:
        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output "Program Continues'
        if answer == 'yes' or answer == 'y':
            answer = "Yes"
            return answer

        # If they say no, output "Display instructions'
        elif answer == 'no' or answer == 'n':
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# Function to display instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("Choose a starting amount to play with - must be between $1 and $ 10")
    print("Then press <enter> to play. \n"
          "You will get a random token which might be a horse, a zebra, a donkey, or a unicorn")
    print()
    print("It costs $1 to play each round but, depending on your prize, you "
          "could win some of your money back. These are the payout amount:\n"
          "\tUnicorn: $5\n"
          "\tHorse:   $0.50\n"
          "\tZebra:   $0.50\n"
          "\tDonkey:  $0\n")
    print("See if you can avoid donkeys, get the unicorns, and finish with "
          "more money than you started with.\n")
    print("*" * 50)
    print()


# Number checking function
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


# Function for random token
def generate_token(balance):
    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "X":
        rounds_played += 1  # keep track of rounds
        number = random.randint(1, 100)  # Only gives donkey

        # adjust balance
        # if the number is between 1 and 5
        # User gets unicorn add $4 to balance
        if 1 <= number <= 5:
            token = "Unicorn"
            balance += 4

        # If the number between 6 and 36
        # User gets donkey (Subtract $1 from balance)
        elif 6 <= number <= 36:
            token = "Donkey"
            balance -= 1

        # In all other cases token must be a horse or zebra
        # Subtract $0.50 from balance in either case
        else:
            # If number is even, set token to zebra
            if number % 2 == 0:
                token = "Zebra"
                balance -= 0.5

            # Otherwise set token to horse
            else:
                token = "Horse"
                balance -= 0.5

        # Output
        print(f"Round {rounds_played}.\n"
              f"Token: {token}\n"
              f"Balance: ${balance:.2f}\n")

        # breaks loop if out balance = 0
        if balance <= 0:
            print("Sorry you ran out of money")
            break

        # Asking to play again
        play_again = input("Do you want to play another round\n"
                           "<enter> to play again or 'X' to exit\n"
                           ">>>\n"
                           "").upper()
    return balance


# Main routine starts here
played_before = yes_no("Have you played this game before?: ")

if played_before == "No":
    instructions()

# Ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with?: $", 1, 10)
print(f"You are playing with ${starting_balance}\n")

closing_balance = generate_token(starting_balance)
print()
print(f"Thankyou for playing\n"
      f"You started with ${starting_balance:.2f}\n"
      f"and you leave with ${closing_balance:.2f}\n"
      f"Goodbye")
