import random # allows the terminal to generate a random choice 

game_choices = ["rock", "paper", "scissors"]
user_score = 0 # user's score
computer_score = 0 # computer's score

while True:
    user = input("Please select rock, paper, scissors, or type 'quit' to exit: ").lower() # requires user's input 

    if user == 'quit': # allows the user to quit the game
        break

    while user not in game_choices: # if the user has selected an invalid option, they will be prompted to select a valid option
        user = input(f"Your input {user} is invalid, please enter a valid option").lower()

    computer = random.choice(game_choices) # generates a random choice against the player

    print(f"user: {user}")
    print(f"computer: {computer}")

    if computer == user: # if the user and computer got the same choice
        print("It is a tie!")
    elif ((user=="paper" and computer=="scissors") or (user=="rock" and computer=="paper") or (user=="scissors" and computer=="rock")):
        print("You lose!")
        computer_score += 1
    elif ((user=="scissors" and computer=="paper") or (user=="rock" and computer=="scissors") or (user=="paper" and computer=="rock")):
        print("You win!")
        user_score += 1

    print(f"Score - You: {user_score}, Computer: {computer_score}\n")

print("Game Over!") # game is over
print(f"Final Score - You: {user_score}, Computer: {computer_score}")