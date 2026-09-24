# 3 — Les types Python

Un type définit la nature d'une valeur et les opérations possibles.

```python
age = 28                 # int   : entier
temperature = 19.5       # float : nombre décimal
prenom = "Ada"           # str   : texte
est_connecte = True      # bool  : vrai ou faux
rien = None              # None  : absence de valeur
```

Python est à **typage dynamique** : une variable n'a pas besoin d'une
déclaration de type, mais chaque valeur possède bien un type.

```python
valeur = 3
print(type(valeur))  # <class 'int'>

valeur = "trois"    # autorisé : valeur d'un autre type
```

## Une opération dépend du type

```python
2 + 3           # 5
"Py" + "thon"  # "Python"
"ha" * 3       # "hahaha"
True + True     # 2 : bool est un sous-type de int
```

Une opération impossible produit une erreur :

```python
"3" + 2  # TypeError
```

Python ne devine pas ici s'il faut produire `"32"` ou `5`. Il faut convertir
explicitement avec `str(2)` ou `int("3")`.
