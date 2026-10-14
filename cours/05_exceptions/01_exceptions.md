# Exceptions : traiter les erreurs

Une **exception** signale qu'une opération ne peut pas se terminer normalement.

```python
int("bonjour")  # ValueError
10 / 0  # ZeroDivisionError
```

Python utilise les mots-clés `try` et `except`.

## Lire le traceback

```text
Traceback (most recent call last):
  File "programme.py", line 4, in <module>
    age = int("Ada")
ValueError: invalid literal for int()
```

Lire de bas en haut :

1. `ValueError` : le type de l'exception ;
2. le message : une explication ;
3. les fichiers, fonctions et lignes traversés.

Une `SyntaxError` empêche généralement le programme de commencer. Les autres
exceptions apparaissent pendant l'exécution.

## `try` et `except`

Placer dans `try` uniquement l'opération susceptible d'échouer :

```python
texte = input("Âge : ")

try:
    age = int(texte)
except ValueError:
    print("L'âge doit être un entier.")
```

Si `int()` réussit, le bloc `except` est ignoré. Si `int()` lève une
`ValueError`, Python interrompt le bloc `try` et exécute le bloc correspondant.

On peut traiter plusieurs erreurs différemment :

```python
try:
    resultat = nombres[index]
except IndexError:
    print("Cet index n'existe pas.")
except TypeError:
    print("L'index doit être un entier.")
```

Ou regrouper plusieurs types :

```python
except (ValueError, TypeError):
    print("Valeur incorrecte.")
```

## Récupérer l'exception

`as` permet d'accéder à l'objet exception et à son message :

```python
try:
    age = int("Ada")
except ValueError as erreur:
    print("Conversion impossible :", erreur)
```

## `else` et `finally`

```python
try:
    age = int(texte)
except ValueError:
    print("Conversion impossible")
else:
    print("Conversion réussie :", age)
finally:
    print("Fin de la tentative")
```

```text
try     → tente l'opération
except  → s'exécute si l'exception correspond
else    → s'exécute si aucune exception n'a été levée
finally → s'exécute toujours
```

`finally` sert notamment à libérer une ressource ou terminer une action de
nettoyage. Éviter d'y placer un `return` : il peut masquer une exception ou un
résultat précédent.

## Lever une exception avec `raise`

Le programme peut signaler lui-même une valeur invalide :

```python
def calculer_prix_ttc(prix_ht: float, taux: float) -> float:
    if prix_ht < 0:
        raise ValueError("Le prix ne peut pas être négatif.")

    return prix_ht * (1 + taux)
```

`return` fournit un résultat normal. `raise` interrompt le chemin normal et
signale que la fonction ne peut pas fournir de résultat valide.

Choisir un type précis :

```text
ValueError         bonne famille de type, mais valeur invalide
TypeError          type de valeur incompatible
KeyError           clé absente d'un dictionnaire
IndexError         index absent d'une séquence
ZeroDivisionError  division par zéro
FileNotFoundError  fichier introuvable
```

## Propagation

Si une fonction ne traite pas une exception, celle-ci remonte vers la fonction
qui l'a appelée.

```text
main() → charger_age() → int("Ada") lève ValueError
  ▲          │
  └─────────┘  l'exception remonte jusqu'à un except compatible
```

Une fonction ne doit traiter une exception que si elle sait quoi en faire.
Sinon, il vaut mieux la laisser remonter.

Pour effectuer une action puis relancer la même exception :

```python
try:
    charger_donnees()
except ValueError:
    print("Chargement impossible")
    raise
```

## Bonnes pratiques

```python
# Trop large : masque aussi des erreurs de programmation inattendues.
try:
    resultat = calculer()
except Exception:
    pass
```

Préférer :

- attraper uniquement les exceptions que l'on sait traiter ;
- garder le bloc `try` court ;
- ne jamais utiliser `except:` sans type dans le code courant ;
- ne pas ignorer une exception sans explication ;
- utiliser une condition pour un cas normal et une exception pour un cas
  exceptionnel ;
- conserver un message utile dans chaque `raise`.
