stock: dict[str, int] = {
    "clavier": 5,
    "souris": 2,
    "ecran": 0,
}

type Historique = list[tuple[str, str, int]]

historique: Historique = []

MENU = """
=== STOCKFLOW ===
1 - Afficher le stock
2 - Ajouter un produit
3 - Enregistrer une entrée
4 - Enregistrer une sortie
5 - Afficher l'historique
6 - Afficher les statistiques
7 - Quitter
""".strip()


def saisie_entier(msg: str = "Quantité saisie: ") -> int:
    while True:
        try:
            entier = int(input(msg))
            if entier > 0:
                return entier
            raise ValueError("Entier invalide")
        except ValueError:
            print("Vous devez entrer un nombre entier positif.")


def afficher_stock(stock: dict[str, int]) -> None:
    print("=== STOCK ===")
    for item, count in stock.items():
        if count <= 1:
            print(f"{item} : {count} unité")
        else:
            print(f"{item} : {count} unités")


def ajouter_produit(stock: dict[str, int]) -> dict[str, int]:
    nom = input("Nom: ").strip().lower()
    qte = saisie_entier("Quantité initiale: ")

    if not nom:
        raise ValueError("Nom invalide.")

    if nom in stock:
        raise ValueError("Le produit existe déjà.")

    stock[nom] = qte
    print(f"Produit '{nom}' ajouté.")

    return stock


def enregistrer_entree(
    stock: dict[str, int], historique: Historique
) -> tuple[dict[str, int], Historique]:
    produit = input("Produit: ").strip().lower()
    qte = saisie_entier("Quantité reçue: ")

    if produit not in stock:
        raise KeyError("Produit non présent dans le stock")

    stock[produit] += qte
    historique.append(("entree", produit, qte))

    print(f"Entrée enregistrée. Nouveau stock : {stock[produit]}")

    return stock, historique


def enregistrer_sortie(
    stock: dict[str, int], historique: Historique
) -> tuple[dict[str, int], Historique]:

    produit = input("Produit: ").strip().lower()
    qte = saisie_entier("Quantité vendue: ")

    if produit not in stock:
        raise KeyError("Produit non présent dans le stock")

    if qte > stock[produit]:
        raise ValueError("Stock insuffisant.")

    stock[produit] -= qte
    historique.append(("sortie", produit, qte))

    print(f"Sortie enregistrée. Nouveau stock : {stock[produit]}")

    return stock, historique


def afficher_historique(historique: Historique) -> None:
    for type_mouvement, produit, quantite in historique:
        print(f"{type_mouvement.upper()} - {produit} - {quantite}")


def afficher_stats(stock: dict[str, int]) -> None:
    diff_prod = len(stock)
    qte_totale = sum(qte for qte in stock.values())
    rupture = [produit for produit in stock if stock[produit] == 0]

    print("=== STATISTIQUES ===")
    print(f"Produits différents: {diff_prod}")
    print(f"Unités disponibles: {qte_totale}")
    print(f"Produits en rupture: {rupture}")


def main(stock: dict[str, int], historique: Historique) -> None:

    while True:
        choice = input("Votre choix: ")

        match choice:
            case "1":
                afficher_stock(stock)
            case "2":
                try:
                    stock = ajouter_produit(stock)
                except ValueError:
                    print("Erreur lors de l'ajout d'un produit. Stock non modifié.")
            case "3":
                try:
                    stock, historique = enregistrer_entree(stock, historique)
                except ValueError as erreur:
                    print(f"Value errror: {erreur}")
                except KeyError as erreur:
                    print(f"Key errror: {erreur}")
            case "4":
                try:
                    stock, historique = enregistrer_sortie(stock, historique)
                except ValueError as erreur:
                    print(erreur)
                except KeyError as erreur:
                    print(erreur)
            case "5":
                afficher_historique(historique)
            case "6":
                afficher_stats(stock)
            case "7":
                return
            case _:
                print("Option invalide, veuillez ré-essayer.")


if __name__ == "__main__":
    # stock, historique = enregistrer_sortie(stock, historique)

    # historique.append(("entree", "clavier", 4))
    # historique.append(("sortie", "souris", 1))

    # afficher_historique(historique=historique)

    main(stock, historique)
