# Collections : organiser des données

Une collection regroupe plusieurs valeurs. Le bon type dépend de ce que l'on
veut faire : conserver un ordre, retrouver rapidement une clé, supprimer les
doublons ou produire les valeurs progressivement.

| Type       | Ordonné             | Doublons     | Mutable     | Usage principal                |
| ---------- | ------------------- | ------------ | ----------- | ------------------------------ |
| `list`     | oui                 | oui          | oui         | suite modifiable               |
| `tuple`    | oui                 | oui          | non         | suite fixe                     |
| `dict`     | ordre d'insertion   | clés uniques | oui         | associer clés et valeurs       |
| `set`      | non garanti         | non          | oui         | unicité et appartenance        |
| `str`      | oui                 | oui          | non         | texte                          |
| générateur | ordre de production | oui          | consommable | valeurs calculées à la demande |

## Deux organisations en mémoire

Les schémas suivants simplifient le fonctionnement habituel de **CPython**.
Ce sont des détails d'implémentation, pas des obligations du langage Python.

### Tableau de références : `list` et `tuple`

Une liste est un tableau dynamique. Ses cases sont côte à côte en mémoire,
mais elles contiennent des **références** vers les objets, pas directement les
objets.

```python
valeurs = [10, "Ada", True]
```

```text
objet list
┌──────────┬──────────┬──────────┐
│ référence │ référence │ référence │  cases contiguës
└─────┬───└─────┬───└─────┬───┘
     │             │             │
     ▼             ▼             ▼
     10           "Ada"          True      objets ailleurs en mémoire
```

Une `list` garde souvent quelques cases libres pour rendre les futurs
`append()` rapides. Elle peut donc occuper un peu plus de place que son contenu.

```
allocation_mémoire = nouvelle_taille + nouvelle_taille/8 + (3 if nouvelle_taille < 9 else 6)
```

Un `tuple` utilise aussi un tableau de références, mais sa taille est fixée à
la création. Il n'a pas besoin de réserver de cases pour grandir.

### Table de hachage : `dict` et `set`

Une table de hachage utilise une fonction de hash pour traduire une valeur en
un index dans un tableau de références.

```python
ages = {"Ada": 36, "Guido": 69}
```

```text
"Ada" ─▶ hash("Ada") ─▶ index 2 ─▶ référence vers ("Ada", 36)
```

La fonction cherche à bien répartir les valeurs entre les index. Deux valeurs
peuvent malgré tout produire le même index : c'est une **collision**. Python
cherche alors une autre case disponible.

- un `dict` associe chaque clé à une valeur ;
- un `set` stocke uniquement des valeurs uniques ;
- les deux utilisent un tableau plus grand que leur nombre d'éléments.

```text
tableau plus grand + cases parfois vides → davantage de mémoire
accès direct grâce à l'index          → recherche en O(1) en moyenne
```

Ce `O(1)` est une moyenne, pas une garantie absolue. Une clé de dictionnaire ou
une valeur de set doit aussi être **hashable** : son hash ne doit pas changer.
Une `str` ou un tuple d'éléments hashables convient ; une `list` mutable ne
convient pas.

## Fragmentation de la mémoire

Les objets Python peuvent avoir des tailles et des durées de vie différentes.
Quand certains sont supprimés, ils peuvent laisser des espaces libres entre
les objets encore utilisés.

```text
avant : [ objet A ][ objet B ][ objet C ][ objet D ]
après : [ objet A ][  espace  ][ objet C ][  espace  ]
```

C'est la **fragmentation**. CPython réutilise beaucoup de ces espaces pour de
futurs objets, mais ne rend pas forcément immédiatement toute cette mémoire au
système.

Conséquences possibles :

- le programme peut garder plus de mémoire que la taille de ses données utiles ;
- suivre des références vers des objets dispersés utilise moins bien le cache du
  processeur ;
- copier de grandes collections consomme temporairement du temps et de la
  mémoire supplémentaires.

Pour un programme débutant, choisir la collection adaptée est plus important
que chercher à contrôler manuellement la mémoire.

## `list` : une suite modifiable

```python
noms: list[str] = ["Ada", "Guido"]
noms.append("Grace")
noms[0] = "Ada Lovelace"
dernier = noms[-1]
```

Opérations courantes :

```python
len(noms)  # nombre d'éléments
"Ada" in noms  # test d'appartenance
noms.remove("Guido")
copie = noms.copy()
```

Une affectation ne copie pas la liste :

```python
copie = noms  # même objet
copie = noms.copy()  # nouvelle liste
```

## `tuple` : une suite fixe

```python
point: tuple[int, int] = (10, 20)
x, y = point
```

On ne peut ni ajouter, ni retirer, ni remplacer une case du tuple. Un tuple
peut toutefois contenir un objet mutable :

```python
donnees = ("nombres", [1, 2])
donnees[1].append(3)  # la liste contenue reste mutable
```

Un tuple est hashable seulement si tous ses éléments le sont.

## `dict` : associer une clé à une valeur

```python
utilisateur: dict[str, str] = {
    "nom": "Ada",
    "langage": "Python",
}

utilisateur["pays"] = "Royaume-Uni"
nom = utilisateur["nom"]
pays = utilisateur.get("pays", "Inconnu")
```

Depuis Python 3.7, un dictionnaire conserve l'ordre d'insertion de ses clés.
L'accès se fait par clé, pas par position.

## `set` : des valeurs uniques

```python
langages: set[str] = {"Python", "Java", "Python"}
print(langages)  # Python n'apparaît qu'une fois
```

```python
backend = {"Python", "Go", "Java"}
data = {"Python", "R", "Julia"}

backend & data  # intersection : {"Python"}
backend | data  # union
backend - data  # différence
```

L'ordre d'itération d'un set n'est pas une garantie sur laquelle s'appuyer.
Pour créer un set vide, utiliser `set()` : `{}` crée un dictionnaire vide.

## `str` : une séquence immutable

Une chaîne est une séquence de caractères Unicode.

```python
langage = "Python"
langage[0]  # "P"
langage[1:4]  # "yth"
len(langage)  # 6
```

Une `str` est immutable. Ses méthodes renvoient donc de nouvelles chaînes :

```python
nom = "  ada lovelace  "
nom_propre = nom.strip().title()

print(nom)  # "  ada lovelace  "
print(nom_propre)  # "Ada Lovelace"
```

Concaténer de nombreuses chaînes avec `+` crée de nombreux objets
intermédiaires. Pour assembler beaucoup de morceaux, préférer `"".join(...)`.

## Parcourir une collection avec `for`

`for` prend successivement chaque valeur d'un objet itérable :

```python
noms = ["Ada", "Guido", "Grace"]

for nom in noms:
    print(nom)
```

Pour parcourir un dictionnaire :

```python
for cle, valeur in utilisateur.items():
    print(cle, valeur)
```

Utiliser `while` quand la répétition dépend d'une condition. Utiliser `for`
quand on veut parcourir les valeurs d'un objet itérable.

## Les compréhensions

Une compréhension construit une collection à partir d'un objet itérable, en
une expression courte.

### Compréhension de liste

```python
nombres = [1, 2, 3, 4, 5]
carres_pairs = [nombre**2 for nombre in nombres if nombre % 2 == 0]

# [4, 16]
```

Elle correspond à cette boucle :

```python
carres_pairs = []

for nombre in nombres:
    if nombre % 2 == 0:
        carres_pairs.append(nombre**2)
```

### Compréhension de dictionnaire

```python
noms = ["Ada", "Guido", "Grace"]
longueurs = {nom: len(nom) for nom in noms}

# {"Ada": 3, "Guido": 5, "Grace": 5}
```

### Expression génératrice, ou compréhension génératrice

```python
carres = (nombre**2 for nombre in nombres)
```

Les parenthèses créent ici un générateur : les valeurs sont calculées à la
demande. Les crochets d'une compréhension de liste créent immédiatement toutes
les valeurs.

```text
[expression for valeur in iterable]  → list
{cle: valeur for valeur in iterable} → dict
(expression for valeur in iterable)  → generator
```

Une compréhension doit rester facile à lire. Si elle accumule plusieurs
conditions ou transformations, préférer une boucle ou une fonction nommée.

## Générateur : produire à la demande

Une fonction qui contient `yield` crée un générateur. Elle produit une valeur,
met son exécution en pause, puis reprend au prochain appel.

```python
from collections.abc import Iterator


def compter(limite: int) -> Iterator[int]:
    nombre = 1

    while nombre <= limite:
        yield nombre
        nombre += 1
```

```python
nombres = compter(3)  # aucun nombre n'est encore produit
next(nombres)  # 1
next(nombres)  # 2
```

```text
list  : stocke toutes les valeurs       → plus de mémoire, réutilisable
generator : garde seulement son état  → peu de mémoire, consommé une fois
```

Un générateur est utile pour une grande quantité de données ou une suite
potentiellement infinie. Il échange souvent un peu de temps d'exécution contre
une forte réduction de la mémoire utilisée.

## Mutabilité : le mémo

```text
mutables   : list, dict, set
immutables : tuple, str, int, float, bool, None

générateur : objet avec un état interne qui avance et se consomme
```

Les objets mutables peuvent être modifiés par toutes les variables qui les
référencent. Les objets immutables ne changent pas : une opération produit un
nouvel objet.
