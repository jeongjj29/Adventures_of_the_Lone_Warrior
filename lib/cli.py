# lib/cli.py
from helpers import (
    exit_program,
    helper_1
)


def main():
    start_menu()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice. Please try again.")



def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")

def start_menu():
    print("Welcome to the adventure game!")
    print("Please enter your name:")
    name = input("> ")
    print(f"Hello, {name}!")
    return
 

if __name__ == "__main__":
    main()
