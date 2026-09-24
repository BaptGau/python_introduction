# 1 — Du code à l'exécution

## Le modèle simple

```text
├─ Utilisateur
│  └─ écrit du code Python (.py)
│
├─ Implémentation de Python : CPython
│  ├─ compile le code en bytecode
│  └─ exécute les instructions du bytecode
│
└─ Processeur
   └─ exécute le code machine de CPython
```

Le **bytecode** est une suite d'instructions internes : charger une valeur,
appeler une fonction, retourner un résultat, etc.

```python
print("Bonjour")
```

peut notamment produire des instructions comme `LOAD_NAME`, `CALL` et
`RETURN_VALUE`. Leur nom exact peut changer selon la version de Python.

## CPython

CPython est l'implémentation de Python la plus courante. L'interpréteur est un
programme, principalement écrit en C, qui a déjà été compilé en code machine
avant son installation.

Quand on lance un fichier `.py`, CPython travaille en deux grandes phases :

```text
1. COMPILE

code source (.py)
    ↓ lecture de la syntaxe
arbre syntaxique (AST)
    ↓ compilation par CPython
objet code contenant du bytecode


2. EXÉCUTE

bytecode
    ↓ lu instruction par instruction
boucle d'interprétation de CPython
    ↓ appelle les opérations internes nécessaires
code machine de CPython
    ↓
processeur
```

Ici, **compiler** ne signifie pas produire directement un programme natif
indépendant. CPython transforme le code source en instructions intermédiaires
qu'il sait exécuter : le bytecode.

### La boucle d'interprétation

La boucle d'interprétation répète essentiellement trois actions :

```text
lire l'instruction → identifier l'opération → exécuter son implémentation
          ↑                                      │
          └─────── instruction suivante ──────────┘
```

Prenons cette fonction :

```python
def additionner(a: int, b: int) -> int:
    return a + b
```

Son bytecode demande notamment à CPython de :

1. charger la valeur référencée par `a` ;
2. charger la valeur référencée par `b` ;
3. effectuer l'opération `+` adaptée à leurs types ;
4. retourner le résultat.

Pour l'addition, CPython doit regarder les objets reçus : `+` n'effectue pas la
même action avec deux nombres, deux chaînes ou des objets personnalisés. Une
seule instruction de bytecode peut donc provoquer l'exécution de nombreuses
instructions machine.

Le processeur ne comprend pas directement le bytecode Python. Il exécute le
code machine de CPython, et ce code machine applique le sens de chaque
instruction du bytecode.

```text
                instructions pour CPython       instructions pour le processeur
code Python  ──────▶  bytecode  ──────────▶  CPython compilé
                                                        │
                                                        ▼
                                                   processeur
```

L'assembleur n'est donc pas une nouvelle étape obligatoire à chaque lancement
du script. S'il intervient dans cette chaîne, c'est lors de la construction de
CPython en programme natif, pas lors de l'exécution habituelle du fichier `.py`.

### Le cache `__pycache__`

CPython peut sauvegarder le bytecode de certains modules dans des fichiers
`.pyc`, placés dans `__pycache__/`. Si le code source n'a pas changé, il peut
réutiliser ce bytecode et éviter de le recompiler.

```text
premier import  : module.py → compilation → bytecode → exécution
imports suivants : fichier .pyc disponible ────────────▶ exécution
```

Le fichier `.pyc` ne contient pas un programme autonome : il a toujours besoin
d'une version compatible de l'interpréteur Python.

D'autres implémentations peuvent faire autrement. PyPy, par exemple, peut
compiler du code pendant l'exécution. Le bytecode montré par `dis` est un
détail de CPython, pas une règle universelle du langage Python.

## Voir les instructions

```bash
uv run python cours/01_base/exemples/voir_bytecode.py
```

Le fichier utilise `dis.dis()` pour afficher le bytecode d'une fonction.
