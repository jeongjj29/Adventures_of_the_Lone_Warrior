# lib/helpers.py



def start_menu():
    print("Welcome to the adventure game!")
    print("Please enter your name:")
    name = input("> ")
    print(f"Hello, {name}!")

def dungeon_menu():
    print("Please select a dungeon.")
    print("1. Slime Cave")
    print("2. Spider's Forest")
    print("3. Undead Graveyard")
    print("4. Dragon's Den")
    print("5. Return to the main menu")

    choice = input("> ")
    if choice == "1":
        print("You have entered the Slime Cave.")
    elif choice == "2":
        print("You have entered the Spider's Forest.")
    elif choice == "3":
        print("You have entered the Undead Graveyard.")
    elif choice == "4":
        print("You have entered the Dragon's Den.")
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")


def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
