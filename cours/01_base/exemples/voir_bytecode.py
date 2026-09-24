"""Afficher le bytecode produit par CPython pour une petite fonction."""

import dis


def saluer(prenom: str, age: int) -> str:
    message = "Bonjour " + prenom
    message = message + f"\nTu as {age} ans"
    return message


if __name__ == "__main__":
    print("Résultat :", saluer("Ada", 20))
    print("\nBytecode de saluer() :")
    dis.dis(saluer)
