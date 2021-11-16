import pytest
import mock



from deplacment import choix
from attack_player import attack_p

def test_choix(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : "f")
    assert choix("f") == "Nous ne comprenons pas votre choix, veuillez saisir n'importe quelle lettre de a, b, c, d selon les options"
    # with mock.patch.object(__builtins__, 'input', lambda: 'f'):
    #     assert choix("f") == "Nous ne comprenons pas votre choix, veuillez saisir n'importe quelle lettre de a, b, c, d selon les options"
    # with mock.patch.object(__builtins__, 'input', lambda: 'd'):
    #     assert choix("d") == "au revoir"

    # assert choix("d") == print("au revoir")
    assert choix("a") == 0.1
    assert choix("b") == 0.3
    assert choix("c") == 0.5
    # assert choix("f") ==  print("Nous ne comprenons pas votre choix, veuillez saisir n'importe quelle lettre de a, b, c, d selon les options")

    #  with pytest.raises(TypeError) : choix(1)

def test_attack_p():
    assert attack_p(20,20) == "Filicitation,Vous avez réussi à vaincre l'ennemi!"
    assert attack_p(20,5) == 15