import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return player_choice, computer_choice

def check_winner(player, computer):
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        return "You win!" if computer == "scissors" else "You lose!"
    elif player == "paper":
        return "You win!" if computer == "rock" else "You lose!"
    elif player == "scissors":
        return "You win!" if computer == "paper" else "You lose!"
    else:
        return "Invalid choice. Please choose rock, paper, or scissors."

player_choice, computer_choice = get_choices()
result = check_winner(player_choice, computer_choice)
print(result)