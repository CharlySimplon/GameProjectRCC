
def attack_p (hp_ennemy,attack_player):
    if hp_ennemy <= attack_player:
        print("Filicitation,Vous avez réussi à vaincre l'ennemi!") 
        return "Filicitation,Vous avez réussi à vaincre l'ennemi!"
    else:
        hp_ennemy -= attack_player
        return hp_ennemy