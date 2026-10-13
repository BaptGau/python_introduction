def fonction(prenom: str, age: int) -> str:
    return f"Bonjour {prenom}, vous avez {age} ans"


def afficher_addition(a: int, b: int) -> int | None:
    # "Bonjour".uppercase() -> "BONJOUR"
    addition_result = a + b
    return addition_result


def fn(a, b):
    return a + b


def addition(valeur_1: int, valeur_2: int) -> int:
    return valeur_1 + valeur_2


# def <nom_de_la_fonction>(<arguments typés>) -> <type de sortie>:
#    <body de la fonction>


def main():
    resultat = addition(a=10, b=5, c=15, d=20)
    print(resultat)


if __name__ == "__main__":
    main()
