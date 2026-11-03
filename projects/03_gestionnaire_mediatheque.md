# Projet — MediaFlow, gestionnaire de médiathèque

## Objectif

Créer une petite application en terminal pour gérer les documents et les
emprunts d'une médiathèque.

Le programme doit permettre de :

1. ajouter un document ;
2. afficher le catalogue ;
3. rechercher un document ;
4. inscrire un adhérent ;
5. emprunter et retourner un document ;
6. afficher quelques statistiques.

Le projet fait travailler la programmation orientée objet et les collections :

```text
Enum TypeDocument  → types de documents autorisés
dataclass Document → données d'un document
dataclass Adherent → données d'un adhérent
Mediatheque        → collections et règles d'emprunt
fonctions          → saisies, affichages et menu
```

Les principales collections sont :

```text
dict[int, Document] → catalogue indexé par identifiant
dict[int, Adherent] → adhérents indexés par identifiant
set[str]            → catégories uniques d'un document
set[int]            → documents empruntés par un adhérent
```

Aucun héritage ni package externe n'est nécessaire.

## 1. L'enum `TypeDocument`

Créer un enum contenant les types suivants :

```python
class TypeDocument(Enum):
    LIVRE = "livre"
    BD = "bd"
    FILM = "film"
```

Ajouter une méthode de classe `depuis_choix()` qui transforme la saisie du
menu en type de document :

```text
"1" | "livre" → TypeDocument.LIVRE
"2" | "bd" → TypeDocument.BD
"3" | "film" → TypeDocument.FILM
```

Utiliser `match`. Tout autre choix lève :

```python
ValueError("Type de document invalide.")
```

## 2. La dataclass `Document`

Un document contient :

```text
identifiant  : int
titre        : str
auteur       : str
type_document: TypeDocument
categories   : set[str]
disponible   : bool, égal à True par défaut
```

Dans `__post_init__()` :

- retirer les espaces autour du titre et de l'auteur ;
- lever `ValueError("Le titre est obligatoire.")` si le titre est vide ;
- lever `ValueError("L'auteur est obligatoire.")` si l'auteur est vide ;
- mettre les catégories en minuscules et retirer les doublons.

Exemple :

```python
{" Python ", "programmation", "python"}
```

devient :

```python
{"python", "programmation"}
```

Attention à ne pas partager le même set entre plusieurs documents :

```python
categories: set[str] = field(default_factory=set)
```

La méthode `resume()` retourne une chaîne prête à afficher :

```text
[1] [LIVRE] [DISPONIBLE] Clean Code — Robert C. Martin
[2] [FILM] [EMPRUNTE] Alien — Ridley Scott
```

Les catégories ne sont pas obligatoires dans ce résumé.

## 3. La dataclass `Adherent`

Un adhérent contient uniquement :

```text
identifiant         : int
nom                 : str
documents_empruntes : set[int]
```

Dans `__post_init__()`, retirer les espaces autour du nom et lever
`ValueError("Le nom est obligatoire.")` si le résultat est vide.

Utiliser également `field(default_factory=set)` pour les emprunts.

La dataclass `Adherent` ne contient aucune autre méthode. Elle sert à regrouper
des données liées.

## 4. La classe `Mediatheque`

La médiathèque contient :

```text
documents        : dict[int, Document]
adherents         : dict[int, Adherent]
```

Note: les documents & adhérents ont des indices croissants à partir de 1. Le 'prochain' identifier correspond à la taille actuelle + 1.

Elle possède six méthodes métier.

### `ajouter_document()`

La méthode :

1. construit un `Document` avec le prochain identifiant ;
2. l'ajoute au dictionnaire ;
3. retourne le document créé.

### `inscrire_adherent()`

La méthode suit les mêmes étapes pour construire, enregistrer et retourner un
`Adherent`.

Deux adhérents peuvent porter le même nom : leur identifiant les distingue.

### `rechercher()`

`rechercher(mot_cle)` retourne une liste contenant les documents dont le titre ou l'auteur contient le mot-clé, sans tenir compte de la casse.

Utiliser une compréhension de liste. Une recherche sans résultat retourne une liste vide.

Une recherche vide lève :

```python
ValueError("Le mot-clé est obligatoire.")
```

### `emprunter()`

`emprunter(identifiant_adherent, identifiant_document)` doit :

1. vérifier que l'adhérent existe ;
2. vérifier que le document existe ;
3. vérifier que le document est disponible ;
4. remplacer `document.disponible` par `False` ;
5. ajouter l'identifiant du document au set `documents_empruntes` ;
6. retourner le document.

Erreurs attendues :

```python
KeyError(f"Adhérent {identifiant_adherent} introuvable.")
KeyError(f"Document {identifiant_document} introuvable.")
ValueError("Document déjà emprunté.")
```

### `retourner()`

`retourner(identifiant_adherent, identifiant_document)` vérifie d'abord que l'adhérent et le document existent.

Si l'identifiant du document n'est pas dans le set de l'adhérent, lever :

```python
ValueError("Ce document n'est pas emprunté par cet adhérent.")
```

Sinon, la méthode :

1. remplace `document.disponible` par `True` ;
2. retire l'identifiant du set de l'adhérent ;
3. retourne le document.

### `statistiques()`

Retourner un dictionnaire simple :

```python
{
    "documents": 5,
    "adherents": 2,
    "disponibles": 3,
    "empruntes": 2,
}
```

Les valeurs dépendent de l'état de la médiathèque.

_Vous pouvez utiliser une expression génératrice pour compter les documents disponibles_ :

```python
sum(document.disponible for document in self.documents.values())
```

Le nombre de documents empruntés peut être calculé à partir du nombre total et du nombre de documents disponibles.

## 5. Afficher le catalogue

L'affichage n'a pas besoin d'être une méthode de `Mediatheque`. Faites selon votre préférence.

--
Créer une fonction qui reçoit la médiathèque, parcourt
`mediatheque.documents.values()` et affiche le résumé de chaque document.
OU
Créer une méthode de médiathèque, parcourt
`self.documents.values()` et affiche le résumé de chaque document.

Si le catalogue est vide, afficher :

```text
Aucun document.
```

## 6. Menu attendu

```text
=== MEDIAFLOW ===
1 - Ajouter un document
2 - Afficher le catalogue
3 - Rechercher un document
4 - Inscrire un adhérent
5 - Emprunter un document
6 - Retourner un document
7 - Afficher les statistiques
8 - Quitter
Votre choix :
```

Utiliser `match` pour traiter le choix. Le menu attrape uniquement les erreurs
attendues (`ValueError` et `KeyError`), affiche leur message, puis recommence.

Ne pas utiliser `except Exception`.

## 7. Scénarios de validation

Le projet est terminé si les scénarios suivants fonctionnent :

1. un document et un adhérent peuvent être ajoutés ;
2. leurs identifiants commencent à `1` et augmentent automatiquement ;
3. les catégories sont nettoyées, mises en minuscules et dédupliquées ;
4. deux documents sans catégorie ne partagent pas le même set ;
5. la recherche trouve un mot présent dans un titre ou un auteur ;
6. un adhérent peut emprunter un document disponible ;
7. un document déjà emprunté est refusé ;
8. seul l'adhérent concerné peut retourner son document ;
9. après un retour, le document redevient disponible ;
10. un identifiant inconnu produit un message d'erreur sans arrêter le menu ;
11. les statistiques comptent correctement les documents disponibles et
    empruntés ;
12. le choix `8` termine le programme proprement.

Tester d'abord les classes directement dans la console Python, puis construire
le menu.

## Aide — interfaces possibles

Vous êtes libres de choisir votre découpage. Si vous ne savez pas comment
commencer, vous pouvez utiliser ces signatures :

```python
from dataclasses import dataclass, field
from enum import Enum


class TypeDocument(Enum):
    LIVRE = "livre"
    BD = "bd"
    FILM = "film"

    @classmethod
    def depuis_choix(cls, choix: str) -> "TypeDocument": ...


@dataclass
class Document:
    identifiant: int
    titre: str
    auteur: str
    type_document: TypeDocument
    categories: set[str] = field(default_factory=set)
    disponible: bool = True

    def __post_init__(self) -> None: ...

    def resume(self) -> str: ...


@dataclass
class Adherent:
    identifiant: int
    nom: str
    documents_empruntes: set[int] = field(default_factory=set)

    def __post_init__(self) -> None: ...


class Mediatheque:
    def __init__(self) -> None: ...

    def ajouter_document(
        self,
        titre: str,
        auteur: str,
        type_document: TypeDocument,
        categories: set[str] | None = None,
    ) -> Document: ...

    def inscrire_adherent(self, nom: str) -> Adherent: ...

    def rechercher(self, mot_cle: str) -> list[Document]: ...

    def emprunter(
        self,
        identifiant_adherent: int,
        identifiant_document: int,
    ) -> Document: ...

    def retourner(
        self,
        identifiant_adherent: int,
        identifiant_document: int,
    ) -> Document: ...

    def statistiques(self) -> dict[str, int]: ...


def afficher_catalogue(mediatheque: Mediatheque) -> None: ...


def lancer_mediaflow() -> None: ...


if __name__ == "__main__":
    lancer_mediaflow()
```

Cette interface est une aide, pas une obligation. Les règles métier et les
scénarios de validation restent obligatoires.
