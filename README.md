# Introduction à Python

Supports courts pour découvrir Python par la pratique.

## Organisation

- `cours/` : notes et mémos vus en classe ;
- `exercices/` : exercices à compléter, écrits avec `pytest` ;
- `projects/` : sujets des projets au format Markdown.

## Démarrage

```bash
uv sync
uv run pytest exercices
```

Les exercices contiennent volontairement des `...` à remplacer. Il est donc
normal que certains tests échouent au départ. Les corrections sont réalisées
directement avec les étudiants.

## Cours

> [Consigne générale : formater le code avec Ruff](cours/00_consigne_generale.md)

### 1. Les bases

1. [Du code à l'exécution](cours/01_base/01_execution_python.md)
2. [Paquets, environnement virtuel et uv](cours/01_base/02_paquets_et_uv.md)
3. [Types Python](cours/01_base/03_types.md)
4. [Mémo de pratique](cours/01_base/04_memo_pratique.md)
5. [Variables et mémoire](cours/01_base/05_variables_et_memoire.md)

### 2. Les fonctions

1. [Découper et réutiliser son code](cours/02_fonctions/01_fonctions.md)

### 3. Control flow

1. [Choisir et répéter](cours/03_control_flow/01_control_flow.md)

### 4. Collections

1. [Organiser et parcourir des données](cours/04_collections/01_collections.md)

### 5. Exceptions

1. [Détecter, traiter et signaler les erreurs](cours/05_exceptions/01_exceptions.md)

### 6. Programmation orientée objet

1. [Classes, dataclasses et enums](cours/06_oop/01_oop.md)

### 7. NumPy et Pandas

1. [Calculer et analyser des données](cours/07_numpy_pandas/01_numpy_pandas.md)

