from deplacment import choix

print("Bienvenue sur le jeu : 'Simplon Escape' !")
print("Le but du jeu est de sauver la princesse Claire emprisonnée en haut du donjon Simplon.co. \nVous êtes le Héros de cette quête et partez à la rescousse de la princesse. \nVous aurez à affronter de nombreux ennemis au cours de votre ascension dans le donjon.")

defi = input("-----------\nEtes-vous prêt(e) à relever ce défi ? (Y/N) ")
playing = True
while playing:
        
    if defi.lower() == "n":
        playing = False
        print("Votre décision est lourde de conséquences. Claire restera dans son donjon pour le restant de ses jours...\n Ouste péant ! Reviens quand tu seras un peu plus valeureux !")
        
    elif defi.lower() == "y":
        print("Votre bravoure vous honore ! Et ce sacrifice quasi certain restera à jamais dans les livres d'histoire...")
        player_name = str(input("Mais au fait, quel est ton nom, jeune aventurier(ère) ? "))
        print("{} dis-tu... Ca reviendra certainement un jour à la mode.".format(player_name))
        print("Trêve de bavardages ! Il est temps pour toi de te confronter au plus grand défi de ta vie...")
        print("--- ENTREE DU DONJON ---")
        floor = 0
        potion = 3
        hp_player = 50
        max_hp_player = 50
        attack_player = 5
        choix()
        break
    
    else:
        defi = str(input("Toi pas comprendre ? Y or N ? "))


