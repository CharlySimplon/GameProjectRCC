from combat import battle

def summon_monster(hp_player, potion, floor,difficulty, attack_player,score, playing):
    # This function give the force and the health points of the ennemy, using the floor's level and the difficulty's level.
    force_base = 5
    hp_base_ennemy = 25
    droprate_base = 10

    score_ennemy = 10
    droprate = droprate_base * (((floor/10)+difficulty)+1)
    force_ennemy = round(force_base + ((floor/10)+difficulty) * force_base)
    hp_ennemy = round(hp_base_ennemy + ((floor/10)+difficulty) * hp_base_ennemy)
    print("Vous venez d'invoquer un monstre avec {} points de vie et avec une force de {}.".format(hp_ennemy,force_ennemy))
   
    hp_player, score, attack_player, potion, floor, playing = battle(hp_player,hp_ennemy,potion,droprate, force_ennemy,score,score_ennemy,difficulty,floor,attack_player,playing)
    return hp_player, score, attack_player, potion, floor, playing
