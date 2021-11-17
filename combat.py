from actions import defense_player, drink_potion, attack_ennemy, attack_p
from drop import drop


def battle(hp_player, hp_ennemy, potion, droprate,force_ennemy, score, score_ennemy, difficulty, floor, attack_player, playing):
    defense = 0
    while hp_player > 0 and hp_ennemy > 0:
        choice = input("1: Attaque \n2: Défendre\n3: Potion\n")
        if choice == "1":
            # Appel de la fonction attack_p du fichier actions
            hp_ennemy = attack_p(hp_ennemy,attack_player)
        elif choice == "2":
            # Appel de la fonction defense_player du fichier actions
            defense = defense_player(defense)
        elif choice == "3":
            if potion >= 1:
                # Appel de la fonction drink_potion du fichier actions
                hp_player, potion = drink_potion(hp_player,potion, max_hp_player=50)
            else: 
                pass
        if hp_ennemy != 0:
            # Appel de la fonction attack_ennemy du fichier actions
            hp_player = attack_ennemy(defense,hp_player,force_ennemy)
            
    if hp_player <= 0:
        # Fin de la partie, retour sur main
        playing = False
        pass
    else:
        # Appel de la fonction drop du fichier drop
        score, attack_player, potion, floor, playing = drop(droprate, score, score_ennemy, difficulty, floor, potion, attack_player, playing)
        # Retour sur la fonction summon_monster du fichier summon_monster
    return hp_player, score, attack_player, potion, floor, playing