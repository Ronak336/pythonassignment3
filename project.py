import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setup
moves = ['rock', 'paper', 'scissors']
results = []

def get_user_move():
    while True:
        move = input("Enter your move (rock/paper/scissors or 'quit'): ").lower()
        if move in moves or move == 'quit':
            return move
        print("Invalid move. Try again.")

def get_computer_move():
    return np.random.choice(moves)

def decide_winner(user, comp):
    if user == comp:
        return 'Draw'
    win_conditions = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    return 'User' if win_conditions[user] == comp else 'Computer'

def play_game():
    print("Welcome to Rock, Paper, Scissors!\n")
    while True:
        user_move = get_user_move()
        if user_move == 'quit':
            break
        comp_move = get_computer_move()
        result = decide_winner(user_move, comp_move)

        print(f"Computer chose: {comp_move}")
        print(f"Result: {result}\n")

        results.append({
            'User Move': user_move,
            'Computer Move': comp_move,
            'Result': result
        })

def analyze_results(results_df):
    print("\nGame Summary:")
    print(results_df['Result'].value_counts())
    sns.set(style="whitegrid")

    # Countplot of results
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Result', data=results_df, palette='pastel')
    plt.title("Game Outcome Counts")
    plt.ylabel("Number of Games")
    plt.xlabel("Result")
    plt.show()

    # Heatmap of move combinations
    pivot = results_df.pivot_table(index='User Move', columns='Computer Move', aggfunc='size', fill_value=0)
    plt.figure(figsize=(6, 5))
    sns.heatmap(pivot, annot=True, cmap="Blues", fmt="d")
    plt.title("User vs Computer Moves")
    plt.show()

if __name__ == "__main__":
    play_game()
    if results:
        df = pd.DataFrame(results)
        analyze_results(df)
    else:
        print("No games played.")