# 5 — Variables et mémoire

## Une variable est un nom, pas une boîte

Une valeur Python est un **objet** stocké en mémoire. Une variable est un nom
qui fait référence à cet objet.

```python
prenom = "Ada"
```

```text
nom                         objet en mémoire

prenom ── référence vers ──▶  "Ada"
```

Python ne permet pas de manipuler directement l'adresse mémoire comme certains autres
langages.

Une affectation peut donner plusieurs noms au **même objet** :

```python
panier_a = ["pomme"]
panier_b = panier_a
```

```text
panier_a ──┐
           ├──▶ ["pomme"]
panier_b ──┘
```

## L'avantage

- Python gère automatiquement l'allocation et la libération de la mémoire ;
- transmettre un objet ne demande pas de recopier tout son contenu ;
- plusieurs parties du programme peuvent travailler sur le même objet ;
- une variable peut être reliée à un nouvel objet simplement.

Quand un objet n'est plus accessible par aucune référence, Python peut
récupérer sa mémoire. Les détails de ce mécanisme dépendent de
l'implémentation de Python - _garbage collector_.

## Impact sur le temps d'exécution

Affecter une variable est généralement rapide : Python copie une
**référence**, pas tout l'objet.

```python
grande_liste = list(range(1_000_000))

meme_liste = grande_liste          # rapide : nouvelle référence
autre_liste = grande_liste.copy()  # plus long : copie des éléments
```

```text
affectation d'une référence → coût presque constant
copie d'une liste             → coût proportionnel à sa taille
```

Les objets immutables peuvent entraîner la création de nouveaux objets :

```python
message = ""
message = message + "Bonjour"  # crée une nouvelle chaîne
```

Créer, copier et supprimer des objets demande du temps. La gestion automatique
de la mémoire ajoute elle aussi un petit coût, mais elle évite au programmeur de
réserver et libérer la mémoire manuellement.

Cette simplicité a une contrepartie : Python doit suivre les références, stocker
le type de chaque objet et déterminer l'opération à effectuer pendant
l'exécution. Cela contribue à rendre Python plus lent et plus gourmand en
mémoire que certains langages compilés, en échange d'un code plus simple à
écrire et à maintenir.

Pour débuter, la priorité reste un code clair et correct. On optimise seulement
si une mesure montre qu'une partie du programme est réellement lente.

## Le piège : les objets mutables partagés

Une liste est **mutable** : elle peut être modifiée sans créer un nouvel objet.

```python
panier_a = ["pomme"]
panier_b = panier_a

panier_b.append("poire")

print(panier_a)  # ["pomme", "poire"]
print(panier_b)  # ["pomme", "poire"]
```

Modifier l'objet avec un nom rend donc la modification visible avec l'autre.

Pour obtenir deux listes indépendantes, il faut copier :

```python
panier_a = ["pomme"]
panier_b = panier_a.copy()

panier_b.append("poire")

print(panier_a)  # ["pomme"]
print(panier_b)  # ["pomme", "poire"]
```

`list`, `dict` et `set` sont mutables. `int`, `float`, `bool`, `str` et `tuple`
sont immutables.

## Modifier ou réaffecter ?

```python
nombres = [1, 2]
autres_nombres = nombres

nombres.append(3)  # modifie l'objet partagé
nombres = [9]      # relie seulement `nombres` à un nouvel objet
```

Après ces instructions :

```text
nombres        ──▶ [9]
autres_nombres ──▶ [1, 2, 3]
```

Avec un objet immutable, une « modification » crée en réalité un nouvel
objet :

```python
age_a = 20
age_b = age_a
age_b += 1

print(age_a)  # 20
print(age_b)  # 21
```

## `==` ou `is` ?

```python
liste_a = [1, 2]
liste_b = [1, 2]

liste_a == liste_b  # True  : même valeur
liste_a is liste_b  # False : objets différents
```

- `==` compare les valeurs ;
- `is` vérifie si deux noms désignent exactement le même objet.

Dans le code courant, utiliser `==` pour comparer des valeurs. Le cas habituel
pour `is` est la comparaison avec `None` :

```python
if resultat is None:
    print("Aucun résultat")
```

Cette notion sera importante avec les fonctions : un paramètre reçoit lui
aussi une référence vers l'objet fourni lors de l'appel.
