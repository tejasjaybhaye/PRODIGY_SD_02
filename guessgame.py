import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    guessed = False

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
            
            # Increment the number of attempts
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
