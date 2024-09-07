# lib/helpers.py
from models.character import Character

def start_menu():
    print("Welcome to the adventure game!")
    print("Please enter your name:")
    name = input("> ")
    Character.create(name)
    print(f"Hello, {name}!")

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
