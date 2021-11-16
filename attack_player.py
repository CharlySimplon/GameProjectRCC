
def attack_p (pv_ennemi,pa_player):
     #This function takes away health points from enemy life's e when an player attacks him.
     # if health points of enemy less then point attack of player, payer will win.
    if pv_ennemi <= pa_player:
        print("Filicitation,Vous avez réussi à vaincre l'ennemi!") 
        return "Filicitation,Vous avez réussi à vaincre l'ennemi!"
    else:
        pv_ennemi -= pa_player
        return pv_ennemi