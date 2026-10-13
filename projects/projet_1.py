# Config set
CODE_SECRET = "1234"
SOLDE_INITIAL = 500
MAX_ESSAIS = 3
PLAFOND_RETRAIT = 300

MENU = """
=== MINI-DISTRIBUTEUR ===
1 - Consulter le solde
2 - Déposer de l'argent
3 - Retirer de l'argent
4 - Quitter
""".strip()


def authentification(code_secret: str, essais: int) -> bool:
    if essais <= 0:
        print("Le nombre d'essais n'est pas valide")
        return False

    compteur = essais

    while compteur > 0:
        code = input("Quel est le code secret: ")
        if code == code_secret:
            return True
        compteur -= 1

    return False


def afficher_solde(solde: int) -> None:
    print(f"Solde disponible: {solde} €.")

def depot(solde: int, montant: int) -> int:
    if montant < 0:
        print("Montant invalide. Solde non modifié.")
        return solde

    solde += montant
    print(f"Dépôt accepté. Nouveau solde : {solde} €")

    return solde

def retrait(solde: int, montant: int, plafond: int) -> int:
    if montant < 0:
        print("Montant invalide. Solde non modifié.")
        return solde

    if montant > solde:
        print("Montant > solde. Pas de modification.")
        return solde

    if montant > plafond:
        print("Montant > plafond. Pas de modification.")
        return solde

    solde -= montant

    print(f"Retrait accepté. Nouveau solde: {solde} €")

    return solde

def main(
    solde_initial: int = SOLDE_INITIAL,
    code_secret: str = CODE_SECRET,
    essais: int = MAX_ESSAIS,
    plafond: int = PLAFOND_RETRAIT
):
    can_enter = authentification(code_secret=code_secret, essais=essais)

    if not can_enter:
        print("Erreur lors de l'authentification !")
        return

    should_run = True
    solde = solde_initial

    while should_run:
        print(MENU)
        choice = input("Votre choix: ")
        match choice:
            case "1":
                afficher_solde(solde=solde)
            case "2":
                montant = int(input("Montant du dépôt: "))
                solde = depot(solde=solde, montant=montant)
            case "3":
                montant = int(input("Montant du retrait: "))
                solde = retrait(solde=solde, montant=montant, plafond=plafond)
            case "4":
                should_run = False


if __name__ == "__main__":
    main()
