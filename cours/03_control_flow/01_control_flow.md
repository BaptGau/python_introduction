# Control flow : booléens, conditions et boucles

Un booléen représente deux états : `True` ou `False`. Il permet au programme
de prendre une décision.

## Comparer des valeurs

```python
age = 20

age == 20  # égal à
age != 20  # différent de
age < 20   # inférieur à
age <= 20  # inférieur ou égal à
age > 20   # supérieur à
age >= 20  # supérieur ou égal à
```

Attention : `=` affecte une valeur, tandis que `==` compare deux valeurs.

Les comparaisons peuvent être enchaînées :

```python
age = 20
18 <= age < 65  # identique à : age >= 18 and age < 65
```

## Opérateurs logiques

```text
and  → toutes les conditions doivent être vraies
or   → au moins une condition doit être vraie
not  → inverse le résultat
```

```python
age = 20
a_un_billet = True
est_interdit = False

peut_entrer = age >= 18 and a_un_billet and not est_interdit
```

Ordre de priorité : `not`, puis `and`, puis `or`. Utiliser des parenthèses
quand elles rendent l'intention plus claire.

```python
peut_entrer = a_un_billet and (age >= 18 or est_accompagne)
```

### Évaluation courte

Python s'arrête dès que le résultat est connu :

```python
diviseur = 0
calcul_possible = diviseur != 0 and 10 / diviseur > 2
```

La division n'est jamais exécutée ici, car la première condition est `False`.

## Valeurs vraies et fausses

Une condition accepte autre chose qu'un `bool`. Sont notamment considérés
comme faux :

```python
False
None
0
0.0
""
[]
{}
```

Les autres valeurs sont généralement considérées comme vraies.

```python
nom = "Ada"

if nom:  # plus naturel que : if nom != ""
    print("Un nom a été fourni")
```

`bool(valeur)` permet d'observer la valeur booléenne correspondante.

## `if`, `elif`, `else`

```python
temperature = 18

if temperature < 0:
    print("Il gèle")
elif temperature < 20:
    print("Il fait frais")
else:
    print("Il fait chaud")
```

Python utilise `elif`, et non `elsif` ou `else if`.

```text
if condition 1 ? ── oui ─▶ bloc 1
       │ non
       ▼
elif condition 2 ? ─ oui ─▶ bloc 2
       │ non
       ▼
else ───────────────────▶ bloc 3
```

Une seule branche est exécutée. L'ordre est donc important : placer les cas
les plus précis avant les cas plus généraux.

## `match` et les motifs

`match` compare une valeur à une suite de **motifs** (*patterns*). Le premier
motif compatible est exécuté.

```python
def traduire_commande(commande: str) -> str:
    match commande:
        case "start" | "demarrer":
            return "Démarrage"
        case "stop":
            return "Arrêt"
        case _:
            return "Commande inconnue"
```

- `"stop"` est un motif littéral ;
- `"start" | "demarrer"` accepte l'un des deux motifs ;
- `_` accepte tout ce qui n'a pas déjà correspondu.

Le pattern matching peut aussi reconnaître la **structure** d'une valeur :

```python
def decrire_point(point: tuple[int, int]) -> str:
    match point:
        case (0, 0):
            return "origine"
        case (0, y):
            return f"axe vertical, y={y}"
        case (x, 0):
            return f"axe horizontal, x={x}"
        case (x, y):
            return f"point x={x}, y={y}"
```

Dans un motif, `x` et `y` **capturent** les valeurs. Un nom seul ne compare pas
avec une variable existante : il capture le cas rencontré.

Une garde ajoute une condition au motif :

```python
match point:
    case (x, y) if x == y:
        print("Le point est sur la diagonale")
    case _:
        print("Autre point")
```

Utiliser `if` pour des conditions générales et `match` lorsque plusieurs cas
dépendent surtout de la valeur ou de la structure d'un objet.

## La boucle `while`

`while` répète un bloc **tant que** sa condition est vraie.

```python
compteur = 1

while compteur <= 3:
    print(compteur)
    compteur += 1
```

```text
tester la condition ── fausse ─▶ sortir de la boucle
         │
       vraie
         ▼
   exécuter le bloc
         │
         └─────────────────────┘
```

La condition doit pouvoir devenir fausse. Sinon, la boucle ne s'arrête jamais.

```python
while True:
    commande = input("Commande : ")

    if commande == "stop":
        break     # quitte immédiatement la boucle

    if commande == "":
        continue  # passe directement au tour suivant

    print(commande)
```

- `break` quitte la boucle ;
- `continue` ignore la fin du tour actuel ;
- mettre à jour les variables de la condition évite les boucles infinies.

Une boucle doit elle aussi avoir une responsabilité claire. Si son contenu
devient long, extraire les différentes actions dans des fonctions.

## Les fonctions récursives

Une fonction est **récursive** lorsqu'elle s'appelle elle-même pour résoudre
une version plus petite du même problème.

Elle a besoin de deux parties :

1. un **cas de base**, qui arrête les appels ;
2. un **cas récursif**, qui se rapproche du cas de base.

```python
def fibonacci(position: int) -> int:
    if position == 0:              # cas de base
        return 0
    if position == 1:              # cas de base
        return 1

    return fibonacci(position - 1) + fibonacci(position - 2)  # cas récursif
```

```text
fibonacci(4)
├─ fibonacci(3)
│  ├─ fibonacci(2)
│  │  ├─ fibonacci(1) → 1
│  │  └─ fibonacci(0) → 0
│  └─ fibonacci(1) → 1
└─ fibonacci(2)
   ├─ fibonacci(1) → 1
   └─ fibonacci(0) → 0

résultat : fibonacci(4) = 3
```

Chaque appel attend le résultat du suivant et occupe de la mémoire dans la
pile d'appels. Sans cas de base, ou si le problème ne s'en rapproche jamais,
Python finit par produire une `RecursionError`.

Cette version de Fibonacci recalcule plusieurs fois les mêmes positions : on
voit par exemple deux appels à `fibonacci(2)`. Elle illustre bien la récursion,
mais une boucle serait plus efficace pour effectuer ce calcul.

La récursion est pratique pour des structures naturellement imbriquées comme
des dossiers ou des arbres. Pour une simple répétition, une boucle est souvent
plus lisible et ne risque pas de dépasser la limite de récursion de Python.
