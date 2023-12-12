# Simple Python Text-Based Game: Treasure Hunt

# Importing necessary libraries
import random
import sys

# Define the game map size
MAP_SIZE = 5

# Function to create the game map
def create_map(size):
    return [["." for _ in range(size)] for _ in range(size)]

# Function to place treasure on the map
def place_treasure(map):
    x = random.randint(0, len(map) - 1)
    y = random.randint(0, len(map) - 1)
    map[x][y] = "T"

# Function to print the current state of the map
def print_map(map):
    for row in map:
        print(" ".join(row))

# Function to ask the player for their move
def get_player_move():
    x = int(input("Enter row number (0-{}): ".format(MAP_SIZE - 1)))
    y = int(input("Enter column number (0-{}): ".format(MAP_SIZE - 1)))
    return x, y

# Function to check if the player found the treasure
def check_treasure(map, x, y):
    return map[x][y] == "T"

# Function to update the map after player's move
def update_map(map, x, y):
    if map[x][y] == ".":
        map[x][y] = "X"

# Main function to run the game
def main():
    print("Welcome to the Treasure Hunt Game!")
    game_map = create_map(MAP_SIZE)
    place_treasure(game_map)

    moves = 0

    while True:
        print_map(game_map)
        x, y = get_player_move()

        if check_treasure(game_map, x, y):
            print("Congratulations! You have found the treasure in {} moves!".format(moves))
            break
        else:
            update_map(game_map, x, y)
            print("No treasure here. Keep searching!")
            moves += 1

        if moves > 10:
            print("Game Over! You've exceeded the maximum number of moves.")
            break

# Check if the script is run as the main program
if __name__ == "__main__":
    main()
