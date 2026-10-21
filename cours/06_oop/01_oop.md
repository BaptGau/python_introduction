# Programmation orientée objet

La programmation orientée objet, ou **POO**, regroupe un état et les
comportements qui travaillent sur cet état.

```text
objet = données + comportements
```

Exemple : un compte bancaire possède un titulaire et un solde. Il peut recevoir
un dépôt ou effectuer un retrait.

## Le vocabulaire

```text
classe      → plan de construction
instance    → objet construit à partir de la classe
attribut    → donnée appartenant à l'objet
méthode     → fonction appartenant à la classe
```

```text
                         classe CompteBancaire
                         /                    \
                        /                      \
        compte_ada                              compte_grace
        titulaire = "Ada"                       titulaire = "Grace"
        solde = 100                             solde = 250
```

Les deux instances suivent le même plan, mais possèdent leur propre état.

## Une classe Python

```python
class CompteBancaire:
    banque = "Python Bank"  # attribut de classe

    def __init__(self, titulaire: str, solde_initial: int = 0) -> None:
        self.titulaire = titulaire
        self._solde = solde_initial

    def consulter_solde(self) -> int:
        return self._solde

    def deposer(self, montant: int) -> None:
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")

        self._solde += montant

    def retirer(self, montant: int) -> None:
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")

        if montant > self._solde:
            raise ValueError("Solde insuffisant.")

        self._solde -= montant
```

Créer et utiliser une instance :

```python
compte = CompteBancaire("Ada", 100)
compte.deposer(50)

print(compte.titulaire)  # Ada
print(compte.consulter_solde())  # 150
```

`__init__()` initialise l'instance après sa création. Les doubles underscores
signalent ici une méthode spéciale utilisée par Python.

## Le paramètre `self`

`self` désigne l'instance sur laquelle la méthode travaille.

```python
compte.deposer(50)
```

correspond approximativement à :

```python
CompteBancaire.deposer(compte, 50)
```

Python fournit automatiquement `compte` comme premier argument. `self` n'est
pas un mot-clé, mais son nom est une convention à toujours respecter.

## Méthode d'instance, de classe ou statique

Une classe peut contenir trois types de méthodes :

| Type     | Décorateur      | Premier paramètre | Travaille avec           |
| -------- | --------------- | ----------------- | ------------------------ |
| instance | aucun           | `self`            | une instance et son état |
| classe   | `@classmethod`  | `cls`             | la classe elle-même      |
| statique | `@staticmethod` | aucun implicite   | uniquement ses arguments |

### Méthode d'instance

C'est le cas le plus courant. Elle lit ou modifie une instance :

```python
class Produit:
    def __init__(self, nom: str, prix: float) -> None:
        self.nom = nom
        self.prix = prix

    def appliquer_remise(self, taux: float) -> None:
        self.prix *= 1 - taux
```

```python
clavier = Produit("Clavier", 50.0)
clavier.appliquer_remise(0.10)
```

### `@classmethod`

Une méthode de classe reçoit la classe dans `cls`, et non une instance dans
`self`. Un usage fréquent est de proposer un autre constructeur :

```python
class Produit:
    def __init__(self, nom: str, prix: float) -> None:
        self.nom = nom
        self.prix = prix

    @classmethod
    def depuis_texte(cls, texte: str) -> "Produit":
        nom, prix = texte.split(":")
        return cls(nom, float(prix))
```

```python
clavier = Produit.depuis_texte("Clavier:49.99")
```

Utiliser `cls(...)` plutôt que `Produit(...)` permet à la méthode de fonctionner
aussi correctement avec une future sous-classe.

Une méthode de classe peut aussi lire ou modifier un attribut de classe :

```python
class Produit:
    taux_tva = 0.20

    @classmethod
    def modifier_taux_tva(cls, nouveau_taux: float) -> None:
        if nouveau_taux < 0:
            raise ValueError("Le taux doit être positif ou nul.")

        cls.taux_tva = nouveau_taux


Produit.modifier_taux_tva(0.10)
```

### `@staticmethod`

Une méthode statique ne reçoit automatiquement ni `self`, ni `cls`. C'est une
fonction rangée dans la classe parce qu'elle est fortement liée à son domaine :

```python
class Produit:
    @staticmethod
    def prix_est_valide(prix: float) -> bool:
        return prix >= 0
```

```python
Produit.prix_est_valide(49.99)  # True
```

Elle ne peut accéder à une instance ou à la classe que si celles-ci lui sont
passées explicitement en argument.

```text
besoin de l'état d'un objet     → méthode d'instance avec self
besoin de la classe             → @classmethod avec cls
aucun des deux, mais lien fort  → @staticmethod
aucun lien fort avec la classe  → fonction de module
```

On peut techniquement appeler une méthode de classe ou statique depuis une
instance, mais l'appel depuis la classe rend généralement l'intention plus claire.

## Attribut d'instance ou de classe

```python
class CompteBancaire:
    banque = "Python Bank"  # partagé par toutes les instances

    def __init__(self, titulaire: str) -> None:
        self.titulaire = titulaire  # propre à chaque instance
```

Utiliser un attribut de classe pour une information réellement commune. Ne pas
y placer une liste mutable destinée à chaque instance : elle serait partagée
par tous les objets.

## Encapsulation

Une classe protège ses règles en faisant passer les modifications par ses
méthodes.

```python
compte.deposer(50)  # la méthode peut valider le montant
```

Le préfixe `_` indique par convention qu'un attribut est interne :

```python
self._solde
```

Ce n'est pas une protection absolue. Le message est : « utiliser les méthodes
publiques plutôt que modifier cet attribut directement ».

## Les grandes idées de la POO

- **Encapsulation** : regrouper l'état et les règles qui le protègent ;
- **Abstraction** : exposer une interface simple et cacher les détails ;
- **Composition** : construire un objet à partir d'autres objets ;
- **Polymorphisme** : Non couvert ici ;
- **Héritage** : Non couvert ici.

## Les dataclasses

Une **dataclass** sert à décrire un objet principalement composé de données.

```python
from dataclasses import dataclass


@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int = 0


clavier = Produit("Clavier", 49.99, 5)
```

Le décorateur `@dataclass` génère notamment :

- `__init__()` pour initialiser les attributs ;
- `__repr__()` pour afficher clairement l'objet ;
- `__eq__()` pour comparer deux objets par leurs valeurs.

```python
print(clavier)
# Produit(nom='Clavier', prix=49.99, quantite=5)

Produit("Clavier", 49.99, 5) == clavier  # True
```

Une dataclass peut aussi contenir des méthodes :

```python
@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int = 0

    def valeur_stock(self) -> float:
        return self.prix * self.quantite
```

### Valeurs mutables par défaut

Chaque instance doit recevoir sa propre liste :

```python
from dataclasses import dataclass, field


@dataclass
class Produit:
    nom: str
    tags: list[str] = field(default_factory=list)
```

Ne pas utiliser `tags: list[str] = []` : la même liste risquerait d'être
partagée. Les dataclasses refusent d'ailleurs les valeurs mutables courantes
comme défauts directs.

### Dataclass immutable

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

`frozen=True` empêche de réaffecter les champs après la création.
Cette protection est superficielle : un champ contenant lui-même une liste
reste mutable.

## Les enums

Une `Enum` représente un ensemble fini de choix nommés. Elle évite les
chaînes dispersées et les fautes de frappe.

```python
from enum import Enum


class StatutCommande(Enum):
    EN_ATTENTE = "en_attente"
    EXPEDIEE = "expediee"
    LIVREE = "livree"
    ANNULEE = "annulee"
```

```python
statut = StatutCommande.EN_ATTENTE

statut is StatutCommande.EN_ATTENTE  # True
statut.name  # "EN_ATTENTE"
statut.value  # "en_attente"
```

Les membres d'une enum sont des objets uniques. On peut les utiliser avec
`match` :

```python
match statut:
    case StatutCommande.EN_ATTENTE:
        print("La commande est en préparation")
    case StatutCommande.EXPEDIEE:
        print("La commande est en route")
    case _:
        print("La commande est terminée")
```

## Dataclass et enum ensemble

```python
from dataclasses import dataclass
from enum import Enum


class StatutCommande(Enum):
    EN_ATTENTE = "en_attente"
    EXPEDIEE = "expediee"


@dataclass
class Commande:
    numero: str
    client: str
    total: float
    statut: StatutCommande = StatutCommande.EN_ATTENTE

    def expedier(self) -> None:
        if self.statut is not StatutCommande.EN_ATTENTE:
            raise ValueError("La commande ne peut pas être expédiée.")

        self.statut = StatutCommande.EXPEDIEE
```

La dataclass décrit les données de la commande. L'enum limite son statut à
des valeurs connues. La méthode protège la transition entre les deux statuts.

## Dataclass ou dictionnaire ?

Un dictionnaire peut techniquement contenir des données hétérogènes. Mais son
typage est plus naturel quand les valeurs jouent le même rôle :

```python
stock: dict[str, int] = {
    "clavier": 5,
    "souris": 2,
}
```

Une dataclass décrit un enregistrement fixe avec des champs hétérogènes :

```python
@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int
    disponible: bool
```

| `dict`                            | `dataclass`                |
| --------------------------------- | -------------------------- |
| clés dynamiques                   | champs connus à l'avance   |
| valeurs souvent homogènes         | champs de types différents |
| accès avec `objet["nom"]`         | accès avec `objet.nom`     |
| structure flexible                | structure explicite        |
| adapté aux index et regroupements | adapté à une entité métier |

```python
# Possible, mais peu précis pour les outils de typage :
produit: dict[str, object] = {
    "nom": "Clavier",
    "prix": 49.99,
    "quantite": 5,
}
```

Choisir une dataclass si les mêmes champs reviennent pour chaque objet et ont
des significations précises. Choisir un dictionnaire si les clés sont
dynamiques ou si l'on construit une table d'association.

### Un dictionnaire avec des clés connues : `TypedDict`

Un `TypedDict` décrit précisément les clés et les types de valeurs attendus
dans un dictionnaire :

```python
from typing import TypedDict


class ProduitJSON(TypedDict):
    nom: str
    prix: float
    quantite: int


produit: ProduitJSON = {
    "nom": "Clavier",
    "prix": 49.99,
    "quantite": 5,
}
```

Un outil de typage peut alors détecter une clé absente, une clé inconnue ou une
valeur du mauvais type. L'accès reste celui d'un dictionnaire :

```python
def valeur_stock(produit: ProduitJSON) -> float:
    return produit["prix"] * produit["quantite"]
```

`TypedDict` n'ajoute aucune validation à l'exécution. La valeur créée est un
dictionnaire ordinaire, pas une instance de `ProduitJSON` :

```python
type(produit) is dict  # True
```

Il est particulièrement utile pour décrire des données qui doivent conserver
une forme de dictionnaire, par exemple un document JSON ou la réponse d'une
API. Une dataclass est préférable lorsque l'on veut construire un véritable
objet, accéder à ses champs avec des attributs ou lui ajouter des méthodes.

## Une classe n'est pas toujours la solution

Cette classe n'apporte aucun état ni comportement d'objet :

```python
class Calculatrice:
    @staticmethod
    def additionner(a: int, b: int) -> int:
        return a + b
```

Une fonction est plus simple :

```python
def additionner(a: int, b: int) -> int:
    return a + b
```

Utiliser plutôt des fonctions quand :

- le calcul dépend uniquement de ses arguments ;
- aucun état ne doit être conservé entre les appels ;
- plusieurs petites transformations indépendantes suffisent.

Utiliser plutôt une classe quand :

- plusieurs données forment une même entité ;
- cette entité possède un état qui évolue ;
- plusieurs comportements travaillent sur cet état ;
- des règles doivent protéger les modifications.

```text
transformation sans état ──▶ fonction
données structurées seules ─▶ dataclass
données structurées en dict ─▶ TypedDict
état + règles + comportements ─▶ classe
choix fini nommé ─────────▶ Enum
```

Éviter les classes qui font tout : lecture des saisies, calculs, affichage,
sauvegarde et validation. Une classe, comme une fonction, doit avoir une
responsabilité claire.
