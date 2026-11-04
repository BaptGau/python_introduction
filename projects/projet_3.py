from dataclasses import dataclass, field
from enum import Enum


class TypeDocument(Enum):
    LIVRE = "livre"
    BD = "bd"
    FILM = "film"

    @classmethod
    def depuis_choix(cls, entree: str):
        match entree:
            case "1" | "livre":
                return cls.LIVRE
            case "2" | "bd":
                return cls.BD
            case "3" | "film":
                return cls.FILM
            case _:
                raise ValueError("Type de document invalide.")


@dataclass
class Document:
    identifiant: int
    titre: str
    auteur: str
    type_document: TypeDocument
    categories: set[str] = field(default_factory=set)
    disponible: bool = True

    def __post_init__(self):

        if not self.titre:
            raise ValueError("Le titre est obligatoire.")
        if not self.auteur:
            raise ValueError("L'auteur est obligatoire.")

        self.titre = self.titre.strip()
        self.auteur = self.auteur.strip()

        self.categories = {c.lower() for c in self.categories}

    def resume(self) -> str:
        return f"[{self.identifiant}] [{self.type_document.name}] {self.titre} - {self.auteur}"


@dataclass
class Adherent:
    identifiant: int
    nom: str
    documents_empruntes: set[int] = field(default_factory=set)

    def __post_init__(self):
        self.nom = self.nom.strip()

        if not self.nom:
            raise ValueError("Le nom est obligatoire.")


class Mediatheque:
    def __init__(
        self,
        documents: dict[int, Document] | None = None,
        adherents: dict[int, Adherent] | None = None,
    ):
        self.documents = documents if documents else {}
        self.adherents = adherents if adherents else {}

    def ajouter_document(
        self,
        titre: str,
        auteur: str,
        type_document: TypeDocument,
        categories: set[str] | None = None,
    ) -> Document:
        nouveau_doc = Document(
            identifiant=len(self.documents) + 1,
            titre=titre,
            auteur=auteur,
            type_document=type_document,
            categories=categories or set(),
        )

        self.documents[nouveau_doc.identifiant] = nouveau_doc

        return nouveau_doc

    def inscrire_adherent(self, nom: str) -> Adherent:
        nouveau_adherent = Adherent(identifiant=len(self.adherents) + 1, nom=nom)

        self.adherents[nouveau_adherent.identifiant] = nouveau_adherent

        return nouveau_adherent

    def rechercher(self, mot_cle: str) -> list[Document]:
        if not mot_cle:
            raise ValueError("Le mot-clé est obligatoire.")

        return [
            doc
            for doc in self.documents.values()
            if mot_cle in doc.titre or mot_cle in doc.auteur
        ]

    def emprunter(
        self,
        identifiant_adherent: int,
        identifiant_document: int,
    ) -> Document:

        adherent = self.adherents.get(identifiant_adherent, None)
        document = self.documents.get(identifiant_document, None)

        if not adherent:
            raise KeyError(f"Adhérent {identifiant_adherent} introuvable.")
        if not document:
            raise KeyError(f"Document {identifiant_document} introuvable.")

        if not document.disponible:
            raise ValueError("Document déjà emprunté.")

        document.disponible = False
        adherent.documents_empruntes.add(document.identifiant)

        return document

    def retourner(
        self,
        identifiant_adherent: int,
        identifiant_document: int,
    ) -> Document:

        adherent = self.adherents.get(identifiant_adherent, None)
        document = self.documents.get(identifiant_document, None)

        if not adherent:
            raise KeyError(f"Adhérent {identifiant_adherent} introuvable.")
        if not document:
            raise KeyError(f"Document {identifiant_document} introuvable.")

        if not document.identifiant in adherent.documents_empruntes:
            raise ValueError("Ce document n'est pas emprunté par cet adhérent.")

        document.disponible = True
        adherent.documents_empruntes.remove(document.identifiant)

        return document

    def statistiques(self) -> dict[str, int]:
        return {
            "documents": len(self.documents),
            "adherents": len(self.adherents),
            "disponibles": len(
                [doc for doc in self.documents.values() if doc.disponible]
            ),
            "empruntes": len(
                [doc for doc in self.documents.values() if not doc.disponible]
            ),
        }

    def afficher_catalogue(self) -> str:
        if not self.documents:
            return "Aucun document."

        repr = ""

        for doc in self.documents.values():
            repr += doc.resume() + "\n"
        return repr.strip()


MENU = """
=== MEDIAFLOW ===
1 - Ajouter un document
2 - Afficher le catalogue
3 - Rechercher un document
4 - Inscrire un adhérent
5 - Emprunter un document
6 - Retourner un document
7 - Afficher les statistiques
8 - Quitter
""".strip()


def main():
    mediatheque = Mediatheque()

    while True:
        print(MENU)

        choice = input("Votre choix: ")

        match choice:
            case "1":
                titre = input("Titre: ")
                auteur = input("Auteur: ")
                type_doc = TypeDocument.depuis_choix(entree=input("Type document: "))

                mediatheque.ajouter_document(
                    titre=titre, auteur=auteur, type_document=type_doc
                )
            case "2":
                print(mediatheque.afficher_catalogue())
            case "3":
                mot_cle = input("Mot clé: ")

                print(mediatheque.rechercher(mot_cle=mot_cle))

            case "4":
                nom_adherent = input("Nom adherent: ")
                print(mediatheque.inscrire_adherent(nom_adherent))

            case "5":
                id_doc = int(input("Identifiant document: "))
                id_adherent = int(input("Identifiant adhérent: "))

                print(
                    mediatheque.emprunter(
                        identifiant_adherent=id_adherent,
                        identifiant_document=id_doc,
                    )
                )

            case "6":
                id_doc = int(input("Identifiant document: "))
                id_adherent = int(input("Identifiant adhérent: "))

                print(
                    mediatheque.retourner(
                        identifiant_adherent=id_adherent,
                        identifiant_document=id_doc,
                    )
                )

            case "7":
                print(mediatheque.statistiques())

            case "8":
                return

            case _:
                raise ValueError("Choix non supporté.")


if __name__ == "__main__":
    main()
