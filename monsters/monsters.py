def creature_attack(creature):
    if creature["Attack"] < player_class["Health"]:
        player_class["Health"] = player_class["Health"] - creature["Attack"]
        print(player_class["Health"])
    else:
        print("You are dead")

# Humanoid Creatures
goblin = {"Title": "Goblin", "Health": 40, "Magic": 0, "Agility": 20, "Attack": 20,}
orc = {"Title": "Orc", "Health": 100, "Magic": 0, "Agility": 80}
troll = {"Title": "Troll", "Health": 300, "Magic": 0, "Agility": 15}

# Undead Monsters
zombie = {"Title": "Zombie", "Health": 40, "Magic": 0, "Agility": 20, "Disease": 40}
skeleton = {"Title": "Skeleton", "Health": 80, "Magic": 0, "Agility": 80}
vampire = {"Title": "Vampire", "Health": 150, "Magic": 100, "Agility": 150, "Disease": 80}
ghost = {"Title": "Ghost", "Health": 80, "Magic": 0, "Agility": 200}

# Beasts
wolf = {"Title": "Wolf", "Health": 80, "Magic": 0, "Agility": 100}
dire_wolf = {"Title": "Dire Wolf", "Health": 120, "Magic": 0, "Agility": 120}
werewolf = {"Title": "Werewolf", "Health": 200, "Magic": 0, "Agility": 200}
boar = {"Title": "Boar", "Health": 100, "Magic": 0, "Agility": 80}
rat = {"Title": "Rat", "Health": 20, "Magic": 0, "Agility": 100}
basilisk = {"Title": "Basilisk", "Health": 80, "Magic": 0, "Agility": 150, "Poison": 150}

