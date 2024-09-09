# lib/cli.py
from helpers import exit_program, dungeon_selection_menu, inn_menu


def main():
    print("Welcome to the adventure game!")
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            dungeon_selection_menu()
        elif choice == "2":
            inn_menu()
        elif choice == "3":
            pass
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


def menu():
    print("Please choose your destination:")
    print("1. Dungeon")
    print("2. Inn")
    print("3. Merchant")
    print("4. Quit game")


if __name__ == "__main__":
    main()
