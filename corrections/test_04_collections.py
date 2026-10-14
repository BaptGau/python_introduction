"""Collections : remplacer les `...` par votre code."""

from collections.abc import Iterator


# Exercice 1 : copier une liste avant de la modifier.
def copier_et_ajouter(elements: list[str], nouvel_element: str) -> list[str]:
    # Retournez une nouvelle liste sans modifier `elements`.
    copied_list = elements.copy()
    copied_list.append(nouvel_element)
    return copied_list


def test_copier_et_ajouter():
    origine = ["Ada", "Guido"]
    resultat = copier_et_ajouter(origine, "Grace")

    assert resultat == ["Ada", "Guido", "Grace"]
    assert origine == ["Ada", "Guido"]
    assert resultat is not origine


# Exercice 2 : lire et construire des tuples.
def calculer_centre(
    point_a: tuple[float, float],
    point_b: tuple[float, float],
) -> tuple[float, float]:
    return (
        (point_a[0] + point_b[0]) / 2,
        (point_a[1] + point_b[1]) / 2,
    )


def test_calculer_centre():
    assert calculer_centre((0.0, 0.0), (4.0, 2.0)) == (2.0, 1.0)
    assert calculer_centre((-2.0, 4.0), (2.0, 8.0)) == (0.0, 6.0)


# Exercice 3 : utiliser un dictionnaire comme table de comptage.
def compter_occurrences(mots: list[str]) -> dict[str, int]:
    compteur = {}

    for mot in mots:
        compteur[mot] = compteur.get(mot, 0) + 1

    return compteur


def test_compter_occurrences():
    assert compter_occurrences(["python", "java", "python", "go"]) == {
        "python": 2,
        "java": 1,
        "go": 1,
    }
    assert compter_occurrences([]) == {}


# Exercice 4 : utiliser les opérations d'ensemble.
def trouver_competences_communes(
    equipe_a: set[str],
    equipe_b: set[str],
) -> set[str]:
    return equipe_a & equipe_b


def test_trouver_competences_communes():
    backend = {"Python", "Go", "Java"}
    data = {"Python", "R", "SQL"}

    assert trouver_competences_communes(backend, data) == {"Python"}
    assert trouver_competences_communes({"Rust"}, {"Python"}) == set()


# Exercice 5 : les méthodes de str créent une nouvelle chaîne.
def normaliser_identifiant(texte: str) -> str:
    # Retirez les espaces aux extrémités, passez en minuscules et remplacez
    # les espaces restants par des underscores.
    return texte.strip().lower().replace(" ", "_")


def test_normaliser_identifiant():
    origine = "  Ada Lovelace  "
    resultat = normaliser_identifiant(origine)

    assert resultat == "ada_lovelace"
    assert origine == "  Ada Lovelace  "


# Exercice 6 : produire les nombres pairs sans construire de liste.
def generer_nombres_pairs(maximum: int) -> Iterator[int]:
    # Utilisez `yield`. Le maximum est inclus s'il est pair.
    for nombre in range(maximum + 1):
        reste = nombre % 2
        if reste == 0:
            yield nombre


def test_generer_nombres_pairs():
    nombres = generer_nombres_pairs(6)

    assert iter(nombres) is nombres
    assert next(nombres) == 0
    assert next(nombres) == 2
    assert list(nombres) == [4, 6]
    assert list(generer_nombres_pairs(1)) == [0]


# Exercice 7 : construire une liste avec une compréhension.
def calculer_carres_pairs(nombres: list[int]) -> list[int]:
    return [nombre**2 for nombre in nombres if not nombre % 2]
    # [<variable finale> for <variable> in <reference> if <filtre>]
    # {key: valeur for <variable> in <reference> if <filtre>]
    # (<variable finale> for <variable> in <reference> if <filtre>)


def test_calculer_carres_pairs():
    assert calculer_carres_pairs([1, 2, 3, 4, 5]) == [4, 16]
    assert calculer_carres_pairs([]) == []


# Exercice 8 : construire un dictionnaire avec une compréhension.
def calculer_longueurs(mots: list[str]) -> dict[str, int]:
    return {mot: len(mot) for mot in mots}


def test_calculer_longueurs():
    assert calculer_longueurs(["Ada", "Python", "Go"]) == {
        "Ada": 3,
        "Python": 6,
        "Go": 2,
    }


# Exercice 9 : retourner une expression génératrice.
def generer_majuscules(mots: list[str]) -> Iterator[str]:
    return (mot.upper() for mot in mots)


def test_generer_majuscules():
    resultat = generer_majuscules(["Ada", "Python"])

    assert iter(resultat) is resultat
    assert next(resultat) == "ADA"
    assert list(resultat) == ["PYTHON"]


# Exercice 10 : Inverser une collection.
def inverse(elements: list[str]) -> list[str]:
    # Retournez une nouvelle liste inversant 'elements'. en utilisant les compréhensions.
    return [elements[i] for i in range(len(elements) - 1, -1, -1)]


def test_inverse():
    origine = ["Ada", "Lovelace", "Grace"]
    resultat = inverse(origine)

    assert resultat == ["Grace", "Lovelace", "Ada"]
