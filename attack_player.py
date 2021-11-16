
def attack_p (hp_ennemy,attack_player):
    if hp_ennemy <= attack_player:
        print("Filicitation,Vous avez réussi à vaincre l'ennemi!") 
        return "Félicitation,Vous avez réussi à vaincre l'ennemi!"
    else:
        hp_ennemy -= attack_player
    print(f'Il reste {hp_ennemy} PV à l\'ennemi')
    # return hp_ennemy