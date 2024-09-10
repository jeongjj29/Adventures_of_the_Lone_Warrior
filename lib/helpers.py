# lib/helpers.py
from models.character import Character
from models.enemy import Enemy
from models.equipment import Equipment


def battle(enemy, player):
    enemy.defend(player.attack)
    print(f"You have dealt {player.attack} damage to the {enemy.name}.")
    if enemy.current_hp <= 0:
        print(f"You have defeated the {enemy.name}.")
        player.level_up(enemy.max_hp)
        player.gold += enemy.gold
        print(f"You have earned {enemy.gold} gold.")
        print(player.__repr__())
        player.update()
        return
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
        player.update()
    else:
        print("You don't have enough gold.")
        print("You have been thrown out of the inn.")
        print(player.__repr__())


def display_inventory(character):
    character_inventory = character.inventory()
    if character_inventory == []:
        print("Inventory is empty.")
    for item in character_inventory:
        print(
            f"{item[0]}. {item[1]} | +{item[2]} Attack | +{item[3]} Max HP | {item[4]} Gold"
        )


def buy_sell(item_id, buyer, seller):
    item = Equipment.find_by_id(item_id)
    if item is None:
        print("That item does not exist.")
        return
    if buyer.gold < item.gold:
        print("You don't have enough gold.")
        return
    buyer.gold -= item.gold
    seller.gold += item.gold
    item.owner_id = buyer.id
    item.update()

    print(f"You have bought {item.name} for {item.gold} gold.")


def exit_program():
    print("Your adventure has ended.")
    print("Thank you for playing")
    print("Goodbye!")
    exit()
