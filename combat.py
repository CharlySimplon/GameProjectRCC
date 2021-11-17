from actions import defense_player, drink_potion, attack_ennemy, attack_p
from drop import drop


def battle(hp_player, hp_ennemy, potion, droprate,force_ennemy, score, score_ennemy, difficulty, floor, attack_player):
    defense = 0
    while hp_player > 0 and hp_ennemy > 0:
        choice = input("1: Attaque \n2: Défendre\n3: Potion\n")
        if choice == "1":
            hp_ennemy = attack_p(hp_ennemy,attack_player)
        elif choice == "2":
            defense = defense_player(defense)
        elif choice == "3":
            if potion >= 1:
                hp_player, potion = drink_potion(hp_player, 50, potion)
            else: 
                pass
        if hp_ennemy != 0:
            hp_player = attack_ennemy(defense,hp_player,force_ennemy)
    if hp_player == 0:
        playing = False
        pass

    score, attack_player, potion, floor = drop(droprate, score, score_ennemy, difficulty, floor, potion, attack_player)
    return hp_player, score, attack_player, potion, floor