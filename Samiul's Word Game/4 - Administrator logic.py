# Create the codeword and key grids
codeword_grid = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
key_grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Loop until administrator quits
while True:
    # Display the menu choices
    print("Menu:\na. Display the codeword puzzle\nb. Display the key grid\nc. Add a word to the puzzle\nd. Delete a word from the puzzle\ne. Edit the puzzle\nf. Create new puzzle with all 26 letters\ng. Quit")

    # Get the administrator's choice
    choice = input("Enter your choice (a-g): ")

    # Display the codeword puzzle
    if choice == "a":
        for row in codeword_grid:
            print(row)

    # Display the key grid
    elif choice == "b":
        for row in key_grid:
            print(row)

    # Add a word to the puzzle
    elif choice == "c":
        word = input("Enter the word to add: ").upper()

        # Check if the word uses only letters A-Z
        if not all(letter.isalpha() and letter.isupper() for letter in word):
            print("Word must use only uppercase letters A-Z.")
            continue

        # Check if the word already exists in the puzzle
        if any(word in row for row in codeword_grid):
            print("Word already exists in the puzzle.")
            continue

        # Add the word to the puzzle
        for row in codeword_grid:
            if ' ' in row:
                index = row.index(' ')
                if index + len(word) <= 3:
                    row[index:index + len(word)] = list(word)
                    break
        else:
            print("Cannot add word to the puzzle.")
            continue

        # Update the key grids
        for i in range(len(codeword_grid)):
            for j in range(len(codeword_grid[i])):
                if codeword_grid[i][j] != ' ':
                    key_grid[i][j] = codeword_grid[i][j]

        # Display the updated grids
        print("Codeword Grid:")
        for row in codeword_grid:
            print(row)
        print("Key Grid:")
        for row in key_grid:
            print(row)

    # Delete a word from the puzzle
    elif choice == "d":
        word = input("Enter the word to delete: ").upper()

        # Check if the word exists in the puzzle
        for row in codeword_grid:
            if word in ''.join(row):
                row[row.index(word[0])] = ' '
                break
        else:
            print("Word does not exist in the puzzle.")
            continue

        # Update the key grids
        for i in range(len(codeword_grid)):
            for j in range(len(codeword_grid[i])):
                if codeword_grid[i][j] == ' ':
                    key_grid[i][j] = ' '

        # Display the updated grids
        print("Codeword Grid:")
        for row in codeword_grid:
            print(row)
        print("Key Grid:")
        for row in key_grid:
            print(row)

    # Edit the puzzle
    elif choice == "e":
        old_word = input("Enter the word to edit: ").upper()
        new_word = input("Enter the new word: ").upper()

        # Check if the old word exists in the puzzle
        for row in codeword_grid:
            if old_word in ''.join(row):
                row[row.index(old_word[0])] = ' '
                break
        else:
            print("Word does not exist in the puzzle.")
            continue

        # Check if the new word uses only letters A-Z
        if not all(letter.isalpha() and letter.isupper() for letter in new_word):
            print("Word must use only uppercase letters A-Z.")
            continue

        # Check if the new word already exists in the puzzle
        if any(new_word in row for row in codeword_grid):
            print("Word already exists in the puzzle.")
            continue

        # Add the new word to the puzzle
        for row in codeword_grid:
            if ' ' in row:
                index = row.index(' ')
                if index + len(new_word) <= 3:
                    row[index:index + len(new_word)] = list(new_word)
                    break
        else:
            print("Cannot add word to the puzzle.")
            continue

        # Update the key grids
        for i in range(len(codeword_grid)):
            for j in range(len(codeword_grid[i])):
                if codeword_grid[i][j] != ' ':
                    key_grid[i][j] = codeword_grid[i][j]

        # Display the updated grids
        print("Codeword Grid:")
        for row in codeword_grid:
            print(row)
        print("Key Grid:")
        for row in key_grid:
            print(row)

    # Create new puzzle with all 26 letters
    elif choice == "f":
        new_grid = [[' ']*3 for _ in range(3)]
        words = ["JAZZ", "BUZZ", "FUZZ", "HUBBUB", "MUZZLE", "PUZZLE", "QUIZZICAL", "RIZZUTO", "SIZZLE", "WAZOO"]
        for word in words:
            for row in new_grid:
                if ' ' in row:
                    index = row.index(' ')
                    if index + len(word) <= 3:
                        row[index:index + len(word)] = list(word)
                        break
            else:
                continue
            break
        else:
            print("Cannot create puzzle with all 26 letters.")
            continue

        # Update the grids
        codeword_grid = new_grid
        key_grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        # Display the updated grids
        print("Codeword Grid:")
        for row in codeword_grid:
            print(row)
        print("Key Grid:")
        for row in key_grid:
            print(row)

    # Quit
    elif choice == "g":
        break

    # Invalid choice
    else:
        print("Invalid choice.")