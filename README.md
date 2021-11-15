# GameProjectRCC

TEST

Projet Jeu R-C-C

Instructions : 
Ouvrez dans votre IDE le fichier main.py du dossier puis le lancer.

Contexte :
Le but du jeu est de sauver la princesse Claire emprisonnée en haut du donjon Simplon.co. Vous êtes le Héros de cette quête et partez à la rescousse de la princesse. Vous aurez à affronter de nombreux ennemis au cours de votre ascension dans le donjon. 

Déroulement :
Ce donjon se présente sous la forme d'une tour avec plusieurs étages (Floor), eux-mêmes composés de 3 chemins (Easy, Normal, Hard). Plus la difficulté choisie est élevée, plus votre score final le sera également. A chaque étage, après avoir déterminé le chemin que vous souhaitez emprunter, vous affronterez un ennemi plus au moins fort selon votre étage et le chemin choisi. Les ennemis auront une faible chance de vous droper un objet (arme, potion) à leur mort. Si vos points de vie atterissent à 0, vous perdez la partie et votre score sera enregistré. A chaque étage, vous aurez le choix de continuer ou de quitter le jeu sur ce score.

Déroulement du combat :
Il se déroule en tour par tour dans lequel vous avez l'initiative. Vous aurez alors le choix entre attaquer, défendre ou utiliser une potion. L'ennemi quant à lui attaquera toujours à la fin de votre tour. 
Attaquer : Inflige des dégats à l'ennemi (% coup critique)
Défendre : Limite les dégats infligés par l'ennemi pendant plusieurs tours
Potion : Permet de récupérer des Points de Vie