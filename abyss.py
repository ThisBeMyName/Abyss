import sys
import os
import pyfiglet
import time
import parser
import random

# Importing monster data from 'monsters.py' file.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'monsters')))
from monsters.monsters import *

def player_attack(player_class, creature):
    attack_chance = player_class["Agility"] / random.randint(1, 4)
    print(attack_chance)
    attack_damage = player_class["Attack"] / random.randint(1, 8)
    attack_damage_rounded = round(attack_damage, 2)
    creature_health = creature["Health"] - attack_damage_rounded
    if creature_health >= 1:
        print(f"You delt {attack_damage_rounded} damage. The creature has {creature_health} health left")
    else:
        print(f"You delt {attack_damage_rounded} damage. The creature is dead!")


# Create ASCII art for the word "ABYSS"
main_title = pyfiglet.figlet_format("ABYSS")

# Print the ASCII art
print(main_title)

# Player Classes & Class Stats
barbarian = {"Title": "Barbarian", "Health": 200, "Magic": 0, "Agility": 80, "Attack": 80, "Weapon": "Axe"}
mage = {"Title": "Mage", "Health": 80, "Magic": 200, "Agility": 100, "Attack": 60, "Weapon": "Staff"}
ranger = {"Title": "Ranger", "Health": 120, "Magic": 0, "Agility": 180, "Attack": 50, "Weapon": "Bow"}
assassin = {"Title": "Assassin", "Health": 100, "Magic": 80, "Agility": 200, "Attack": 40, "Weapon": "Dagger"}

# Set Player Name
print("What is your name?")
player_name = input("> ")

# Set Player Class
print("What is your class?")
print("1. Barbarian")
print("2. Mage")
print("3. Ranger")
print("4. Assassin")
player_class = int(input("> "))

while player_class != 1 and player_class != 2 and player_class != 3 and player_class != 4:
    print("Invalid Choice. Please select a valid class.")
    print("1. Barbarian")
    print("2. Mage")
    print("3. Ranger")
    print("4. Assassin")
    player_class = int(input("> "))

if player_class == 1:
    player_class = barbarian
elif player_class == 2:
    player_class = mage
elif player_class == 3:
    player_class = ranger
elif player_class == 4:
    player_class = assassin


print(f"Player Name: {player_name}")
print(f"You have chosen the {player_class["Title"]} class with the following stats:")
print(f"Health: {player_class["Health"]}, Magic: {player_class["Magic"]}, Agility: {player_class["Agility"]}")
#time.sleep(5)

# Create ASCII art for the word "The Forest"
forest_title = pyfiglet.figlet_format("The Forest")

# Print ASCII Forest Title
print(forest_title)
#time.sleep(3)

print("You awaken and find yourself in a large meadow surrounded by trees.")
#time.sleep(5)
print("The sun is high in the sky. Birds are chirping, and you can feel a light breeze.")
#time.sleep(5)
print("You look around you and find a small bag. You can feel some items inside.")
#time.sleep(5)
print(f"Opening it up, you find a small empty container, a {player_class["Weapon"]}, and a flint & steel.")
#time.sleep(5)

player_attack(player_class, goblin)

