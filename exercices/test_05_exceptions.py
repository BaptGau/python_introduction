"""Exceptions : remplacer les `...` par votre code."""

import pytest


# Exercice 1 : traiter uniquement une erreur de conversion.
def convertir_entier(texte: str) -> int | None:
    # Retournez l'entier, ou None si int() lève une ValueError.
    ...


def test_convertir_entier():
    assert convertir_entier("42") == 42
    assert convertir_entier("-5") == -5
    assert convertir_entier("bonjour") is None


# Exercice 2 : attraper une exception précise.
def diviser(dividende: float, diviseur: float) -> float | None:
    # Retournez None uniquement en cas de ZeroDivisionError.
    ...


def test_diviser():
    assert diviser(10, 2) == 5
    assert diviser(10, 0) is None

    # Une TypeError inattendue doit continuer à remonter.
    with pytest.raises(TypeError):
        diviser("dix", 2)


# Exercice 3 : signaler une valeur invalide avec raise.
def valider_age(age: int) -> int:
    # Levez ValueError si l'âge n'est pas compris entre 0 et 130 inclus.
    # Sinon, retournez l'âge.
    ...


def test_valider_age():
    assert valider_age(0) == 0
    assert valider_age(42) == 42
    assert valider_age(130) == 130

    with pytest.raises(ValueError, match="entre 0 et 130"):
        valider_age(-1)

    with pytest.raises(ValueError, match="entre 0 et 130"):
        valider_age(131)


# Exercice 4 : utiliser except, else et finally.
def convertir_avec_journal(texte: str, journal: list[str]) -> int | None:
    # En cas d'échec, ajoutez "erreur" au journal et retournez None.
    # En cas de succès, ajoutez "succes" et retournez l'entier.
    # Dans tous les cas, ajoutez ensuite "fin" avec finally.
    ...


def test_convertir_avec_journal():
    journal_succes = []
    assert convertir_avec_journal("12", journal_succes) == 12
    assert journal_succes == ["succes", "fin"]

    journal_erreur = []
    assert convertir_avec_journal("Ada", journal_erreur) is None
    assert journal_erreur == ["erreur", "fin"]
