# Projet — StockFlow, gestionnaire de stock

**Durée : 3 heures**  
**Format : individuel**  
**Livrables : `flow_stockflow.md` puis `stockflow.py`**

## Objectif

Créer une application en terminal pour gérer le stock d'une petite boutique.

Le programme doit permettre de :

1. consulter le stock ;
2. ajouter un nouveau produit ;
3. enregistrer une entrée ou une sortie de stock ;
4. consulter l'historique des mouvements ;
5. afficher quelques statistiques ;
6. traiter proprement les saisies et opérations invalides.

Le projet utilise uniquement les bases de Python, les fonctions, le control
flow, les collections et les exceptions intégrées. Aucune classe n'est
nécessaire.

## Avant de coder — flow obligatoire

Lire la fiche [Représenter le flow](00_representer_un_flow.md), puis préparer un flow avant d'écrire le programme.

Le document doit contenir :

- un flowchart du menu principal et de sa boucle ;
- le flow détaillé d'une entrée et d'une sortie de stock ;
- une table de décision couvrant produit inconnu, quantité invalide, stock
  insuffisant et mouvement accepté ;
- les chemins d'erreur qui ne modifient ni le stock ni l'historique ;
- les responsabilités ou fonctions identifiées grâce au diagramme.

## Données de départ

```python
stock: dict[str, int] = {
    "clavier": 5,
    "souris": 2,
    "ecran": 0,
}

historique: list[tuple[str, str, int]] = []
```

Chaque collection a une responsabilité :

```text
stock       : nom du produit → quantité disponible
historique  : (type de mouvement, produit, quantité)
```

Exemple d'historique :

```python
[
    ("entree", "clavier", 4),
    ("sortie", "souris", 1),
]
```

## Règles métier

- les noms de produits sont nettoyés avec `strip().lower()` ;
- un nom vide est invalide ;
- deux produits ne peuvent pas avoir le même nom ;
- une quantité de mouvement doit être strictement positive ;
- une quantité initiale doit être positif ou nul ;
- une sortie ne peut pas rendre le stock négatif ;
- un mouvement refusé ne modifie ni le stock ni l'historique ;

## Menu attendu

Le menu est affiché dans une boucle `while` :

```text
=== STOCKFLOW ===
1 - Afficher le stock
2 - Ajouter un produit
3 - Enregistrer une entrée
4 - Enregistrer une sortie
5 - Afficher l'historique
6 - Afficher les statistiques
7 - Quitter
Votre choix :
```

Utiliser `match` pour traiter le choix. Une commande inconnue affiche un
message, puis le menu apparaît de nouveau.

## Fonctionnalités obligatoires

### 0. Saisie d'un nombre

Créer une fonction qui demande un nombre entier selon à partir d'un message, le retourne si le nombre est valide et
réessaie si le nombre est
invalide.

```
def saisie_entier(msg: str = "Entrez un nombre: ") -> int:
    ...
```

Cette fonction sera utilisée pour demander les quantités par la suite.

### 1. Afficher le stock

Parcourir le dictionnaire :

```text
=== STOCK ===
clavier : 5 unités
souris : 2 unités
ecran : 0 unité
```

L'ordre exact des produits n'est pas imposé.

### 2. Ajouter un produit

Demander le nom et la quantité initiale.

```text
Nom : Webcam
Quantité initiale : 4
Produit "webcam" ajouté.
```

Si le produit existe déjà, lever une `ValueError` :

```text
Ce produit existe déjà.
```

La normalisation d'un nom (`produit.strip().lower()`) lève `ValueError` si le nom nettoyé est vide.

La création d'un produit n'est pas un mouvement et ne doit pas être ajoutée à
l'historique.

### 3. Enregistrer une entrée

Une entrée augmente la quantité disponible.

```text
Produit : clavier
Quantité reçue : 4
Entrée enregistrée. Nouveau stock : 9
```

Après réussite, ajouter ce tuple à l'historique :

```python
("entree", "clavier", 4)
```

Un produit inconnu doit provoquer une `KeyError`, ensuite traitée par le menu.

Si la quantité est négative ou nulle, lever une `ValueError` avec le
message `"Quantitée invalide."`.

### 4. Enregistrer une sortie

Une sortie diminue la quantité sans jamais passer sous zéro.

```text
Produit : souris
Quantité vendue : 1
Sortie enregistrée. Nouveau stock : 1
```

Après réussite, ajouter :

```python
("sortie", "souris", 1)
```

Un produit inconnu doit provoquer une `KeyError`, ensuite traitée par le menu.

Si la quantité demandée dépasse le stock, lever une `ValueError` avec le
message `"Stock insuffisant."`.

### 5. Afficher l'historique

Parcourir la liste de tuples avec `for` et décomposer chaque tuple :

```python
for type_mouvement, produit, quantite in historique:
    ...
```

Affichage attendu :

```text
=== HISTORIQUE ===
ENTREE — clavier — 4
SORTIE — souris — 1
```

Si aucun mouvement n'a réussi/n'est enregistré :

```text
Aucun mouvement.
```

### 6. Afficher les statistiques

Afficher :

- le nombre de produits avec `len(stock)` ;
- la quantité totale disponible ;
- le nombre de produits en rupture, donc avec une quantité égale à zéro.

Utiliser au moins une expression génératrice.

Exemple initial :

```text
=== STATISTIQUES ===
Produits différents : 3
Unités disponibles : 7
Produits en rupture : 1
```

## Gestion des exceptions

### Saisie d'un entier

Créer une fonction dédiée qui redemande une valeur jusqu'à recevoir un entier
dans les limites autorisées.

Elle doit utiliser `try/except ValueError` autour de `int(input(...))`.

```text
Quantité : bonjour
Veuillez saisir un entier.
Quantité : -2
La valeur doit être supérieure ou égale à 1.
Quantité : 3
```

Pour la quantité initiale et le seuil, appeler la fonction avec `minimum=0`.

## Point d'entrée

Créer une fonction principale d'orchestration et protéger son appel avec
`if __name__ == "__main__":`.

## Scénarios de validation

Le projet est terminé si les scénarios suivants fonctionnent :

1. `"  CLAVIER  "` est normalisé en `"clavier"` ;
2. une saisie texte est refusée sans arrêter le programme ;
3. ajouter `webcam` avec une quantité de `4` réussit ;
4. ajouter une seconde fois `webcam` est refusé ;
5. ajouter `4` claviers fait passer leur stock de `5` à `9` ;
6. retirer `1` souris fait passer leur stock de `2` à `1` ;
7. retirer `10` souris est refusé sans modifier le stock ni l'historique ;
8. modifier un produit inconnu affiche `"Produit inconnu."` ;
9. les statistiques initiales indiquent `3` produits, `7` unités et `1`
   rupture ;
10. l'historique contient uniquement les mouvements réussis ;
11. le choix `7` termine le programme proprement.

Tester les fonctions métier directement dans la console avant de construire
le menu complet.

## Aide — interfaces possibles

Vous êtes libres de choisir vos fonctions. Voici un découpage possible si vous
avez besoin d'un point de départ :

```python
def demander_entier(message: str, minimum: int = 1) -> int: ...


def normaliser_nom(nom: str) -> str: ...


def ajouter_produit(
        stock: dict[str, int],
        seuils: dict[str, int],
        nom: str,
        quantite: int,
        seuil: int,
) -> None: ...


def ajouter_stock(stock: dict[str, int], produit: str, quantite: int) -> None: ...


def retirer_stock(stock: dict[str, int], produit: str, quantite: int) -> None: ...


def enregistrer_mouvement(
        historique: list[tuple[str, str, int]],
        type_mouvement: str,
        produit: str,
        quantite: int,
) -> None: ...


def lancer_stockflow() -> None: ...
```

Exemple de traitement d'une sortie :

```python
try:
    retirer_stock(stock, produit, quantite)
except KeyError:
    print("Produit inconnu.")
except ValueError as erreur:
    print(erreur)
else:
    enregistrer_mouvement(historique, "sortie", produit, quantite)
```

Ces interfaces sont facultatives. Les comportements décrits dans le sujet
restent obligatoires.
