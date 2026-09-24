"""Premiers exercices : remplacer les `...` par votre code."""


def test_afficher_un_message(capsys):
    # Votre code : affichez exactement "Bonjour Ada !"
    ...

    # Assert
    sortie = capsys.readouterr().out
    assert sortie == "Bonjour Ada !\n"


def test_inspecter_des_variables():
    # Given
    entier = 42
    decimal = 3.14
    texte = "Python"
    booleen = True

    # Votre code : remplacez chaque `...` par le bon type.
    # Posez aussi un breakpoint ici et inspectez les quatre variables.
    assert type(entier) is ...
    assert type(decimal) is ...
    assert type(texte) is ...
    assert type(booleen) is ...


def test_operations_numeriques():
    # Votre code
    division = ...
    division_entiere = ...
    reste = ...
    puissance = ...

    # Asserts
    assert division == 3.5
    assert division_entiere == 3
    assert reste == 1
    assert puissance == 49


def test_operations_sur_les_textes():
    # Given
    debut = "Py"
    fin = "thon"

    # Votre code
    langage = ...
    rire = ...

    # Asserts
    assert langage == "Python"
    assert rire == "hahaha"


def test_operations_sur_les_booleens():
    # Given
    prof_est_sympa = True
    je_prefere_sas = False

    add_result = prof_est_sympa + je_prefere_sas
    mult_result = prof_est_sympa * je_prefere_sas

    # Asserts - complétez les ...
    assert add_result == ...
    assert mult_result == ...
    assert type(add_result) is ...
    assert type(mult_result) is ...


"""Imports, erreurs et saisie utilisateur."""

import pytest


def test_importer_une_fonction():
    # Votre code : importez sqrt depuis le module math.
    ...

    # Assert : remplacez `...` par un appel à sqrt.
    assert ... == 3


def test_comprendre_une_erreur_de_type():
    # Quelle type d'erreur cette opération retourne t-elle ? hint: executer la commande hors du test pour voir.
    with pytest.raises(...):
        "3" + 2


def test_corriger_une_erreur_de_type():
    # Given
    nombre_saisi = "3"

    # Votre code : obtenez le nombre 5 avec une conversion et une addition.
    resultat = ...

    # Assert
    assert resultat == 5
    assert type(resultat) is int


def test_lire_une_saisie(monkeypatch):
    # Pytest simule la saisie de l'utilisateur.
    monkeypatch.setattr("builtins.input", lambda message: "Ada")

    # Votre code : appelez input() avec la question "Ton prénom ? ".
    prenom = ...

    # Assert
    assert prenom == "Ada"


def test_int_conversion():
    age_str = "12"

    # Votre code : Convertissez age_str et ajouter 1.
    age_annee_prochaine = ...

    # Assert
    assert age_annee_prochaine == 13


def test_boolean_conversion():
    ma_str = "J'adore le cours de python"

    assert bool(ma_str) == ...


def test_str_conversion():
    age = 27

    # Votre code : str converted doit contenir la chaîne: "J'ai 27 ans"
    str_converted = ...

    assert str_converted == "J'ai 27 ans"
