"""Control flow : booléens, conditions, pattern matching et boucle while."""
from typing import Literal


# Exercice 1 : combiner des conditions avec and, or et not.
def peut_entrer(
    age: int,
    a_un_billet: bool,
    est_accompagne: bool,
    est_interdit: bool,
) -> bool:
    # Une personne peut entrer si elle a un billet, n'est pas interdite et si
    # elle est majeure ou accompagnée.
    return a_un_billet and not est_interdit and (age >= 18 or est_accompagne)


def test_peut_entrer():
    assert peut_entrer(20, True, False, False) is True
    assert peut_entrer(16, True, True, False) is True
    assert peut_entrer(16, True, False, False) is False
    assert peut_entrer(20, False, False, False) is False
    assert peut_entrer(20, True, False, True) is False


# Exercice 2 : choisir une branche avec if, elif et else.
def classer_temperature(temperature: float) -> Literal["gel", "frais", "chaud"]:
    # Retournez "gel", "frais" ou "chaud".
    # gel : moins de 0 ; frais : moins de 20 ; chaud : à partir de 20.
    if temperature < 0:
        return "gel"
    elif temperature < 20:
        return "frais"
    else:
        return "chaud"



def test_classer_temperature():
    assert classer_temperature(-5.0) == "gel"
    assert classer_temperature(0.0) == "frais"
    assert classer_temperature(19.9) == "frais"
    assert classer_temperature(20.0) == "chaud"


# Exercice 3 : utiliser des motifs littéraux avec match.
def traduire_commande(commande: str) -> str:
    # "start" et "demarrer" donnent "Démarrage".
    # "stop" donne "Arrêt". Tout autre texte donne "Commande inconnue".
    match commande:
        case "start":
            return "Démarrage"
        case "demarrer":
            return "Démarrage"
        case "stop":
            return "Arrêt"
        case _:
            return "Commande inconnue"


def test_traduire_commande():
    assert traduire_commande("start") == "Démarrage"
    assert traduire_commande("demarrer") == "Démarrage"
    assert traduire_commande("stop") == "Arrêt"
    assert traduire_commande("pause") == "Commande inconnue"


# Exercice 4 : reconnaître la structure d'un tuple avec match.
def decrire_point(point: tuple[int, int]) -> str:
    # Distinguez l'origine, l'axe vertical, l'axe horizontal et les autres
    # points. Inspirez-vous des motifs du cours.
    match point:
        case (0, 0):
            return "origine"
        case (0, y):
            return f"axe vertical"
        case (x, 0):
            return f"axe horizontal"
        case (x, y):
            return f"autre point"


def test_decrire_point():
    assert decrire_point((0, 0)) == "origine"
    assert decrire_point((0, 4)) == "axe vertical"
    assert decrire_point((3, 0)) == "axe horizontal"
    assert decrire_point((3, 4)) == "autre point"


# Exercice 5 : construire une liste avec une boucle while.
def compter_jusqua(limite: int) -> list[int]:
    output = []
    # Pour une limite de 3, retournez [1, 2, 3].
    # hint: Vous pouvez utiliser la méthode 'output.append(<element>)' pour ajouter un élément à une liste
    compteur = 1

    while compteur < limite+1:
        output.append(compteur)
        compteur += 1

    return output

def test_compter_jusqua():
    assert compter_jusqua(1) == [1]
    assert compter_jusqua(4) == [1, 2, 3, 4]
    assert compter_jusqua(0) == []


# Exercice 6 : combiner while et if.
def trouver_premier_multiple(
    debut: int,
    fin: int,
    diviseur: int,
) -> int | None:
    # Cherchez entre debut et fin inclus. Retournez None si rien n'est trouvé.
    compteur = debut

    while compteur < fin + 1:
        reste = compteur % diviseur
        if reste == 0:
            return compteur

        compteur += 1

    return None

def test_trouver_premier_multiple():
    assert trouver_premier_multiple(10, 20, 7) == 14
    assert trouver_premier_multiple(15, 20, 7) is None
    assert trouver_premier_multiple(21, 21, 7) == 21


# Exercice 7 : appeler une fonction de manière récursive.
def factorielle(n: int) -> int | None:
    if n <= 0:
        print(f"Factorielle prend un nombre positif en entrée. Nombre donné: {n}")
        return 1
    if n == 1:
        return n
    else:
        return n*factorielle(n-1)



def test_factorielle_recursive():
    assert factorielle(0) == 1
    assert factorielle(1) == 1
    assert factorielle(3) == 6
    assert factorielle(5) == 120
