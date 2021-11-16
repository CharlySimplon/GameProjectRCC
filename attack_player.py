
def attack_p (pv_ennemi,pa_player):
    if pv_ennemi <= pa_player:
        print("Filicitation,Vous avez réussi à vaincre l'ennemi!") 
        return "Filicitation,Vous avez réussi à vaincre l'ennemi!"
    else:
        pv_ennemi -= pa_player
        return pv_ennemi