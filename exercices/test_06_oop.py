"""POO : compléter les classes et dataclasses."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Self, TypedDict

import pytest


# Exercice 1 : construire une classe simple.
class Rectangle:
    def __init__(self, longueur: float, largeur: float) -> None:
        # Créez les attributs d'instance `longueur` et `largeur`.
        ...

    def calculer_aire(self) -> float: ...

    def calculer_perimetre(self) -> float: ...


def test_rectangle():
    rectangle = Rectangle(5.0, 3.0)

    assert rectangle.longueur == 5.0
    assert rectangle.largeur == 3.0
    assert rectangle.calculer_aire() == 15.0
    assert rectangle.calculer_perimetre() == 16.0


# Exercice 2 : utiliser une classmethod et une staticmethod.
class Utilisateur:
    def __init__(self, nom: str, email: str) -> None:
        self.nom = nom
        self.email = email

    @classmethod
    def depuis_texte(cls, texte: str) -> "Utilisateur":
        # Le format attendu est "nom;email".
        # Validez l'email avec `cls.email_est_valide()` et levez ValueError si
        # celui-ci est invalide.
        # Retournez une instance avec `cls(...)`, pas `Utilisateur(...)`.
        ...

    @staticmethod
    def email_est_valide(email: str) -> bool:
        # Un email valide contient exactement un `@`, avec du texte avant et
        # après. Cette validation est volontairement simplifiée.
        ...


def test_utilisateur_depuis_texte():
    utilisateur = Utilisateur.depuis_texte("Ada;ada@example.com")

    assert isinstance(utilisateur, Utilisateur)
    assert utilisateur.nom == "Ada"
    assert utilisateur.email == "ada@example.com"


def test_depuis_texte_utilise_cls():
    class Administrateur(Utilisateur):
        pass

    administrateur = Administrateur.depuis_texte("Grace;grace@example.com")

    assert isinstance(administrateur, Administrateur)


def test_email_est_valide():
    assert Utilisateur.email_est_valide("ada@example.com") is True
    assert Utilisateur.email_est_valide("ada.example.com") is False
    assert Utilisateur.email_est_valide("@example.com") is False
    assert Utilisateur.email_est_valide("ada@") is False
    assert Utilisateur.email_est_valide("ada@@example.com") is False

    with pytest.raises(ValueError, match="Email invalide"):
        Utilisateur.depuis_texte("Ada;adresse-invalide")


# Exercice 3 : compléter une dataclass avec une méthode d'instance.
@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int = 0

    def calculer_valeur_stock(self) -> float: ...


def test_produit_dataclass():
    clavier = Produit("Clavier", 49.99, 3)

    assert clavier.nom == "Clavier"
    assert clavier.prix == 49.99
    assert clavier.quantite == 3
    assert clavier.calculer_valeur_stock() == pytest.approx(149.97)

    # Une dataclass compare automatiquement ses champs.
    assert clavier == Produit("Clavier", 49.99, 3)
    assert repr(clavier) == "Produit(nom='Clavier', prix=49.99, quantite=3)"


# Exercice 4 : classmethod et staticmethod dans une dataclass.
@dataclass
class Temperature:
    celsius: float

    @classmethod
    def depuis_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        # Formule : (fahrenheit - 32) * 5 / 9
        # Levez ValueError si la température obtenue n'est pas valide.
        ...

    @staticmethod
    def celsius_est_valide(celsius: float) -> bool:
        # Le zéro absolu vaut -273.15 °C.
        ...


def test_temperature_depuis_fahrenheit():
    zero = Temperature.depuis_fahrenheit(32)
    ebullition = Temperature.depuis_fahrenheit(212)

    assert zero.celsius == pytest.approx(0.0)
    assert ebullition.celsius == pytest.approx(100.0)


def test_temperature_validation():
    assert Temperature.celsius_est_valide(-273.15) is True
    assert Temperature.celsius_est_valide(-273.16) is False

    with pytest.raises(ValueError, match="Température invalide"):
        Temperature.depuis_fahrenheit(-500)


# Exercice 5 : donner une liste différente à chaque instance.
@dataclass
class Panier:
    proprietaire: str
    produits: list[str] = field(default_factory=list)

    def ajouter(self, produit: str) -> None: ...


def test_panier_default_factory():
    panier_ada = Panier("Ada")
    panier_grace = Panier("Grace")

    panier_ada.ajouter("Clavier")

    assert panier_ada.produits == ["Clavier"]
    assert panier_grace.produits == []
    assert panier_ada.produits is not panier_grace.produits


# Exercice 6 : associer une enum et une dataclass.
class StatutTache(Enum):
    A_FAIRE = ...
    TERMINEE = ...


@dataclass
class Tache:
    titre: str
    statut: StatutTache = StatutTache.A_FAIRE

    def terminer(self) -> None: ...


def test_tache_et_enum():
    tache = Tache("Terminer les exercices")

    assert tache.statut is StatutTache.A_FAIRE

    tache.terminer()

    assert tache.statut is StatutTache.TERMINEE
    assert StatutTache.A_FAIRE.value == "a_faire"
    assert StatutTache.TERMINEE.value == "terminee"


# Exercice 7 : composer une dataclass à partir d'autres dataclasses.
@dataclass
class Adresse:
    rue: str
    ville: str
    code_postal: str


@dataclass
class Coordonnees:
    email: str
    telephone: str


@dataclass
class Client:
    nom: str
    adresse: Adresse
    coordonnees: Coordonnees

    def etiquette(self) -> str:
        # Utilisez les attributs de la dataclass `Adresse` contenue dans le
        # client. Le format attendu est "nom - rue, code_postal ville".
        ...


def test_composition_dataclasses():
    adresse = Adresse("1 rue de Python", "Paris", "75001")
    coordonnees = Coordonnees("ada@example.com", "01 23 45 67 89")
    client = Client("Ada Lovelace", adresse, coordonnees)

    assert client.adresse is adresse
    assert client.coordonnees is coordonnees
    assert client.adresse.ville == "Paris"
    assert client.coordonnees.email == "ada@example.com"
    assert client.etiquette() == "Ada Lovelace - 1 rue de Python, 75001 Paris"


# Exercice 8 : utiliser une méthode de classe pour construire une dataclass.
@dataclass
class Livre:
    titre: str
    auteur: str
    annee: int

    @classmethod
    def depuis_texte(cls, texte: str) -> "Livre":
        # Le format attendu est "titre;auteur;annee".
        # Convertissez l'année en entier et construisez l'objet avec `cls(...)`.
        ...


def test_livre_depuis_texte():
    livre = Livre.depuis_texte("Les Misérables;Victor Hugo;1862")

    assert livre == Livre("Les Misérables", "Victor Hugo", 1862)
    assert isinstance(livre.annee, int)


def test_livre_depuis_texte_utilise_cls():
    @dataclass
    class Oeuvre:
        titre: str

        @classmethod
        def depuis_livre(cls, livre: Livre) -> Self: ...

    livre = Livre(titre="Les Misérables", auteur="Victor Hugo", annee=1862)
    oeuvre = Oeuvre.depuis_livre(livre)

    assert isinstance(oeuvre, Oeuvre)
    assert oeuvre.titre == livre.titre


# Exercice 9 : parser du texte en enum avec `match`.
class NiveauJournal(Enum):
    INFO = "info"
    AVERTISSEMENT = "avertissement"
    ERREUR = "erreur"

    @classmethod
    def depuis_texte(cls, texte: str) -> "NiveauJournal":
        # Utilisez `match` pour accepter les textes "info", "avertissement"
        # et "erreur". Levez ValueError("Niveau inconnu") pour toute autre
        # valeur.
        ...


def test_niveau_journal_depuis_texte():
    assert NiveauJournal.depuis_texte("info") is NiveauJournal.INFO
    assert NiveauJournal.depuis_texte("avertissement") is NiveauJournal.AVERTISSEMENT
    assert NiveauJournal.depuis_texte("erreur") is NiveauJournal.ERREUR


def test_niveau_journal_inconnu():
    with pytest.raises(ValueError, match="Niveau inconnu"):
        NiveauJournal.depuis_texte("debug")


# Exercice 10 : décrire un dictionnaire avec des clés et des types connus.
class LigneCommande(TypedDict):
    produit: str
    quantite: int
    prix_unitaire: float


def calculer_total_ligne(ligne: LigneCommande) -> float:
    # Accédez aux valeurs avec leurs clés et calculez :
    # quantite * prix_unitaire.
    ...


def test_ligne_commande_typed_dict():
    ligne: LigneCommande = {
        "produit": "Clavier",
        "quantite": 3,
        "prix_unitaire": 49.99,
    }

    # Un TypedDict reste un dictionnaire à l'exécution.
    assert isinstance(ligne, dict)
    assert ligne["produit"] == "Clavier"
    assert calculer_total_ligne(ligne) == pytest.approx(149.97)


def test_ligne_commande_decrit_les_cles_attendues():
    assert LigneCommande.__required_keys__ == {
        "produit",
        "quantite",
        "prix_unitaire",
    }
