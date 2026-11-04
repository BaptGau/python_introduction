"""NumPy et Pandas : remplacer les `...` par votre code."""

import numpy as np
import pandas as pd


# Exercice 1 : effectuer un calcul vectorisé.
def convertir_en_fahrenheit(temperatures: np.ndarray) -> np.ndarray:
    # Formule : celsius * 9 / 5 + 32.
    # N'utilisez pas de boucle Python et ne modifiez pas le tableau reçu.
    ...


def test_convertir_en_fahrenheit():
    celsius = np.array([-10.0, 0.0, 20.0, 100.0])
    resultat = convertir_en_fahrenheit(celsius)

    np.testing.assert_allclose(resultat, [14.0, 32.0, 68.0, 212.0])
    np.testing.assert_array_equal(celsius, [-10.0, 0.0, 20.0, 100.0])


# Exercice 2 : filtrer avec un masque booléen.
def garder_valeurs_positives(valeurs: np.ndarray) -> np.ndarray:
    # Zéro n'est pas une valeur positive.
    ...


def test_garder_valeurs_positives():
    valeurs = np.array([-3, 0, 7, -1, 4])

    np.testing.assert_array_equal(garder_valeurs_positives(valeurs), [7, 4])


# Exercice 3 : comprendre l'argument axis.
def calculer_moyenne_par_colonne(matrice: np.ndarray) -> np.ndarray: ...


def test_calculer_moyenne_par_colonne():
    matrice = np.array(
        [
            [10.0, 20.0, 30.0],
            [20.0, 40.0, 60.0],
            [30.0, 60.0, 90.0],
        ]
    )

    np.testing.assert_allclose(
        calculer_moyenne_par_colonne(matrice),
        [20.0, 40.0, 60.0],
    )


# Exercice 4 : utiliser le broadcasting.
def centrer_colonnes(matrice: np.ndarray) -> np.ndarray:
    # Soustrayez à chaque valeur la moyenne de sa colonne.
    # N'utilisez pas de boucle Python.
    ...


def test_centrer_colonnes():
    matrice = np.array([[1.0, 10.0], [3.0, 20.0], [5.0, 30.0]])
    resultat = centrer_colonnes(matrice)

    np.testing.assert_allclose(
        resultat,
        [[-2.0, -10.0], [0.0, 0.0], [2.0, 10.0]],
    )
    np.testing.assert_allclose(resultat.mean(axis=0), [0.0, 0.0])


# Exercice 5 : construire un DataFrame.
def creer_ventes() -> pd.DataFrame:
    # Créez puis retournez le DataFrame décrit par les assertions.
    ...


def test_creer_ventes():
    ventes = creer_ventes()

    assert list(ventes.columns) == ["produit", "categorie", "prix", "quantite"]
    assert ventes.to_dict(orient="list") == {
        "produit": ["Livre", "Clavier", "Cahier", "Souris"],
        "categorie": ["Culture", "Informatique", "Papeterie", "Informatique"],
        "prix": [12.0, 50.0, 5.0, 25.0],
        "quantite": [2, 1, 4, 3],
    }


# Exercice 6 : ajouter une colonne avec un calcul vectorisé.
def ajouter_total(ventes: pd.DataFrame) -> pd.DataFrame:
    # Retournez une copie avec une colonne `total` égale à prix * quantite.
    # Le DataFrame reçu ne doit pas être modifié.
    ...


def test_ajouter_total():
    ventes = creer_ventes()
    resultat = ajouter_total(ventes)

    assert resultat["total"].tolist() == [24.0, 50.0, 20.0, 75.0]
    assert "total" not in ventes.columns
    assert resultat is not ventes


# Exercice 7 : filtrer les lignes d'un DataFrame.
def filtrer_par_total_minimum(
    ventes: pd.DataFrame,
    minimum: float,
) -> pd.DataFrame:
    # Gardez les lignes dont le total est supérieur ou égal au minimum.
    ...


def test_filtrer_par_total_minimum():
    ventes = ajouter_total(creer_ventes())
    resultat = filtrer_par_total_minimum(ventes, 50.0)

    assert resultat["produit"].tolist() == ["Clavier", "Souris"]
    assert resultat["total"].tolist() == [50.0, 75.0]


# Exercice 8 : traiter les valeurs manquantes.
def remplacer_prix_manquants(ventes: pd.DataFrame) -> pd.DataFrame:
    # Dans une copie, remplacez les prix manquants par la moyenne des prix connus.
    ...


def test_remplacer_prix_manquants():
    ventes = pd.DataFrame(
        {
            "produit": ["Livre", "Clavier", "Cahier"],
            "prix": [10.0, np.nan, 20.0],
        }
    )
    resultat = remplacer_prix_manquants(ventes)

    assert resultat["prix"].tolist() == [10.0, 15.0, 20.0]
    assert pd.isna(ventes.loc[1, "prix"])


# Exercice 9 : regrouper puis agréger.
def calculer_total_par_categorie(ventes: pd.DataFrame) -> pd.Series:
    # Calculez la somme de `total` par catégorie et triez l'index.
    ...


def test_calculer_total_par_categorie():
    ventes = ajouter_total(creer_ventes())
    resultat = calculer_total_par_categorie(ventes)
    attendu = pd.Series(
        [24.0, 125.0, 20.0],
        index=["Culture", "Informatique", "Papeterie"],
        name="total",
    )

    pd.testing.assert_series_equal(resultat, attendu)
