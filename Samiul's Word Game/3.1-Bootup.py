def boot_up():
    print("Welcome to the Codeword Puzzle Game!")
    print("Please select an option:")
    print("1. Administrator")
    print("2. Player")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")
    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (1/2/3): ")

    return choice

choice = boot_up()

if choice == "1":
    # Administrator login
    admin_username = input("Enter your username: ")
    admin_password = input("Enter your password: ")
    # Check username and password
    # ...
elif choice == "2":
    # Player login
    player_username = input("Enter your username: ")
    player_password = input("Enter your password: ")
    # Check username and password
    # ...
elif choice == "3":
    # Exit the program
    print("Exiting the program...")
    exit()