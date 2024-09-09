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
            return
        else:
            print("Invalid choice. Please try again.")


def battle_menu(enemy, player):
    enemy.defend(player.attack)
    print(f"You have dealt {player.attack} damage to the {enemy.name}.")
    if enemy.current_hp <= 0:
        player.exp += enemy.max_hp
        player.gold += enemy.gold
        print(f"You have defeated the {enemy.name}.")
        print(player.level_up(enemy.max_hp))
        print(f"You have earned {enemy.gold} gold.")
        print(player.__repr__())

    player.defend(enemy.attack)
    print(f"{enemy.name} has dealt {enemy.attack} damage to you.")
    if player.current_hp <= 0:
        print("You died.")
        exit_program()


def inn_menu():
    print("Welcome to the inn.")
    print("What would you like to do?")
    print("1. Rest (10 gold)")
    print("2. Leave")

    choice = input("> ")
    if choice == "1":
        if player.gold >= 10:
            player.gold -= 10
            player.current_hp += 50
            if player.current_hp > player.max_hp:
                player.current_hp = player.max_hp
            print("You have healed 50 hp.")
            print(player.__repr__())
        else:
            print("You don't have enough gold.")
            print("You have been thrown out of the inn.")
            print(player.__repr__())
    elif choice == "2":
        return


def exit_program():
    print("Your adventure has ended.")
    print("Thank you for playing")
    print("Goodbye!")
    exit()
