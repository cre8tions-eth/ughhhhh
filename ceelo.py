import random

def roll_dice():
    """Simulates rolling three dice and returns the result."""
    return sorted([random.randint(1, 6) for _ in range(3)], reverse=True)

def determine_outcome(roll):
    """Determines the outcome of the roll according to Cee-lo rules."""
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
    else:  # No valid combination
        return ("No combo", 0)

def compare_outcomes(outcome1, outcome2):
    """Determines the winner based on the outcomes."""
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
    print("Welcome to the Cee-lo Dice Game!")
    rounds = int(input("How many rounds would you like to play? "))

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        input("Press Enter to roll dice for Player 1...")
        player1_roll = roll_dice()
        player1_outcome = determine_outcome(player1_roll)
        print(f"Player 1 rolled: {player1_roll} -> {player1_outcome}")

        input("Press Enter to roll dice for Player 2...")
        player2_roll = roll_dice()
        player2_outcome = determine_outcome(player2_roll)
        print(f"Player 2 rolled: {player2_roll} -> {player2_outcome}")

        winner = compare_outcomes(player1_outcome, player2_outcome)
        print(f"Result: {winner}")

if __name__ == "__main__":
    main()