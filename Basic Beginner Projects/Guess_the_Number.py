import random

magic_number = random.randint(1, 10)
guesses = 0

while True:
    n = int(input("Enter your Guess: "))
    guesses += 1

    if n == magic_number:
        print("Congrats! You guessed it correctly.")
        print("You used", guesses, "guesses.")
        break
    elif n < magic_number:
        print("Incorrect! Guess Higher.")
    else:
        print("Incorrect! Guess Lower.")

print("The magic number was", magic_number)