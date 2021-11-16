def choix(route="", floor=0, score=0): 
    print(f'Vous arrivez à l\'étage {floor} et votre score est de : {score}') 
    a = "a:route facile"
    b = "b:route normal"
    c = "c:route difficile" 
    d = "d:quitter le jeu" 
    difficulty = 0
     
    while route not in ["a","b","c","d"]:
        print("Vous avez le choix entre 3 routes devant vous :\n",a,b,c,d)
        route = input("Quelle route voulez-vous choisir?")
        if route == "d":
            playing = False
            return print("au revoir")
        elif route == "a":
            difficulty = 0
        elif route == "b":
            difficulty = 0.1
        elif route == "c":
            difficulty = 0.2
        else :
             print("Veuillez saisir  a, b, c ou d selon les options")

    return difficulty
    