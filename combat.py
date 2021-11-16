from attack_ennemy import attack_ennemy
from defense_player import defense_player


def battle():
    defense = 0
    while hp_player != 0 or hp_ennemy != 0:
        choice = input("1: Attaque \n2: Défendre\n3: Potion")
        if choice == "1":
            attack_ennemy()
        elif choice == "2":
            defense_player(defense)
        elif choice == "3":
            potion(hp_player, max_players_hp, potion) 