# n! -> produit de 1 à n
# n * n-1 * n-2 * ... * 1

def factorielle(n: int) -> int | None:
    if n <= 0:
        print(f"Factorielle prend un nombre positif en entrée. Nombre donné: {n}")
        return
    if n == 1:
        return n
    else:
        return n*factorielle(n-1)


if __name__ == "__main__":
    print(factorielle(5))