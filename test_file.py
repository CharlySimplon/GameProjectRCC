import pytest
from potion import potion
from drop import drop,item
from deplacment import choix
from attack_player import attack_p
from attack_ennemy import attack_ennemy
from defense_player import defense_player


def test_potion():
    assert potion(50, 100, 2) == print("+20 PV ========> ",70)
    assert potion(80, 100, 3) == print("+20 PV ========> ",100)
    assert potion(40, 100, 4) == print("+20 PV ========> ",60)
    assert potion(90, 100, 2) == print("+20 PV ========> ",100)
    assert potion(85, 100, 3) == print("+20 PV ========> ",100)

def test_drop():
    assert drop(20, 30, 50, 10, 0) == print('Nouveau score : 60')
    assert drop(20, 30, 50, 20, 0.1) == print('Nouveau score : 90')
    assert drop(20, 30, 50, 30, 0.2) == print('Nouveau score : 140')
    assert drop(20, 50, 50, 20, 0) == print('Nouveau score : 70')
    assert drop(20, 21, 80, 10, 0.2) == print('Nouveau score : 110')

def test_item():
    assert item(10, 2, 20) == print("Votre équipement actuel est meilleur")
    assert item(10 ,2, 30) == print("Votre équipement actuel est meilleur")
    assert item(1, 2, 25) == 55
    assert item(51, 3, 5) == 4

def test_choix(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : "f")
    assert choix("f") == "Nous ne comprenons pas votre choix, veuillez saisir n'importe quelle lettre de a, b, c, d selon les options"
    assert choix("a") == 0.1
    assert choix("b") == 0.3
    assert choix("c") == 0.5


def test_attack_p():
    assert attack_p(20,20) == "Filicitation,Vous avez réussi à vaincre l'ennemi!"
    assert attack_p(20,5) == 15

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