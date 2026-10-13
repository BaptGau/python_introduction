# Projet — Le mini-distributeur bancaire

**Durée : 3 heures**  
**Format : individuel**  
**Livrables : `flow_distributeur.md` puis `distributeur.py`**

## Objectif

Créer un distributeur bancaire utilisable dans le terminal.

Le programme doit :

1. demander un code secret ;
2. bloquer l'accès après trois erreurs ;
3. afficher un menu tant que l'utilisateur ne quitte pas ;
4. permettre de consulter le solde, de déposer et de retirer de l'argent ;

Ce projet mobilise les types, les entrées/sorties, les fonctions, les
booléens, `if/elif/else`, `match` et les boucles `while`.

## Avant de coder — flow obligatoire

Lire la fiche [Représenter le flow](00_representer_un_flow.md), puis préparer un flow avant d'écrire le programme.

Le document doit contenir :

- un flowchart allant de l'authentification à la fin de session ;
- la boucle du menu et les branches associées à chaque choix ;
- les chemins « code correct » et « trois erreurs » ;

## Règles du distributeur

Au démarrage :

```python
CODE_SECRET = "1234"
SOLDE_INITIAL = 500
MAX_ESSAIS = 3
PLAFOND_RETRAIT = 300
```

- le code est comparé comme une chaîne de caractères ;
- trois codes incorrects bloquent la session ;
- un montant doit être un entier strictement positif ;
- un retrait ne peut pas dépasser le solde disponible ;
- un retrait ne peut pas dépasser `PLAFOND_RETRAIT` ;
- une opération refusée ne modifie pas le solde ;
- le solde ne doit jamais devenir négatif.

Les montants sont des entiers pour ce premier projet : `25` est valide, mais
`25.50`, `-10` et `bonjour` ne le sont pas.

## Menu attendu

Après l'authentification, le menu est affiché en boucle :

```text
=== MINI-DISTRIBUTEUR ===
1 - Consulter le solde
2 - Déposer de l'argent
3 - Retirer de l'argent
4 - Quitter
Votre choix :
```

Utiliser `match` pour traiter le choix. Une commande inconnue doit afficher un
message puis laisser l'utilisateur essayer de nouveau.

## Fonctionnalités obligatoires

### 1. Authentification

Demander le code tant qu'il est incorrect et qu'il reste des essais.

```text
Code secret : 0000
Code incorrect. Essais restants : 2
Code secret : 1234
Accès autorisé.
```

Si les trois essais échouent :

```text
Carte bloquée.
```

Le menu ne doit alors jamais apparaître.

### 2. Consultation du solde

```text
Solde disponible : 500 €
```

### 3. Dépôt

Demander un montant valide, l'ajouter au solde et enregistrer l'opération.

```text
Montant du dépôt : 50
Dépôt accepté. Nouveau solde : 550 €
```

### 4. Retrait

Vérifier le montant, le plafond et le solde avant de modifier quoi que ce soit.

```text
Montant du retrait : 80
Retrait accepté. Nouveau solde : 470 €
```

Messages attendus en cas de refus :

```text
Solde insuffisant.
Le plafond de retrait est de 300 €.
```

### 6. Fin de session

Le choix `5` arrête la boucle et affiche :

```text
Au revoir. Solde final : 470 €
```

## Point d'entrée

Créer une fonction principale qui orchestre le programme : elle appelle
d'autres fonctions, mais ne contient pas elle-même tous les calculs. Protéger
son appel avec `if __name__ == "__main__":`.

## Valider un montant

`int(input(...))` provoque une erreur si l'utilisateur saisit `bonjour`.
Utiliser `str.isdigit()` permet de vérifier la saisie avant la conversion :

```python
texte = input("Montant : ")

if texte.isdigit():
    montant = int(texte)
```

Une fonction dédiée doit recommencer avec une boucle `while` tant que la saisie
n'est pas un entier strictement positif.

```text
Montant : bonjour
Montant invalide.
Montant : -20
Montant invalide.
Montant : 0
Montant invalide.
Montant : 20
```

## Scénarios de validation

Le projet est terminé si les huit scénarios suivants fonctionnent :

1. le bon code ouvre le menu ;
2. trois mauvais codes bloquent la session ;
3. un dépôt de `50` fait passer le solde de `500` à `550` ;
4. un retrait de `80` après ce dépôt laisse `470` ;
5. un retrait supérieur au solde est refusé sans modifier le solde ;
6. un retrait supérieur à `300` est refusé ;
7. `bonjour`, `-20` et `0` sont refusés comme montants ;

Tester aussi chaque fonction séparément dans la console Python lorsque c'est
possible.

## Contraintes de qualité

- utiliser des noms explicites en français ;
- annoter les arguments et les valeurs de retour ;
- une fonction = une responsabilité ;
- ne pas utiliser de variable globale modifiable ;
- ne pas dupliquer le traitement d'une même saisie ;
- ne pas utiliser de boucle `for` pour ce projet ;
- ne pas installer de package externe.

## Aide — interfaces possibles

Vous êtes libres de choisir votre découpage. Si vous ne savez pas comment
commencer, vous pouvez utiliser ces signatures :

```python
def authentifier(code_secret: str, maximum_essais: int) -> bool: ...


def demander_montant(message: str) -> int: ...


def deposer(solde: int, montant: int) -> int: ...


def retirer(
    solde: int,
    montant: int,
    plafond: int,
) -> int: ...


def lancer_distributeur() -> None: ...


if __name__ == "__main__":
    lancer_distributeur()
```

Cette interface est une aide, pas une obligation. Les règles métier et les
scénarios de validation restent obligatoires.
