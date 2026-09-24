# Les fonctions

Une fonction est un bloc de code **nommé**, **réutilisable** et chargé d'un
rôle précis.

```python
def convertir_minutes_en_secondes(minutes: int) -> int:
    return minutes * 60


duree = convertir_minutes_en_secondes(5)
```

```text
paramètre                  valeur retournée
    ↓                           ↑
minutes → [ convertir en secondes ] → secondes
```

## Pourquoi créer des fonctions ?

- **Découper** un problème complexe en petites responsabilités ;
- **réutiliser** le même code sans le copier ;
- **lire** le programme comme une suite d'actions nommées ;
- **tester** chaque comportement séparément.

## Une fonction = un rôle

```python
def calculer_sous_total(prix: float, quantite: int) -> float:
    return prix * quantite


def calculer_tva(sous_total: float, taux: float) -> float:
    return sous_total * taux


def calculer_total(sous_total: float, tva: float) -> float:
    return sous_total + tva
```

Chaque fonction répond à une seule question. Le programme principal assemble
ces petites briques.

```python
sous_total = calculer_sous_total(10.0, 3)
tva = calculer_tva(sous_total, 0.2)
total = calculer_total(sous_total, tva)
```

Si une fonction calcule, affiche, demande une saisie **et** sauvegarde une
valeur, elle a probablement trop de responsabilités. Découper ne signifie pas
créer une fonction pour chaque ligne : chaque fonction doit porter une action
claire et utile.

## Bien nommer et typer

Difficile à comprendre :

```python
def f(a, b):
    return a * b
```

Plus clair :

```python
def calculer_sous_total(prix_unitaire: float, quantite: int) -> float:
    return prix_unitaire * quantite
```

Les annotations indiquent les valeurs attendues :

```text
                         argument         retour
                            ↓              ↓
def doubler(nombre: int) -> int:
    return nombre * 2
```

Python **ne vérifie pas ces types automatiquement pendant l'exécution**.
Ils servent de documentation et aident PyCharm à signaler des erreurs avant
de lancer le programme.

```python
def doubler(nombre: int) -> int:
    return nombre * 2


doubler("ha")  # Python l'accepte et renvoie "haha" malgré l'annotation int
```

## `return` n'est pas `print`

```python
def additionner(a: int, b: int) -> int:
    return a + b


resultat = additionner(2, 3)  # resultat vaut 5
print(resultat)                # affiche 5
```

- `return` transmet une valeur au code qui appelle la fonction ;
- `print` affiche du texte et retourne `None`.

Une fonction sans `return` explicite retourne aussi `None`.

## Paramètres et arguments

Les **paramètres** sont les noms déclarés par la fonction. Les **arguments**
sont les valeurs fournies au moment de l'appel.

```python
def saluer(prenom: str, message: str = "Bonjour") -> str:
    return message + " " + prenom


saluer("Ada")                         # argument positionnel
saluer(prenom="Ada", message="Salut")  # arguments nommés
```

Un paramètre avec une valeur par défaut devient optionnel. Les paramètres
obligatoires se placent avant ceux qui ont une valeur par défaut.

## `*args` : plusieurs arguments positionnels

`*args` rassemble un nombre variable d'arguments positionnels dans un tuple.

```python
def additionner(*nombres: float) -> float:
    return sum(nombres)


additionner(2, 3)        # nombres vaut (2, 3)
additionner(2, 3, 4, 5)  # nombres vaut (2, 3, 4, 5)
```

Dans `*nombres: float`, l'annotation `float` décrit chaque argument reçu, pas
le tuple complet.

Le nom `args` est une convention, mais c'est l'étoile `*` qui donne ce
comportement. Un nom plus précis comme `*nombres` est souvent plus lisible.

## `**kwargs` : plusieurs arguments nommés

`**kwargs` rassemble un nombre variable d'arguments nommés dans un dictionnaire.

```python
def creer_profil(**informations: str) -> dict[str, str]:
    return informations


profil = creer_profil(nom="Ada", langage="Python")
# informations vaut {"nom": "Ada", "langage": "Python"}
```

Dans `**informations: str`, l'annotation `str` décrit chaque valeur du
dictionnaire. Ses clés sont toujours des chaînes de caractères.

Le nom `kwargs` signifie *keyword arguments* et n'est lui aussi qu'une
convention. Les deux étoiles `**` sont importantes.

## Déballer une collection lors d'un appel

Les mêmes symboles permettent l'opération inverse lors de l'appel :

```python
nombres = [2, 3, 4]
additionner(*nombres)  # identique à additionner(2, 3, 4)

donnees = {"nom": "Ada", "langage": "Python"}
creer_profil(**donnees)  # identique aux deux arguments nommés
```

Préférer des paramètres explicites quand leur nombre et leur rôle sont connus.
Utiliser `*args` ou `**kwargs` quand la fonction doit réellement accepter un
nombre variable d'arguments.

## Variables locales

Les paramètres et variables créés dans une fonction sont **locaux** :

```python
def construire_message(prenom: str) -> str:
    message = "Bonjour " + prenom
    return message


# `message` n'existe pas ici.
```

Préférer les paramètres aux variables globales rend une fonction plus simple
à comprendre, réutiliser et tester.
