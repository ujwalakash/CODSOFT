import random
class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]
    def get_user_choice(self):
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower()
            if user_input in self.choices:
                return user_input
            else:
                print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
    def get_computer_choice(self):
        return random.choice(self.choices)
    def determine_winner(self, user_choice, computer_choice):
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win this round!"
        else:
            self.computer_score += 1
            return "Computer wins this round!"

    def display_scores(self):
        print(f"\n--- Current Score ---")
        print(f"Your Score: {self.user_score}")
        print(f"Computer Score: {self.computer_score}")
        print("---------------------")

    def play_round(self):
        print("\n--- New Round ---")
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        print(result)
        self.display_scores()

    def play_game(self):
        print("Welcome to Rock-Paper-Scissors!")
        while True:
            self.play_round()
            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again == "yes":
                pass
            elif play_again == "no":
                print("\nThanks for playing!")
                self.display_scores() 
                print("\n--- Final Result ---")
                if self.user_score > self.computer_score:
                    print("Congratulations! You won the game overall!")
                elif self.computer_score > self.user_score:
                    print("The computer won the game overall. Better luck next time!")
                else:
                    print("The game ended in a tie overall!")
                print("--------------------")
                break 
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_game()