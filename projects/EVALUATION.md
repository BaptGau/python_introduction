# Évaluation finale — Une machine virtuelle typée

Ce projet est le projet sur lequel vous serez évalués.

## Modalités

**Groupe : entre 1 et 3 personnes**  
**Date de rendu : 20/12/2026**

Le projet doit être rendu de l'une des manières suivantes :

- envoyer un mail à `baptiste.gautier@univ-paris1.fr` avec le projet au format
  `.zip` en pièce jointe ;
- envoyer par mail un lien vers le dépôt Git du projet ;
- ajouter `@BaptGau` au projet Git et envoyer par mail le lien du dépôt.

Le mail doit préciser les noms des membres du groupe.

## Avant de rendre

1. relire tous les scénarios de validation à la fin du sujet ;
2. vérifier qu'ils fonctionnent réellement ;
3. formater le code avec :

```bash
uv run ruff format
```

4. ouvrir une dernière fois les fichiers rendus pour vérifier qu'ils sont
   complets et qu'ils s'exécutent.

## Barème — 20 points

### Code fonctionnel — 10 points

Les classes, les instructions, la pile et les opérations demandées doivent
fonctionner. Les scénarios de validation servent de référence.

La correction utilisera aussi quelques programmes non communiqués dans le
sujet. Il ne faut donc pas écrire une solution qui fonctionne uniquement avec
les exemples fournis.

### Optimisation et lisibilité — 5 points

Cette partie évalue notamment :

- l'utilisation du bon outil au bon endroit : enum, dataclass, liste, union de
  types, méthode ou fonction ;
- des noms explicites et des annotations de type utiles ;
- des méthodes courtes avec une responsabilité claire ;
- l'absence de duplication inutile ;
- un code formaté et facile à relire.
- le principe de "moindre surprise".

Il n'est pas nécessaire de chercher des optimisations complexes. Une solution
simple, cohérente et lisible est préférable.

### Usage de l'IA — 5 points

Le barème s'inspire du
[framework 0RWX](https://0rwx.com/) :

- **ZER0** — travail réalisé sans IA : `5/5` ;
- **READ** — l'IA conseille ou inspire, mais ne modifie pas le projet et le
  groupe écrit le code : `5/5` ;
- **WRITE** — l'IA produit ou modifie une partie du code, mais le groupe relit,
  comprend et corrige le résultat : entre `1/5` et `4/5` selon le niveau de
  maîtrise démontré ;
- **EXECUTE** — projet entièrement produit par l'IA, que le groupe n'est pas
  capable de lire, d'expliquer ou de corriger : `0/5`.

Utiliser une IA n'est donc pas interdit. Toutefois, cette partie du barême vise à récompenser le travail fait à la main.

## Objectif

Inspiré de ce [livre](https://createlang.rs/01_calculator/vm.html).

Construire une petite machine virtuelle capable d'exécuter une suite
d'instructions.

La machine manipule trois types de valeurs :

- des nombres ;
- des textes ;
- des booléens.

Elle utilise une **pile** : les valeurs sont ajoutées et retirées à la fin
d'une liste avec `append()` et `pop()`.

```text
programme → instruction suivante → opération sur la pile → résultat
```

Le projet mobilise les notions vues en cours :

- listes et pile LIFO ;
- conditions, boucles et `match` ;
- exceptions ;
- enums, classes et dataclasses ;
- unions de types et annotations ;
- séparation des responsabilités.

## 1. Les valeurs de la VM

La pile ne contient pas directement des `float`, `str` ou `bool`. Chaque type
est représenté par une dataclass.

### `Nombre`

```python
@dataclass
class Nombre:
    valeur: float
```

Dans `__post_init__()` :

- accepter un `int` ou un `float`, mais pas un `bool` ;
- convertir la valeur en `float` ;
- lever `TypeError("Un nombre est attendu.")` pour une autre valeur.

Exemples :

```python
Nombre(2).valeur  # 2.0
Nombre(2.5).valeur  # 2.5
Nombre(True)  # TypeError
Nombre("deux")  # TypeError
```

### `Texte`

```python
@dataclass
class Texte:
    valeur: str
```

Une valeur qui n'est pas une chaîne lève :

```python
TypeError("Un texte est attendu.")
```

### `Booleen`

```python
@dataclass
class Booleen:
    valeur: bool
```

Seuls `True` et `False` sont acceptés. Une autre valeur lève :

```python
TypeError("Un booléen est attendu.")
```

### Union des valeurs

Créer l'union suivante :

```python
type Valeur = Nombre | Texte | Booleen
```

## 2. Les codes d'opération

Créer un enum `CodeOperation` contenant huit opérations :

| Opération           | Effet                                      |
| ------------------- | ------------------------------------------ |
| `CHARGER_CONSTANTE` | empiler une constante du programme         |
| `ADDITION`          | additionner ou concaténer deux valeurs     |
| `SOUSTRACTION`      | soustraire deux nombres                    |
| `MULTIPLICATION`    | multiplier deux nombres                    |
| `DIVISION`          | diviser deux nombres                       |
| `EGAL`              | comparer deux valeurs                      |
| `NON`               | inverser un booléen                        |
| `RETIRER`           | retirer le sommet et mémoriser le résultat |

Les valeurs internes de l'enum sont libres. Elles doivent simplement être
uniques.

## 3. La dataclass `Instruction`

Une instruction contient :

```text
code     : CodeOperation
operande : int | None
```

Seule l'opération `CHARGER_CONSTANTE` attend un opérande. Cet entier représente
la position de la constante à charger.

Exemple :

```python
Instruction(CodeOperation.CHARGER_CONSTANTE, 0)
Instruction(CodeOperation.ADDITION)
```

Dans `__post_init__()` :

- `CHARGER_CONSTANTE` doit recevoir un entier positif ou nul ;
- les autres opérations doivent avoir `None` comme opérande ;
- une instruction invalide lève `ValueError("Opérande invalide.")`.

## 4. La dataclass `Programme`

Un programme contient :

```text
instructions : list[Instruction]
constantes   : list[Valeur]
```

La table des constantes peut contenir plusieurs types :

```python
[
    Nombre(2),
    Nombre(3),
    Texte("Python"),
    Booleen(True),
]
```

Dans `__post_init__()` :

- vérifier que chaque instruction est une `Instruction` ;
- vérifier que chaque constante est un `Nombre`, un `Texte` ou un `Booleen` ;
- copier les deux listes avec `.copy()` afin que le programme ne dépende pas
  ensuite des listes fournies par l'appelant.

Erreurs attendues :

```python
TypeError("Instruction invalide.")
TypeError("Constante invalide.")
```

## 5. La classe `MachineVirtuelle`

La machine contient :

```text
programme        : Programme
pile_valeurs     : list[Valeur]
dernier_resultat : Valeur | None
```

La pile est vide et le dernier résultat vaut `None` à la création de la
machine.

La machine possède quatre méthodes principales.

### `empiler()`

Ajouter une valeur à la fin de la pile avec `append()`.

### `depiler()`

Retirer et retourner la dernière valeur avec `pop()`.

Si la pile est vide, lever :

```python
IndexError("Pile de valeurs vide.")
```

### `executer_instruction()`

Recevoir une `Instruction`, appliquer son opération et modifier la pile ou le
dernier résultat.

Utiliser `match` sur le code de l'instruction.

Toutes les opérations binaires doivent dépiler dans cet ordre :

```python
droite = self.depiler()
gauche = self.depiler()
```

Cet ordre est important pour la soustraction et la division.

### `executer()`

À chaque appel, la méthode doit :

1. vider la pile ;
2. remettre `dernier_resultat` à `None` ;
3. parcourir les instructions dans leur ordre avec une boucle `for` ;
4. appeler `executer_instruction()` pour chaque instruction ;
5. vérifier qu'un résultat a été produit ;
6. vérifier que la pile est vide ;
7. retourner le dernier résultat.

Si aucun résultat n'a été produit ou si la pile contient encore des valeurs à
la fin, lever :

```python
ValueError("Programme incomplet.")
```

Le même objet `MachineVirtuelle` doit pouvoir être exécuté deux fois.

## 6. Comportement des opérations

### Charger une constante

`CHARGER_CONSTANTE` récupère la valeur située à l'index donné et l'empile.

Un index inexistant lève :

```python
IndexError("Constante introuvable.")
```

### Addition

Deux combinaisons sont acceptées :

```text
Nombre(a) + Nombre(b) → Nombre(a + b)
Texte(a)  + Texte(b)  → Texte(a + b)
```

Exemples :

```text
Nombre(2) + Nombre(3)   → Nombre(5)
Texte("Py") + Texte("thon") → Texte("Python")
```

### Opérations numériques

`SOUSTRACTION`, `MULTIPLICATION` et `DIVISION` acceptent uniquement deux
`Nombre`.

La division par zéro lève :

```python
ZeroDivisionError("Division par zéro.")
```

### Égalité

`EGAL` compare deux valeurs et empile un `Booleen` :

```text
Nombre(2) == Nombre(2) → Booleen(True)
Texte("a") == Texte("b") → Booleen(False)
Nombre(1) == Texte("1") → Booleen(False)
```

### Négation booléenne

`NON` accepte uniquement un `Booleen` :

```text
Booleen(True)  → Booleen(False)
Booleen(False) → Booleen(True)
```

### Retirer un résultat

`RETIRER` dépile une valeur et la place dans `dernier_resultat`.

Un programme peut contenir plusieurs instructions `RETIRER`. Le dernier
résultat retiré devient le résultat retourné par `executer()`.

### Types incompatibles

Une opération recevant un mauvais type lève :

```python
TypeError(f"Types incompatibles pour {instruction.code.name}.")
```

Une opération refusée ne doit pas empiler de résultat incorrect.

## 7. Exemples obligatoires

### Calcul : `(2 + 3) * 4`

Constantes :

```python
[Nombre(2), Nombre(3), Nombre(4)]
```

Instructions :

```text
CHARGER_CONSTANTE 0
CHARGER_CONSTANTE 1
ADDITION
CHARGER_CONSTANTE 2
MULTIPLICATION
RETIRER
```

Résultat : `Nombre(20)`.

### Concaténation de texte

Constantes :

```python
[Texte("Py"), Texte("thon")]
```

Instructions :

```text
CHARGER_CONSTANTE 0
CHARGER_CONSTANTE 1
ADDITION
RETIRER
```

Résultat : `Texte("Python")`.

### Comparaison et négation

Constantes :

```python
[Nombre(2), Nombre(3)]
```

Instructions :

```text
CHARGER_CONSTANTE 0
CHARGER_CONSTANTE 1
EGAL
NON
RETIRER
```

Résultat : `Booleen(True)`.

## 8. Scénarios de validation

Vérifiez bien tous les scénarios avant de rendre le projet :

1. `Nombre(2)` contient la valeur `2.0` ;
2. `Nombre(True)`, `Texte(2)` et `Booleen(1)` sont refusés ;
3. une instruction avec un opérande interdit est refusée ;
4. charger une constante place la bonne valeur au sommet de la pile ;
5. `(2 + 3) * 4` produit `Nombre(20)` ;
6. `10 - 3` produit `Nombre(7)` dans le bon ordre ;
7. `8 / 2` produit `Nombre(4)` ;
8. une division par zéro lève la bonne exception ;
9. `Texte("Py") + Texte("thon")` produit `Texte("Python")` ;
10. additionner un nombre et un texte est refusé ;
11. l'égalité de deux valeurs produit le bon booléen ;
12. `NON` inverse un booléen et refuse les autres types ;
13. dépiler une pile vide lève la bonne exception ;
14. charger un index inconnu lève la bonne exception ;
15. un programme sans résultat ou avec des valeurs restantes est refusé ;
16. le même objet machine peut être exécuté deux fois avec le même résultat ;
17. les listes fournies au programme ne sont pas modifiées par l'exécution.

La correction porte sur les valeurs retournées et les exceptions, pas sur des
textes affichés dans le terminal.

## Contraintes de qualité

- annoter tous les paramètres et toutes les valeurs de retour ;
- utiliser les noms proposés dans le sujet ;
- utiliser une liste comme pile avec `append()` et `pop()` ;
- utiliser `match` pour exécuter une instruction ;
- ne pas utiliser de variable globale modifiable ;
- ne pas utiliser d'héritage ;
- ne pas masquer les erreurs avec `except Exception` ;
- ne pas modifier les instructions ou les constantes pendant l'exécution ;
- ne pas installer de package supplémentaire.

## Aide — interfaces possibles

Cette interface est une aide, pas une obligation. Vous pouvez adapter le
découpage tant que tous les comportements demandés sont respectés.

```python
from dataclasses import dataclass, field
from enum import Enum


@dataclass
class Nombre:
    valeur: float

    def __post_init__(self) -> None: ...


@dataclass
class Texte:
    valeur: str

    def __post_init__(self) -> None: ...


@dataclass
class Booleen:
    valeur: bool

    def __post_init__(self) -> None: ...


type Valeur = Nombre | Texte | Booleen


class CodeOperation(Enum):
    CHARGER_CONSTANTE = "charger_constante"
    ADDITION = "addition"
    SOUSTRACTION = "soustraction"
    MULTIPLICATION = "multiplication"
    DIVISION = "division"
    EGAL = "egal"
    NON = "non"
    RETIRER = "retirer"


@dataclass
class Instruction:
    code: CodeOperation
    operande: int | None = None

    def __post_init__(self) -> None: ...


@dataclass
class Programme:
    instructions: list[Instruction]
    constantes: list[Valeur]

    def __post_init__(self) -> None: ...


@dataclass
class MachineVirtuelle:
    programme: Programme
    pile_valeurs: list[Valeur] = field(default_factory=list)
    dernier_resultat: Valeur | None = None

    def empiler(self, valeur: Valeur) -> None: ...

    def depiler(self) -> Valeur: ...

    def executer_instruction(self, instruction: Instruction) -> None: ...

    def executer(self) -> Valeur: ...


def creer_exemple() -> Programme: ...
```
