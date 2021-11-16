def choix(route=""):  
    a = "a:route facile"
    b = "b:route normal"
    c = "c:route difficile" 
    d = "d:quitter le jeu" 
    difficulte = 0
     
    while route not in ["a","b","c","d"]:
        print("Vous avez le choix entre 3 routes devant vous :\n",a,b,c,d)
        route = input("quel route vous voulez choisser?")
        if route == "d":
            playing = False
            return print("au revoir")
        elif route == "a":
            difficulte = 0.1
        elif route == "b":
            difficulte = 0.3
        elif route == "c":
            difficulte = 0.5
        else :
             print("Veuillez saisir n'importe quelle lettre de a, b, c, d selon les options")

    return difficulte
    