# lib/cli.py
from helpers import exit_program, battle, rest, display_inventory, buy_sell
from models.character import Character
from models.enemy import Enemy
from models.equipment import Equipment

player = Character.find_by_id(1)
merchant = Character.find_by_id(2)


def main():
    print("Welcome to the adventure game!")
    while True:
        print("Please choose your destination:")
        print("1. Dungeon")
        print("2. Inn")
        print("3. Merchant")
        print("5. Quit game")
        choice = input("> ")
        if choice == "1":
            dungeon_selection_menu()
        elif choice == "2":
            inn_menu()
        elif choice == "3":
            merchant_menu()
        elif choice == "5":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


def dungeon_selection_menu():
    print("Please select a dungeon.")
    print("1. Slime Cave")
    print("2. Spider's Forest")
    print("3. Undead Graveyard")
    print("4. Dragon's Den")
    print("5. Return to the main menu")

    choice = input("> ")
    if choice == "1":
        print("You have entered the Slime Cave.")
        dungeon_menu("cave")
    elif choice == "2":
        print("You have entered the Spider's Forest.")
        dungeon_menu("forest")
    elif choice == "3":
        print("You have entered the Undead Graveyard.")
        dungeon_menu("graveyard")
    elif choice == "4":
        print("You have entered the Dragon's Den.")
        dungeon_menu("den")
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")


def dungeon_menu(location):
    dungeon_monster = Enemy.find_by_location(location)
    while dungeon_monster.current_hp > 0 and player.current_hp > 0:
        print(dungeon_monster.__repr__())
        print(player.__repr__())
        print("What would you like to do?")
        print("1. Fight")
        print("2. Flee")

        choice = input("> ")
        if choice == "1":
            print(f"You attack the {dungeon_monster.name}.")
            battle(dungeon_monster, player)
        elif choice == "2":
            print(f"You run away from the {dungeon_monster.name}.")
            return
        else:
            print("Invalid choice. Please try again.")


def inn_menu():
    print("Welcome to the inn.")
    print("What would you like to do?")
    print("1. Rest (10 gold)")
    print("2. Leave")

    choice = input("> ")
    if choice == "1":
        rest(player)
    elif choice == "2":
        return


def merchant_menu():
    print("Welcome to the general store.")
    print("What would you like to do?")
    print("1. Buy equipment")
    print("2. Sell equipment")
    print("3. Leave")

    choice = input("> ")
    if choice == "1":
        buy_menu(player, merchant)
    elif choice == "2":
        buy_menu(merchant, player)
    elif choice == "3":
        return


def buy_menu(buyer, seller):
    display_inventory(seller)
    print(f"Current Gold: {buyer.gold}")
    print("Select item by ID")
    print("0. Leave")
    choice = input("> ")
    if choice == "0":
        return
    else:
        buy_sell(choice, buyer, seller)


if __name__ == "__main__":
    main()
