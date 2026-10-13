"""Fonctions : remplacer les `...` par votre code."""


# Exercice 1 : construire une fonction simple et réutilisable.
def convertir_minutes_en_secondes(minutes: int) -> int:
    return minutes * 60


def test_convertir_minutes_en_secondes():

    assert convertir_minutes_en_secondes(1) == 60
    assert convertir_minutes_en_secondes(5) == 300
    assert convertir_minutes_en_secondes(0) == 0


# Exercice 2 : une fonction pour chaque responsabilité.
def calculer_aire_rectangle(longueur: float, largeur: float) -> float:
    return longueur * largeur


def calculer_perimetre_rectangle(longueur: float, largeur: float) -> float:
    return 2 * (longueur + largeur)


# hint: longueur x largeur
def test_calculer_aire_rectangle():
    assert calculer_aire_rectangle(5.0, 3.0) == 15.0
    assert calculer_aire_rectangle(2.5, 2.0) == 5.0


# hint: 2x(longeur + largeur)
def test_calculer_perimetre_rectangle():
    assert calculer_perimetre_rectangle(5.0, 3.0) == 16.0
    assert calculer_perimetre_rectangle(2.5, 2.0) == 9.0


# Exercice 3 : `return` doit fournir le résultat, pas seulement l'afficher.
def construire_message_bienvenue(prenom: str) -> str:
    return f"Bienvenue {prenom} !"


def test_construire_message_bienvenue():
    resultat = construire_message_bienvenue("Ada")

    assert resultat == "Bienvenue Ada !"
    assert isinstance(resultat, str)


# Exercice 4 : découper un calcul en petites fonctions.
def calculer_sous_total(prix_unitaire: float, quantite: int) -> float:
    sous_total = prix_unitaire * quantite
    return sous_total


def calculer_tva(sous_total: float, taux_tva: float) -> float:
    return sous_total * taux_tva


def calculer_total(prix_unitaire: float, quantite: int, taux_tva: float) -> float:
    # Votre code doit réutiliser calculer_sous_total() et calculer_tva().
    sous_total = calculer_sous_total(prix_unitaire=prix_unitaire, quantite=quantite)
    tva = calculer_tva(
        sous_total=sous_total,
        taux_tva=taux_tva,
    )

    total = sous_total + tva

    return total


def test_calculer_sous_total():
    assert calculer_sous_total(12.5, 4) == 50.0


def test_calculer_tva():
    assert calculer_tva(50.0, 0.2) == 10.0


# Exercice 5 : accepter plusieurs arguments positionnels avec *args.
def additionner(*nombres: float) -> float:
    return sum(nombres)


def test_additionner_avec_args():
    assert additionner(2.0, 3.0) == 5.0
    assert additionner(1.0, 2.0, 3.0, 4.0) == 10.0

    valeurs = [10.0, 20.0, 5.0]
    assert additionner(*valeurs) == 35.0


# Exercice 6 : accepter plusieurs arguments nommés avec **kwargs.
def creer_profil(**informations: str) -> dict[str, str]:
    return {"nom": informations["nom"], "langage": informations["langage"]}


def test_creer_profil_avec_kwargs():

    attendu = {
        "nom": "Ada",
        "langage": "Python",
    }

    # Remplacez `...` par deux arguments nommés.
    resultat = creer_profil(nom="Ada", langage="Python")

    assert attendu == resultat
