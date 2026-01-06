import random  # import random module

# Function to get player and computer choices
def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors): ").capitalize()
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

# Function to determine the winner
def check_win(player, computer):
    print(f"\nYou chose {player}, computer chose {computer}.\n")

    if player == computer:
        return "It's a tie!"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock smashes Scissors. You win!"
        else:
            return "Paper covers Rock. You lose!"
    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers Rock. You win!"
        else:
            return "Scissors cuts Paper. You lose!"
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts Paper. You win!"
        else:
            return "Rock smashes Scissors. You lose!"
    else:
        return "Invalid choice! Please choose Rock, Paper, or Scissors."

# Run the game
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
