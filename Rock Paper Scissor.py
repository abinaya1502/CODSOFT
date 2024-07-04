import random

def play_game():
    # Define the possible choices
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        # Get the user's choice
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        # Get the computer's choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
play_game()
