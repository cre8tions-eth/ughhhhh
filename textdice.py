import random
import time
import os

# ASCII representations of dice faces
DICE_FACES = {
    1: ("+-------+", "|       |", "|   o   |", "|       |", "+-------+"),
    2: ("+-------+", "| o     |", "|       |", "|     o |", "+-------+"),
    3: ("+-------+", "| o     |", "|   o   |", "|     o |", "+-------+"),
    4: ("+-------+", "| o   o |", "|       |", "| o   o |", "+-------+"),
    5: ("+-------+", "| o   o |", "|   o   |", "| o   o |", "+-------+"),
    6: ("+-------+", "| o   o |", "| o   o |", "| o   o |", "+-------+"),
}

def print_dice(dice_values):
    """Print ASCII representation of dice side-by-side."""
    dice_art = [DICE_FACES[val] for val in dice_values]
    for i in range(5):  # Each die has 5 rows
        print("  ".join(die[i] for die in dice_art))

def roll_dice():
    """Simulate rolling three dice and return their values."""
    return [random.randint(1, 6) for _ in range(3)]

def roll_dice_animation():
    """Display a rolling dice animation."""
    print("\nRolling the dice...")
    for _ in range(10):  # Display intermediate rolls
        dice_values = roll_dice()
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        print_dice(dice_values)
        time.sleep(0.2)  # Short pause to create animation effect
    final_roll = roll_dice()
    os.system('cls' if os.name == 'nt' else 'clear')
    print_dice(final_roll)
    return final_roll

def determine_outcome(roll):
    """Determine the outcome of the roll according to C-Lo rules."""
    roll = sorted(roll, reverse=True)
    if roll[0] == roll[1] == roll[2]:  # Trips
        return ("Trips", roll[0])
    elif roll == [6, 5, 4]:  # Automatic win
        return ("6-5-4", 0)
    elif roll == [1, 2, 3]:  # Automatic loss
        return ("1-2-3", 0)
    elif roll[0] == roll[1]:  # Pair + Point
        return ("Point", roll[2])
    elif roll[1] == roll[2]:  # Pair + Point
        return ("Point", roll[0])
    else:  # No combo
        return ("No combo", 0)

def compare_outcomes(outcome1, outcome2):
    """Determine the winner based on outcomes."""
    ranks = {"Trips": 3, "6-5-4": 2, "Point": 1, "1-2-3": 0, "No combo": -1}

    if ranks[outcome1[0]] > ranks[outcome2[0]]:
        return "Player 1 wins!"
    elif ranks[outcome1[0]] < ranks[outcome2[0]]:
        return "Player 2 wins!"
    elif outcome1[0] == "Trips" and outcome2[0] == "Trips":
        return "Player 1 wins!" if outcome1[1] > outcome2[1] else "Player 2 wins!"
    elif outcome1[0] == "Point" and outcome2[0] == "Point":
        return "Player 1 wins!" if outcome1[1] > outcome2[1] else "Player 2 wins!"
    return "It's a tie!"

def main():
    print("Welcome to The Poke Pond plays C-Lo!")
    rounds = int(input("How many rounds would you like to play? "))

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        
        input("Press Enter to roll dice for Player 1...")
        player1_roll = roll_dice_animation()
        player1_outcome = determine_outcome(player1_roll)
        print(f"Player 1 rolled: {player1_roll} -> {player1_outcome}")
        
        input("Press Enter to roll dice for Player 2...")
        player2_roll = roll_dice_animation()
        player2_outcome = determine_outcome(player2_roll)
        print(f"Player 2 rolled: {player2_roll} -> {player2_outcome}")
        
        winner = compare_outcomes(player1_outcome, player2_outcome)
        print(f"Result: {winner}")

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()