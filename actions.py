def attack_ennemy(defense,hp_player,force_ennemy):
    """This function takes away health points from life's player when an ennemy attacks him."""
    if defense != 0 :
        force_ennemy_with_defense = round(force_ennemy / 1.5)
        defense -= 1
        hp_player -= force_ennemy_with_defense
        print("Vous avez subi {} points de dégâts".format(force_ennemy_with_defense))

    else:    
        hp_player -= force_ennemy
        print("Vous avez subi {} points de dégâts".format(force_ennemy))

    print(f'Il vous reste {hp_player}PV')
    return hp_player 


def attack_p (hp_ennemy,attack_player):
    """This function takes away health points from life's ennemy when the player attacks."""
    if hp_ennemy <= attack_player:
        print("Filicitation,Vous avez réussi à vaincre l'ennemi!") 
        return 0
    else:
        print(f'Il reste {hp_ennemy} PV à l\'ennemi')
        return hp_ennemy - attack_player


def defense_player(defense):
    """This function give a shield to the player during 3 turns."""
    if defense !=0 :
        print("Tu as déjà un bouclier !")
    else:
        defense = 3
        print("Te voilà équipé d'un bouclier pendant 3 tours !")
    return defense
    

def drink_potion(players_hp, potion, max_hp_player):
    """This function gives back 20 HP to the player in battle."""
    if players_hp < max_hp_player -20:
        players_hp += 20
    else:
        players_hp = max_hp_player
    potion -= 1
    print(f'-------Vous avez maintenant {potion} potions et {players_hp}PV')
    return players_hp, potion