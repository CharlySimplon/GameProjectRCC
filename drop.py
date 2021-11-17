from random import randint


def drop(droprate, score, score_ennemy, difficulty, floor, potion, attack_player):
    """This function allow to know if an item is won or not and to update the score depending on
    the difficulty and the ennemy"""
    value = randint(0,100)
    if difficulty == 0:
        factor = 1
    elif difficulty == 0.1:
        factor = 2
    elif difficulty == 0.2:
        factor = 3
    score += (score_ennemy * factor)
    floor += 1
    if value <= droprate : 
        print("----------------L'ennemi a laissé un objet derrière lui--------------------")
        value = randint(0, 100)
        score, attack_player, potion, floor = item(value,potion,attack_player, floor, score)
    print(f'Nouveau score : {score}')
    return score, attack_player, potion, floor

def item(value, potion, attack_player, floor, score):
    """ This function allow to attribute an equipment to a player if it is better than the ancient 
    depending on a random value"""
    dict = {"EXCALIBUR" : 50, "Hâche": 20, "Epee": 15, "Dague": 8, "Cure-dent": 2}
    if 0 < value <= 1:
        print("EXCALIBUR")
        if attack_player < 5 + dict["EXCALIBUR"]:
            attack_player = 5 + dict["EXCALIBUR"]
        else: 
            print("Votre équipement actuel est meilleur")
    elif 1 < value <= 7:
        print("Hâche")
        if attack_player < 5 + dict["Hâche"]:
            attack_player = 5 + dict["Hâche"]
        else: 
            print("Votre équipement actuel est meilleur") 
    elif 7 < value <= 15:
        print("Epee")
        if attack_player < 5 + dict["Epee"]:
            attack_player = 5 + dict["Epee"]
        else: 
            print("Votre équipement actuel est meilleur")
    elif 15 < value <= 30:
        print("Dague")
        if attack_player < 5 + dict["Dague"]:
            attack_player = 5 + dict["Dague"]
        else: 
            print("Votre équipement actuel est meilleur")
    elif 30 < value <= 50:
        print("Cure-dent")
        if attack_player < 5 + dict["Cure-dent"]:
            attack_player = 5 + dict["Cure-dent"]
        else: 
            print("Votre équipement actuel est meilleur")
    else:
        print("Potion")
        if potion < 5:
            potion += 1
    return score, attack_player, potion, floor
    
    
     