# lib/helpers.py
from models.character import Character
from models.enemy import Enemy


def battle(enemy, player):
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


def rest(player):
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


def exit_program():
    print("Your adventure has ended.")
    print("Thank you for playing")
    print("Goodbye!")
    exit()
