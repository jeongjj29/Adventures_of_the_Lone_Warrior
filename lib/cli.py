# lib/cli.py
from helpers import (
    exit_program,
    battle,
    rest,
    display_inventory,
    buy_sell,
    display_characters,
    character_creation,
)
from models.character import Character
from models.enemy import Enemy
from models.equipment import Equipment

merchant = Character.find_by_id(1)


def welcome_menu():
    print("Welcome to the adventure game!")
    print("Would you like to create a new character or load an existing one?")
    print("\033[33m1. Create new character")
    print("2. Load existing character")
    print("3. Delete existing character\033[0m")
    choice = input("> ")
    if choice == "1":
        return character_creation_menu()
    elif choice == "2":
        return load_character_menu()
    elif choice == "3":
        delete_character_menu()
    else:
        print("Invalid choice. Please try again.")
        welcome_menu()


def character_creation_menu():
    print("Please enter your name:")
    name = input("> ")
    print("Please choose your playstyle:")
    print("\033[33m1. DPS")
    print("2. Tank")
    print("3. Balanced\033[0m")
    choice = input("> ")
    if choice == "1":
        player = character_creation(name, "dps")
        return player
    elif choice == "2":
        player = character_creation(name, "tank")
        return player
    elif choice == "3":
        player = character_creation(name, "balanced")
        return player
    else:
        print("Invalid choice. Please try again.")
        character_creation_menu()


def load_character_menu():
    print("Please select a character:")
    display_characters()
    choice = input("> ")
    player = Character.find_by_id(choice)
    if player is None:
        print("Invalid choice. Please try again.")
        load_character_menu()
    else:
        print(f"You have loaded {player.name}.")
        return player


def delete_character_menu():
    print("Please select a character:")
    display_characters()
    choice = input("> ")
    player = Character.find_by_id(choice)
    if player is None:
        print("Invalid choice. Please try again.")
        delete_character_menu()
    else:
        print(f"You have deleted {player.name}.")
        player.delete()
        welcome_menu()


player = welcome_menu()
print(player)


def main():
    while True:
        print("Please choose your destination:")
        print("1. Dungeon")
        print("2. Inn")
        print("3. Merchant")
        print("4. Display inventory")
        print("5. Quit game")
        choice = input("> ")
        if choice == "1":
            dungeon_selection_menu()
        elif choice == "2":
            inn_menu()
        elif choice == "3":
            merchant_menu()
        elif choice == "4":
            display_inventory(player)
            inventory_menu()
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
        dungeon_selection_menu()
    elif choice == "2":
        print("You have entered the Spider's Forest.")
        dungeon_menu("forest")
        dungeon_selection_menu()
    elif choice == "3":
        print("You have entered the Undead Graveyard.")
        dungeon_menu("graveyard")
        dungeon_selection_menu()
    elif choice == "4":
        print("You have entered the Dragon's Den.")
        dungeon_menu("den")
        dungeon_selection_menu()
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")


def dungeon_menu(location):
    dungeon_monster = Enemy.find_by_location(location)
    while dungeon_monster.current_hp > 0 and player.current_hp > 0:
        print(player.__repr__())
        print(dungeon_monster.__repr__())
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
        inn_menu()
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
        merchant_menu()
    elif choice == "2":
        buy_menu(merchant, player)
        merchant_menu()
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


def inventory_menu():
    print("What would you like to do?")
    print("Select equipment to equip by ID")
    print("0. Leave")
    choice = input("> ")
    if choice == "0":
        return
    else:
        equipment = Equipment.find_by_id(choice)
        if equipment.owner_id == player.id:
            player.equip(equipment)
            print(player.__repr__())
            return
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
