# 4 — Mémo de pratique

## Afficher et lire

```python
prenom = input("Ton prénom : ")  # input() renvoie toujours une str
print("Bonjour", prenom)
```

## Opérateurs

```text
+   addition / concaténation
-   soustraction
*   multiplication / répétition
/   division (résultat float)
//  division entière
%   reste de la division
**  puissance
```

## Imports

```python
import math
from math import sqrt
```

## Lire une erreur

Lire le traceback du bas vers le haut :

1. type de l'erreur (`TypeError`, `NameError`, etc.) ;
2. message ;
3. fichier et numéro de ligne.

## Inspecter dans PyCharm

1. Cliquer dans la marge pour poser un point d'arrêt.
2. Lancer **Debug** plutôt que **Run**.
3. Observer les noms, valeurs et types dans **Variables**.
4. Avancer avec **Step Over**.
