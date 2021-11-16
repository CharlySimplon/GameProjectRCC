from combat import battle

def summon_monster(floor,difficulty):
    # This function give the force and the health points of the ennemy, using the floor's level and the difficulty's level.
    force_base = 5
    hp_base_ennemy = 25
    score_ennemy = 10
    force_ennemy = round(force_base + ((floor/10)+difficulty) * force_base)
    hp_ennemy = round(hp_base_ennemy + ((floor/10)+difficulty) * hp_base_ennemy)
    print("Vous venez d'invoquer un monstre avec {} points de vie et avec une force de {}.".format(hp_ennemy,force_ennemy))
    battle(hp_ennemy,force_ennemy,score_ennemy)

    return "Vie {}, Force {}".format(hp_ennemy,force_ennemy)