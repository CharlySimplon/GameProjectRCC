import pytest
from attack_ennemy import attack_ennemy
from defense_player import defense_player

def test_attack_ennemy():
    assert attack_ennemy(0,20,10,50) == print("Il vous reste {} points de vie.".format(10)) #recoit un coup sans defense
    assert attack_ennemy(1,20,10,50) == print("Il vous reste {} points de vie.".format(13)) #recoit un coup avec defense
    assert attack_ennemy(0,10,0,50) == print("Il vous reste {} points de vie.".format(10)) #recoit un coup égale à 0 sans défense
    assert attack_ennemy(2,10,0,50) == print("Il vous reste {} points de vie.".format(10)) #recoit un coup égale à 0 avec défense

    assert attack_ennemy(0,5,10,50) == print("Vous mourrez dans d'atroces souffrances...Votre score est de : {} points.".format(50)) #meurt sans défense
    assert attack_ennemy(2,5,10,60) == print("Vous mourrez dans d'atroces souffrances...Votre score est de : {} points.".format(60)) #meurt avec défense

def test_defense_player():
    assert defense_player(0) == print("Te voilà équipé d'un bouclier pendant 3 tours !") #met un bouclier
    assert defense_player(2) == print("Tu as déjà un bouclier !") #refuse de mettre un bouclier car déjà équipé