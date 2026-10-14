# tuples
t = (0, 1, 2)
t2 = (1, 2, 3, 4)

t3 = (t[0] + t2[0], ...)

# list, str, tuple
t3 = (1, "bonjour", "python", True, None)
s = "Bonjour"


def fn(x, y) -> tuple[int, str, bool]:
    return x + y, str(x + y), True


# list
def list_ex():
    ma_liste = [0, 1, 2]
    ma_liste[0] = 10

    l = [i for i in range(11)]

    print(sum(l))

    t = (0, 1, 2)


# dict
def exemple_dict():
    mon_dict = {}
    mon_dict["cle"] = 10

    notes = {}

    mon_dict[(0, 0)] = 10
    notes["Baptiste"] = 20
    notes["Aurélien"] = 12

    for key in notes:
        print(key)

    for value in notes.values():
        print(value)

    for key, value in notes.items():
        print(f"{key}: {value}")

    d = {f"indice_{i}": i for i in range(11)}

    print(d)


def exemple_for():
    squared_erreurs = [10, 12, 13, 10]
    somme = 0

    for err in squared_erreurs:
        somme += err

    print(somme)


def fn(s: str) -> str:
    s += " modifiée !"
    return s


def fn_2(l: list) -> None:
    l.append("modifiée !")


if __name__ == "__main__":
    s = "chaine"
    l = ["liste"]

    fn(s)
    fn_2(l)

    print(s)
    print(l)

    # list_ex()
    # exemple_dict()
#
#     print(t[0])
#     print(t2[1])
#
#     print(t3[3])  # affiche quoi ?
#
#     call = fn(10, 3)
#
#     print(type(call))
#     print(call)
