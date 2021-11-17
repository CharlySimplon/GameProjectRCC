import pytest
from actions import drink_potion, attack_ennemy, attack_p, defense_player
from drop import drop,item
from deplacment import choix



def test_drink_potion():
    assert drink_potion(50, 2, 100) == (70, 1)
    assert drink_potion(80, 3, 100) == (100, 2)
    assert drink_potion(40, 4, 100) == (60, 3)
    assert drink_potion(90, 2, 110) == (110, 1)
    assert drink_potion(85, 3, 90) == (90, 2)


def test_drop():
    # score, attack_player, potion, floor, playing
    #assert drop(droprate, score, score_ennemy, difficulty, floor, potion, attack_player, playing,value = randint(0,100)) == 
    assert drop(20, 50,60,0.1,80,3,2,True,66) == (170, 2, 3, 81, True)
    # assert drop(20, 50,60,0.1,80,3,2,True,18) == (170, 2, 3, 81, True)
    # assert drop(20, 50,60,0.1,80,3,2,True,66) == (170, 2, 3, 81, True)
    # assert drop(20, 50,60,0.1,80,3,2,True,66) == (170, 2, 3, 81, True)

def test_item():
   # assert item(value, potion, attack_player, floor, score, playing) 
    assert item(2, 30, 1, 50, True,10) == (50,30,2,1,True)
    assert item(2, 25, 2, 100, True,1) == (100,55,2,2,True)
    assert item(3, 5,10, 0,False,51) == (0,5,4,10,False)
    assert item(5, 5,10, 0,False,51) == (0,5,5,10,False)
"""
def test_choix(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : "f")
    assert choix("f") == 
    assert choix("a") == 
    assert choix("b") == 
    assert choix("c") == 
"""

def test_attack_p():
    assert attack_p(20,20) == 0
    assert attack_p(20,5) == 15
    assert attack_p(25,7) == 18
    assert attack_p(20,60) == 0


def test_attack_ennemy():
    assert attack_ennemy(0,20,10) ==  10 #recoit un coup sans defense
    assert attack_ennemy(1,20,10) ==  13 #recoit un coup avec defense
    assert attack_ennemy(0,10,0) ==  10 #recoit un coup égale à 0 sans défense
    assert attack_ennemy(2,10,0) ==  10 #recoit un coup égale à 0 avec défense

def test_defense_player():
    assert defense_player(0) == 3 #met un bouclier
    assert defense_player(2) == 2 #refuse de mettre un bouclier car déjà équipé
    assert defense_player(1) == 1 #refuse de mettre un bouclier car déjà équipé