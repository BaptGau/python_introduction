# NumPy et Pandas : calculer et analyser des données

```python
import numpy as np
import pandas as pd
```

- **NumPy** manipule efficacement des tableaux numériques ;
- **Pandas** manipule des données organisées en lignes et colonnes.

## `list` ou tableau NumPy ?

Une liste Python stocke des **références** vers des objets. Elle peut mélanger
les types et changer de taille facilement.

```python
valeurs = [10, 2.5, "inconnu"]
```

```text
list : [référence] [référence] [référence]
             │          │          │
             ▼          ▼          ▼
            10         2.5     "inconnu"
```

Un `ndarray` NumPy contient normalement des valeurs d'un même type, décrites
par son `dtype`. Elles sont souvent rangées dans une zone mémoire contiguë ;
une vue peut toutefois parcourir cette zone avec un pas différent.

```python
temperatures = np.array([18.5, 20.0, 21.5])

temperatures.dtype  # float64
temperatures.shape  # (3,)
temperatures.ndim  # 1
```

```text
ndarray float64 : [18.5] [20.0] [21.5]
                   valeurs homogènes et proches en mémoire
```

Cela apporte généralement :

- moins de mémoire pour de nombreuses valeurs numériques ;
- un meilleur usage du cache du processeur ;
- des calculs effectués par du code compilé, sans boucle Python par valeur ;
- des tableaux à plusieurs dimensions.

En contrepartie, un tableau NumPy est moins flexible : son type et sa taille
sont contraints. Créer un tableau a aussi un coût. Une `list` reste adaptée à
une petite collection générale ou hétérogène.

## Vectorisation et parallélisation

Avec une liste, le programme exécute la boucle dans l'interpréteur Python :

```python
prix = [10.0, 20.0, 30.0]
prix_ttc = [valeur * 1.2 for valeur in prix]
```

Avec NumPy, on décrit l'opération sur le tableau entier :

```python
prix = np.array([10.0, 20.0, 30.0])
prix_ttc = prix * 1.2
```

C'est la **vectorisation** : la boucle existe toujours, mais elle est exécutée
dans du code compilé et optimisé. Le processeur peut parfois traiter plusieurs
valeurs avec une même instruction (**SIMD**).

```text
boucle Python  : Python pilote chaque opération
vectorisation  : NumPy confie la boucle au code compilé
parallélisation: plusieurs cœurs exécutent du travail en même temps
```

Vectoriser ne signifie donc pas automatiquement paralléliser :

- beaucoup d'opérations NumPy libèrent le GIL : plusieurs threads Python
  peuvent alors travailler en parallèle sur des tableaux distincts ;
- certains calculs d'algèbre linéaire utilisent plusieurs threads via BLAS ;
- cela dépend de l'opération et de l'installation de NumPy ;
- `np.vectorize()` facilite l'écriture, mais ne rend pas une fonction plus rapide
  et ne la parallélise pas.

Pandas vectorise aussi de nombreuses opérations, mais ne parallélise pas
automatiquement un traitement.

## Créer et lire un tableau

```python
notes = np.array([12, 15, 9, 18])
zeros = np.zeros(3)  # [0., 0., 0.]
suite = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

notes[0]  # 12
notes[-1]  # 18
notes[1:3]  # array([15, 9])
```

Un tableau à deux dimensions possède des lignes et des colonnes :

```python
matrice = np.array(
    [
        [10, 20, 30],
        [40, 50, 60],
    ]
)

matrice.shape  # (2, 3)
matrice[1, 2]  # 60
matrice[:, 0]  # première colonne : [10, 40]
```

## Calculs, filtres et agrégations

Les opérations se font élément par élément :

```python
notes + 1
notes * 2
notes >= 10  # tableau de booléens
notes[notes >= 10]  # filtre : [12, 15, 18]
```

```python
notes.sum()
notes.mean()
notes.min()
notes.max()
```

Sur plusieurs dimensions, `axis` indique l'axe que l'on réduit :

```python
matrice.sum(axis=0)  # somme de chaque colonne : [50, 70, 90]
matrice.sum(axis=1)  # somme de chaque ligne   : [60, 150]
```

## Broadcasting

Le **broadcasting** permet de combiner des tableaux de formes compatibles sans
répéter manuellement les valeurs.

```python
matrice = np.array([[10, 20, 30], [40, 50, 60]])
bonus = np.array([1, 2, 3])

matrice + bonus
# [[11, 22, 33],
#  [41, 52, 63]]
```

`bonus` est appliqué à chaque ligne. Le broadcasting évite souvent une copie,
mais des expressions complexes peuvent tout de même créer de gros tableaux
intermédiaires.

## Vue ou copie ?

Une tranche NumPy est souvent une **vue** sur les mêmes données :

```python
valeurs = np.array([1, 2, 3, 4])
vue = valeurs[1:3]
vue[0] = 99

print(valeurs)  # [1, 99, 3, 4]
```

Utiliser `.copy()` lorsqu'une copie indépendante est nécessaire.

## Pandas : `Series` et `DataFrame`

Une `Series` est une colonne avec un index. Un `DataFrame` est une table dont
chaque colonne peut avoir son propre type.

```python
ventes = pd.DataFrame(
    {
        "produit": ["Livre", "Clavier", "Livre"],
        "categorie": ["Culture", "Informatique", "Culture"],
        "prix": [12.0, 50.0, 12.0],
        "quantite": [2, 1, 3],
    }
)

ventes.shape
ventes.dtypes
ventes.head()
```

Pandas s'appuie notamment sur NumPy, tout en ajoutant des labels, des types de
colonnes supplémentaires et des outils d'analyse.

## Sélectionner et filtrer

```python
ventes["prix"]  # une Series
ventes[["produit", "prix"]]  # un DataFrame

ventes.loc[0, "produit"]  # sélection par labels
ventes.iloc[0, 2]  # sélection par positions

cheres = ventes.loc[ventes["prix"] >= 20]
```

Pour créer une colonne, préférer aussi une opération vectorisée :

```python
ventes["total"] = ventes["prix"] * ventes["quantite"]
```

Une affectation modifie le `DataFrame`. Utiliser `ventes.copy()` si l'original
doit rester intact.

## Valeurs manquantes

Une donnée absente peut être représentée par `NaN` ou `pd.NA` selon le type.

```python
ventes["prix"].isna()  # repérer
ventes["prix"].fillna(ventes["prix"].mean())
ventes.dropna(subset=["prix"])  # retirer les lignes concernées
```

Le bon traitement dépend du sens métier : remplacer une valeur manquante par
zéro n'est pas toujours correct.

## Regrouper et agréger

`groupby` suit l'idée **séparer → appliquer → combiner** :

```python
total_par_categorie = ventes.groupby("categorie")["total"].sum()
```

```text
Culture         → lignes du groupe → somme → 60.0
Informatique    → lignes du groupe → somme → 50.0
```

## Mémo

```text
list       → flexible, hétérogène, code Python général
ndarray    → homogène, compact, calcul numérique vectorisé
Series     → une colonne indexée
DataFrame  → table avec colonnes nommées et potentiellement hétérogènes

vectorisation ≠ parallélisation automatique
slice NumPy    → souvent une vue
DataFrame.copy → copie avant modification indépendante
```
