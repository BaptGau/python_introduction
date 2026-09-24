# 2 — Paquets, environnement virtuel et `uv`

## Des briques réutilisables

Un **module** est généralement un fichier Python. Un **package** regroupe des
modules. Une dépendance est un package externe utilisé par notre projet.

```text
┌─ Projet ───────────────────────────────┐
│ notre code                            │
│   ├─ module calcul.py                 │
│   └─ package boutique/               │
│                                      │
│ briques externes                     │
│   ├─ pytest  → lancer les tests       │
│   └─ requests → appeler un site web   │
└───────────────────────────────────────┘
```

On importe une brique pour l'utiliser :

```python
import math

print(math.sqrt(81))
```

## Pourquoi un environnement virtuel ?

Deux projets peuvent demander des versions différentes du même package.

```text
Projet A → .venv → package X version 1
Projet B → .venv → package X version 2
```

Chaque `.venv` isole l'interpréteur et les packages du projet. On évite ainsi
de modifier le Python du système ou de casser un autre projet.

> `.venv` est un environnement virtuel. `.env` est habituellement un fichier
> de variables de configuration : ce ne sont pas les mêmes choses.

## Ce que fait `uv`

```text
pyproject.toml → uv sync → .venv + versions exactes dans uv.lock
                         ↓
                 uv run python ...
                 uv run pytest
```

- `uv add nom-du-package` : ajoute une dépendance ;
- `uv sync` : crée ou met à jour `.venv` ;
- `uv run ...` : lance une commande dans cet environnement ;
- `uv.lock` : verrouille les versions pour reproduire l'installation.

On commit `pyproject.toml` et `uv.lock`, mais jamais `.venv/`.

## Le `Makefile`

Un `Makefile` donne des noms courts aux commandes fréquentes du projet :

```makefile
lint:
	uv run ruff check

format:
	uv run ruff format
```

On peut alors lancer :

```bash
make lint
make format
```

`make` exécute les commandes : il ne remplace ni `uv`, ni les outils appelés.
Les lignes de commande d'un `Makefile` commencent obligatoirement par une
tabulation. Un target doit rester une action simple et reproductible.
