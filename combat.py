from attack_ennemy import attack_ennemy
from defense_player import defense_player
from attack_player import attack_p
from drop import drop
from potions import drink_potion
from random import randint


def battle(hp_player, hp_ennemy, potion, droprate,force_ennemy, score, score_ennemy, difficulty, floor, attack_player):
    defense = 0
    while hp_player != 0 or hp_ennemy != 0:
        choice = input("1: Attaque \n2: Défendre\n3: Potion")
        if choice == "1":
            attack_p(hp_ennemy,attack_player)
        elif choice == "2":
            defense_player(defense)
        elif choice == "3":
            drink_potion(hp_player, max_players_hp=50, potion=potion)
        if hp_ennemy != 0:
            attack_ennemy(defense,hp_player,force_ennemy)
    if hp_player == 0:
        playing = False

    
    drop(droprate, score, score_ennemy, difficulty, floor, potion, attack_player) 