# Create the codeword and key grids
codeword_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
key_grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Create the player keys
player1_key = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
player2_key = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Initialize the player health values
player1_health = 5
player2_health = 5

# Loop until either player quits or puzzle is solved
while True:
    # Display the menu choices
    print("Menu:\n1. Play the game\n2. Quit")

    # Get the player's choice
    choice = input("Enter your choice (1/2): ")

    # If the player chooses to quit, break out of the loop
    if choice == "2":
        break

    # Get the player's name
    player_name = input("Enter your name: ")

    # Determine which player is playing
    if player_name == "Player 1":
        player_key = player1_key
        player_health = player1_health
    else:
        player_key = player2_key
        player_health = player2_health

    # Check if the player has enough health to play
    if player_health < 2:
        print("You don't have enough health to play.")
        continue

    # Display the codeword and key grids
    print("Codeword Grid:")
    for row in codeword_grid:
        print(row)
    print("Key Grid:")
    for row in player_key:
        print(row)

    # Get the cell to complete from the player
    cell = input("Enter the cell you want to complete (index number): ")
    index = int(cell)

    # Get the row and column of the cell
    row = (index - 1) // 3
    col = (index - 1) % 3

    # Get the letter to fill in from the player
    letter = input("Enter the letter to fill in: ")

    # Check if the letter is correct
    if key_grid[row][col] == letter:
        print("Correct!")
        player_health += 2
        player_key[row][col] = codeword_grid[row][col]
    else:
        print("Incorrect!")
        player_health -= 2
        player_key[row][col] = 0

    # Display the updated player key grid
    print("Player Key Grid:")
    for row in player_key:
        print(row)

    # Check if the puzzle is solved
    if player_key == codeword_grid:
        print("Congratulations, you solved the puzzle!")
        break

    # Go to the next player
    if player_name == "Player 1":
        player1_key = player_key
        player1_health = player_health
    else:
        player2_key = player_key
        player2_health = player_health

# Print player statistics
print("Player 1: Correct guesses = {}, Incorrect guesses = {}, Health = {}".format(
    sum(1 for row in player1_key for cell in row if cell != 0),
    sum(1 for row in player1_key for cell in row if cell == 0),
    player1_health
))
print("Player 2: Correct guesses = {}, Incorrect guesses = {}, Health = {}".format(
    sum(1 for row in player2_key for cell in row if cell != 0),
    sum(1 for row in player2_key for cell in row if cell == 0),
    player2_health
))