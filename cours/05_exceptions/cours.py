def ex_1():
    try:
        age = int(input("Âge: "))
        age /= int(input("Par combien voulez vous diviser cet âge: "))

    except ValueError:
        print("L'âge doit être un entier.")

    except ZeroDivisionError as err:
        print(err)
        print("Le diviseur ne doit pas être nul")

    else:
        print("Tout a bien fonctionné")

    finally:
        print("Fin")


if __name__ == "__main__":
    ex_1()
