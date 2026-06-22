import random

choices = ["rock", "paper", "scissors"]
user_points = 0
computer_points = 0

while user_points < 5 and computer_points < 5:
    computer_choice = random.choice(choices)
    user_choice = input("Enter Your Choice : ROCK, PAPER, SCISSORS ").lower()
    
    if user_choice not in choices:
        print("Invalid input!")
        continue
    
    print("Computer chose:", computer_choice)

    
    if user_choice == "rock" and computer_choice == "scissors":
        print("Congratulations ! You won this Round")
        user_points += 1
        
    elif user_choice == "paper" and computer_choice == "rock":
        print("Congratulations ! You won this Round")
        user_points += 1
        
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Congratulations ! You won this Round")
        user_points += 1

    elif user_choice == computer_choice:
        print("Tie!")
        
    else:
        print("Computer wins ! ")
        computer_points += 1

    print("Score:")
    print("You:", user_points)
    print("Computer:", computer_points)
    print()

if user_points == 5:
    print("🎉 Congratulations! You won the game!")
else:
    print("💻 Computer won the game!")
    
    
