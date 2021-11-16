import pytest
from potion import potion
from drop import drop,item

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
