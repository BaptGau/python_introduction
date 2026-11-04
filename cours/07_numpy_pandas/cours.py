import time

import numpy as np
import pandas as pd


def track_time(fn, arr) -> float:
    start = time.monotonic()
    fn(arr)
    return time.monotonic() - start


def add_numpy(arr):
    np.sum(arr)


def add_python(arr):
    sum(arr)


def bench():
    arr_nombres = np.arange(1, 100_000_001)

    temps_python = track_time(add_python, [i for i in range(1, 100_000_001)])

    temps_numpy = track_time(add_numpy, arr_nombres)

    print(f"Temps python: {temps_python}")
    print(f"Temps numpy: {temps_numpy}")
    print(f"Gain numpy: {temps_python / temps_numpy}")


def first_steps():
    notes = np.array([12, 15, 9, 18])
    zeros = np.zeros(3)  # [0., 0., 0.]
    suite = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

    print(notes[0])  # 12
    print(notes[-1])  # 18
    print(notes[1:3])  # array([15, 9])

    print(notes * 2)
    print(notes - 10)
    print(notes.sum(axis=0))

    np.sum(notes, axis=0)

    valeurs = np.array([1, 2, 3, 4])
    vue = valeurs[1:3]
    print(vue)

    vue[0] = 99

    print(valeurs)


def first_steps_pandas():
    ventes = pd.DataFrame(
        {
            "produit": ["Livre", "Clavier", "Livre"],
            "categorie": ["Culture", "Informatique", "Culture"],
            "prix": [12.0, 50.0, 12.0],
            "quantite": [2, 1, 3],
        }
    )

    print(ventes.shape)
    print(ventes.dtypes)
    print(ventes.head(5))

    print(ventes["prix"])  # une Series
    print(ventes[["produit", "prix"]])  # un DataFrame

    print(ventes.loc[0, "produit"])  # sélection par labels
    print(ventes.iloc[0, 2])  # sélection par positions

    cheres = ventes.loc[ventes["prix"] >= 20]

    print(cheres)

    ventes["total"] = ventes["prix"] * ventes["quantite"]

    print(ventes)

    total_par_categorie = ventes.groupby("categorie")[["quantite", "total"]].sum()

    print(total_par_categorie)


if __name__ == "__main__":
    # bench()

    first_steps_pandas()
