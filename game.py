import random
import json
import os
import sys
from datetime import datetime

# Configuration for High Scores
SCORE_FILE = "highscores.json"

# ANSI Color Codes for Terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_scores():
    if not os.path.exists(SCORE_FILE):
        return []
    try:
        with open(SCORE_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_score(player_name, score, difficulty):
    scores = load_scores()
    new_entry = {
        "name": player_name,
        "score": score,
        "difficulty": difficulty,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    scores.append(new_entry)
    # Keep only top 10 scores, sorted by attempts (lower is better)
    scores = sorted(scores, key=lambda x: x['score'])[:10]
    
    with open(SCORE_FILE, 'w') as f:
        json.dump(scores, f, indent=4)

def display_leaderboard():
    scores = load_scores()
    print(f"\n{Colors.HEADER}=== 🏆 HALL OF FAME 🏆 ==={Colors.ENDC}")
    if not scores:
        print("No high scores yet. Be the first!")
    else:
        print(f"{'Name':<15} | {'Diff':<10} | {'Attempts':<10} | {'Date'}")
        print("-" * 55)
        for s in scores:
            print(f"{s['name']:<15} | {s['difficulty']:<10} | {s['score']:<10} | {s['date']}")
    print("-" * 55)

def get_difficulty():
    print(f"\n{Colors.CYAN}Select Difficulty:{Colors.ENDC}")
    print("1. Easy (1-50, Unlimited guesses)")
    print("2. Hard (1-100, 10 guesses)")
    print("3. Impossible (1-1000, 15 guesses)")
    
    while True:
        choice = input(f"{Colors.BOLD}Enter choice (1-3): {Colors.ENDC}")
        if choice == '1': return 50, float('inf'), "Easy"
        if choice == '2': return 100, 10, "Hard"
        if choice == '3': return 1000, 15, "Impossible"
        print(f"{Colors.FAIL}Invalid choice. Please try again.{Colors.ENDC}")

def play_game():
    clear_screen()
    print(f"{Colors.HEADER}🎲 WELCOME TO THE ULTIMATE NUMBER GUESSING GAME 🎲{Colors.ENDC}")
    
    upper_limit, max_guesses, difficulty_name = get_difficulty()
    secret_number = random.randint(1, upper_limit)
    attempts = 0
    
    print(f"\n{Colors.GREEN}I'm thinking of a number between 1 and {upper_limit}.{Colors.ENDC}")
    if max_guesses != float('inf'):
        print(f"You have {Colors.WARNING}{max_guesses}{Colors.ENDC} attempts.")

    while attempts < max_guesses:
        try:
            guess_str = input(f"\nAttempt {attempts + 1}: Enter your guess: ")
            if guess_str.lower() in ['quit', 'exit']:
                print("Thanks for playing!")
                sys.exit()
                
            guess = int(guess_str)
            attempts += 1
            
            if guess < 1 or guess > upper_limit:
                print(f"{Colors.WARNING}Please enter a number between 1 and {upper_limit}.{Colors.ENDC}")
                continue

            if guess < secret_number:
                print(f"{Colors.BLUE}Too low! 📉{Colors.ENDC}")
            elif guess > secret_number:
                print(f"{Colors.BLUE}Too high! 📈{Colors.ENDC}")
            else:
                print(f"\n{Colors.BOLD}{Colors.GREEN}🎉 CORRECT! The number was {secret_number}! 🎉{Colors.ENDC}")
                print(f"You won in {attempts} attempts.")
                
                save = input("Save high score? (y/n): ").lower()
                if save == 'y':
                    name = input("Enter your name: ")
                    save_score(name, attempts, difficulty_name)
                    display_leaderboard()
                return

        except ValueError:
            print(f"{Colors.FAIL}Invalid input. Please enter a valid integer.{Colors.ENDC}")

    print(f"\n{Colors.FAIL}💀 GAME OVER! You ran out of guesses.{Colors.ENDC}")
    print(f"The number was {Colors.BOLD}{secret_number}{Colors.ENDC}.")

if __name__ == "__main__":
    while True:
        play_game()
        if input(f"\n{Colors.CYAN}Play again? (y/n): {Colors.ENDC}").lower() != 'y':
            print("Goodbye!")
            break
