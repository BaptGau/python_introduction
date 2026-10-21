from dataclasses import dataclass
from enum import Enum, auto
from typing import Self, TypedDict


class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: int = 0) -> None:
        self.titulaire = titulaire
        self._solde = solde_initial

    def consulter_solde(self) -> int:
        return self._solde

    def deposer(self, montant: int) -> None:
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")

        self._solde += montant

    def retirer(self, montant: int) -> None:
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")

        if montant > self._solde:
            raise ValueError("Solde insuffisant.")

        self._solde -= montant


# state-full vs state-less


def deposer(solde: int, montant: int) -> int:
    if montant <= 0:
        raise ValueError("Le montant doit être positif.")

    solde += montant

    return solde


def retirer(solde, montant: int) -> int:
    if montant <= 0:
        raise ValueError("Le montant doit être positif.")

    if montant > solde:
        raise ValueError("Solde insuffisant.")

    solde -= montant

    return solde


compte = CompteBancaire(titulaire="Baptiste Gautier", solde_initial=100)
compte.deposer(1000)
print(compte.consulter_solde())

solde = 100
solde = deposer(solde, 1000)
print(solde)


# -------
d = {}


@dataclass
class TestResult:
    p_value: float
    conclusion: str


@dataclass
class Produit:
    nom: str
    prix: float
    quantite: int = 0


t_test_result = TestResult(p_value=0.3, conclusion="La conclusion est que...")
prod = Produit(nom="clavier", prix=50, quantite=1)

print(prod)


# -------
class MonDictionnaire(TypedDict):
    nom: str
    prix: float
    quantite: int


d = MonDictionnaire(nom="bonjour", prix=4, quantite=1)
print(d)


# ------
class MonPetitEnum(Enum):
    AFFICHER_STOCK = auto()
    ENREGISTRER_ENTREE = auto()
    ENREGISTRER_SORTIE = auto()

    @classmethod
    def parse(cls, s: str):
        match s:
            case "afficher_stock":
                return cls.AFFICHER_STOCK
            case "enregistrer_entree":
                return cls.ENREGISTRER_ENTREE
            case "enregistrer_sortie":
                return cls.ENREGISTRER_SORTIE
            case _:
                raise ValueError()


def fn(entree: MonPetitEnum):
    match entree:
        case MonPetitEnum.AFFICHER_STOCK:
            ...
        case MonPetitEnum.ENREGISTRER_ENTREE:
            ...
        case MonPetitEnum.ENREGISTRER_SORTIE:
            ...
        case _:
            ...
