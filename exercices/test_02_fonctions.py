"""Fonctions : remplacer les `...` par votre code."""


# Exercice 1 : construire une fonction simple et réutilisable.
def convertir_minutes_en_secondes(minutes: int) -> int: ...


def test_convertir_minutes_en_secondes():
    assert convertir_minutes_en_secondes(1) == 60
    assert convertir_minutes_en_secondes(5) == 300
    assert convertir_minutes_en_secondes(0) == 0


# Exercice 2 : une fonction pour chaque responsabilité.
def calculer_aire_rectangle(longueur: float, largeur: float) -> float: ...


def calculer_perimetre_rectangle(longueur: float, largeur: float) -> float: ...


# hint: longueur x largeur
def test_calculer_aire_rectangle():
    assert calculer_aire_rectangle(5.0, 3.0) == 15.0
    assert calculer_aire_rectangle(2.5, 2.0) == 5.0


# hint: 2x(longeur + largeur)
def test_calculer_perimetre_rectangle():
    assert calculer_perimetre_rectangle(5.0, 3.0) == 16.0
    assert calculer_perimetre_rectangle(2.5, 2.0) == 9.0


# Exercice 3 : `return` doit fournir le résultat, pas seulement l'afficher.
def construire_message_bienvenue(prenom: str) -> str: ...


def test_construire_message_bienvenue():
    resultat = construire_message_bienvenue("Ada")

    assert resultat == "Bienvenue Ada !"
    assert isinstance(resultat, str)


# Exercice 4 : découper un calcul en petites fonctions.
def calculer_sous_total(prix_unitaire: float, quantite: int) -> float: ...


def calculer_tva(sous_total: float, taux_tva: float) -> float: ...


def calculer_total(prix_unitaire: float, quantite: int, taux_tva: float) -> float:
    # Votre code doit réutiliser calculer_sous_total() et calculer_tva().
    ...


def test_calculer_sous_total():
    assert calculer_sous_total(12.5, 4) == 50.0


def test_calculer_tva():
    assert calculer_tva(50.0, 0.2) == 10.0


def test_calculer_total(monkeypatch):
    appels = {"sous_total": 0, "tva": 0}

    def faux_sous_total(prix_unitaire: float, quantite: int) -> float:
        appels["sous_total"] += 1
        return 50.0

    def fausse_tva(sous_total: float, taux_tva: float) -> float:
        appels["tva"] += 1
        return 10.0

    monkeypatch.setattr(
        __name__ + ".calculer_sous_total",
        faux_sous_total,
    )
    monkeypatch.setattr(__name__ + ".calculer_tva", fausse_tva)

    assert calculer_total(12.5, 4, 0.2) == 60.0
    assert appels == {"sous_total": 1, "tva": 1}


# Exercice 5 : accepter plusieurs arguments positionnels avec *args.
def additionner(*nombres: float) -> float: ...


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
    resultat = creer_profil(...)

    assert attendu == resultat
