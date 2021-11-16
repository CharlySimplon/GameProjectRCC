
def attack_ennemy(defense,hp_player,force_ennemy,score):
    #This function takes away health points from life's player when an ennemy attacks him.
    if defense != 0 :
        force_ennemy_with_defense = round(force_ennemy / 1.5)
        defense -= 1
        hp_player -= force_ennemy_with_defense
        print("Vous avez subi {} points de dégâts".format(force_ennemy_with_defense))

    else:    
        hp_player -= force_ennemy
        print("Vous avez subi {} points de dégâts".format(force_ennemy))

    if hp_player <= 0 :
        playing = False
        return print("Vous mourrez dans d'atroces souffrances...Votre score est de : {} points.".format(score))
        
    else:
        return print("Il vous reste {} points de vie.".format(hp_player))
