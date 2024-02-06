# Yahtzee Game
#submission by Paavni Shankar Bhatnagar

import random

class YahtzeeGame:
    def __init__(self):
        # Initialize game state variables
        self.cup = [0, 0, 0, 0, 0]
        self.held_dice = [False, False, False, False, False]
        self.roll_count = 0
        self.score_sheet = {chr(ord('A') + i): [None] * 13 for i in range(2)}
        self.current_player = 'A'

    def roll_dice(self):
        # Roll the dice if the roll count is less than 3
        if self.roll_count < 3:
            for i in range(5):
                if not self.held_dice[i]:
                    self.cup[i] = random.randint(1, 6)
            self.display_dice()
            self.roll_count += 1
        else:
            print("You can't roll more than 3 times in a turn.")

    def display_dice(self):
        # Display the current dice values
        print(f"Current Dice: {self.cup}")

    def hold_dice(self, indices):
        # Hold specific dice based on user input
        for index in indices:
            if 1 <= index <= 5:
                self.held_dice[index - 1] = True
            else:
                print("Invalid dice index. Please enter a number between 1 and 5.")

    def release_dice(self, indices):
        # Release specific dice based on user input
        for index in indices:
            if 1 <= index <= 5:
                self.held_dice[index - 1] = False
            else:
                print("Invalid dice index. Please enter a number between 1 and 5.")

    def score_dice(self, category):
        # Score the current dice in a specified category
        if category in self.score_sheet[self.current_player] and self.score_sheet[self.current_player][category] is None:
            score = sum(self.cup)
            self.score_sheet[self.current_player][category] = score
            print(f"Scored {score} points for {category}.")
        else:
            print(f"{category} already scored or does not exist.")

    def show_score_sheet(self):
        # Display the current player's score sheet
        print(f"\nPlayer {self.current_player}'s Score Sheet:")
        for i, score in enumerate(self.score_sheet[self.current_player]):
            category = chr(ord('A') + i)
            if score is not None:
                print(f"{category}: {score}")
            else:
                print(f"{category}: Not scored yet")

    def switch_player(self):
        # Switch to the other player's turn
        self.current_player = 'B' if self.current_player == 'A' else 'A'

    def print_help(self):
        # Display a help message with available commands
        print("\nCommands:")
        print(" - roll: Roll the dice.")
        print(" - hold: Hold specific dice.")
        print(" - release: Release specific dice.")
        print(" - sheet: Display the current player's score sheet.")
        print(" - score: Score the current dice in a category (A, B, C, ..., M).")
        print(" - switch: Switch to the other player's turn.")
        print(" - help: Display this help message.")

    def play_game(self):
        # Main game loop
        print("Welcome to Yahtzee!")
        while None in self.score_sheet['A'] + self.score_sheet['B']:
            print(f"\nPlayer {self.current_player}'s Turn:")
            self.roll_dice()

            # Get user command and execute corresponding action
            command = input("Enter command (roll, hold, release, sheet, score, switch, help): ").lower()

            if command == "roll":
                self.roll_dice()
            elif command == "hold":
                indices = list(map(int, input("Enter dice indices to hold (space-separated): ").split()))
                self.hold_dice(indices)
            elif command == "release":
                indices = list(map(int, input("Enter dice indices to release (space-separated): ").split()))
                self.release_dice(indices)
            elif command == "sheet":
                self.show_score_sheet()
            elif command == "score":
                category = input("Enter category to score (A, B, C, ..., M): ").upper()
                self.score_dice(category)
            elif command == "switch":
                self.switch_player()
                print(f"Switched to Player {self.current_player}'s turn.")
            elif command == "help":
                self.print_help()
            else:
                print("Invalid command. Type 'help' for available commands.")

if __name__ == "__main__":
    # Initialize and play the Yahtzee game
    yahtzee = YahtzeeGame()
    yahtzee.play_game()
