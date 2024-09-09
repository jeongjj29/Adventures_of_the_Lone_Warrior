# lib/helpers.py
from models.character import Character
from models.enemy import Enemy

player = Character.create("Player", 10, 100, 0)


def enemy_stats(enemy):
    print(
        f"{enemy.name} | HP: {enemy._current_hp} / {enemy._max_hp} | Attack: {enemy.attack}"
    )


def player_stats(player):
    print(
        f"{player.name} | HP: {player.current_hp} / {player.max_hp} | Attack: {player.attack}"
    )


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
    elif choice == "3":
        print("You have entered the Undead Graveyard.")
    elif choice == "4":
        print("You have entered the Dragon's Den.")
    elif choice == "5":
        return
    else:
        print("Invalid choice. Please try again.")


def dungeon_menu(location):
    if location == "cave":
        dungeon_monster = Enemy.create("Slime", 5, 20, 5)
        print(f"You have encountered a {dungeon_monster.name}.")
    while dungeon_monster.current_hp > 0 and player.current_hp > 0:
        print(enemy_stats(dungeon_monster))
        print(player_stats(player))
        print("What would you like to do?")
        print("1. Fight")
        print("2. Flee")

        choice = input("> ")
        if choice == "1":
            print(f"You attack the {dungeon_monster.name}.")
            battle_menu(dungeon_monster, player)
        elif choice == "2":
            print(f"You run away from the {dungeon_monster.name}.")
            dungeon_monster.delete()
        else:
            print("Invalid choice. Please try again.")


def battle_menu(enemy, player):
    enemy.defend(player.attack)
    player.defend(enemy.attack)
    print(f"You have dealt {player.attack} damage to the {enemy.name}.")
    print(f"{enemy.name} has dealt {enemy.attack} damage to you.")

    if enemy.current_hp <= 0:
        print("You won the battle!")

    if player.current_hp <= 0:
        print("You died.")
        exit_program()


def exit_program():
    print("Goodbye!")
    exit()
