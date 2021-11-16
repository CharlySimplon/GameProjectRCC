import pytest
import main
from main import play
from main import start

def test_play(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : "n")
    assert play("test") == print("Votre décision est lourde de conséquences. Claire restera dans son donjon pour le restant de ses jours...\n Ouste péant ! Reviens quand tu seras un peu plus valeureux !")

# def test_play():
    # assert play(Y) == print("Votre bravoure vous honore ! Et ce sacrifice quasi certain restera à jamais dans les livres d'histoire...") 
    # assert play(N) == print("Votre décision est lourde de conséquences. Claire restera dans son donjon pour le restant de ses jours...\n Ouste péant ! Reviens quand tu seras un peu plus valeureux !")

# def test_start():
#     assert start()


