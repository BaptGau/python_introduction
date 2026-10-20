# Consigne générale — formater le code

Avant de rendre un exercice ou un projet, formater tous les fichiers Python :

```bash
make format
```

Cette commande appelle Ruff. La commande équivalente est :

```bash
uv run ruff format .
```

Relire ensuite les fichiers modifiés avant de les rendre. Le formatage améliore
la présentation du code, mais ne vérifie pas son fonctionnement.

## Vérifier le code avec le linter

Le **linter** analyse le code sans l'exécuter. Il peut notamment signaler :

- un import ou une variable inutilisée ;
- un nom inconnu ;
- une expression sans effet ;
- certaines erreurs ou constructions difficiles à lire.

Lancer Ruff avec :

```bash
make lint
```

La commande équivalente est :

```bash
uv run ruff check .
```

Chaque message indique le fichier, la ligne, le code de la règle et une
explication :

```text
exemple.py:8:5: F841 Local variable `resultat` is assigned to but never used
```

Corriger les messages un par un, puis relancer la commande jusqu'à ce qu'elle
termine sans erreur. Certains exercices incomplets peuvent volontairement
signaler des `...` ou des variables encore inutilisées.

```text
ruff format → met le code en forme
ruff check  → cherche des problèmes dans le code
pytest      → vérifie le comportement du programme
```
