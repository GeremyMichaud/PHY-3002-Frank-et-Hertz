import numpy as np
from scipy.signal import find_peaks


def determiner_approx_indexes_maximums(valeurs, colonne_y, zero_threshold, voisins, average_within,
                                       filtre_min, signe_check_range):
    """

    :param filtre_min:
    :param valeurs:
    :param colonne_x:
    :param colonne_y:
    :return:
    """
    derive_premiere = valeurs[2 * voisins:, colonne_y] - valeurs[:-2 * voisins, colonne_y]
    derive_deuxieme = derive_premiere[2 * voisins:] - derive_premiere[:-2 * voisins]
    derive_premiere_zero = np.logical_and((derive_premiere > -zero_threshold), derive_premiere < zero_threshold)
    derive_deuxieme_zero = np.logical_and((derive_deuxieme > -zero_threshold), derive_deuxieme < zero_threshold)
    max_or_min = np.logical_and(derive_premiere_zero[voisins:-voisins], derive_deuxieme_zero)
    max_or_min_filtre = np.logical_and(max_or_min, valeurs[2 * voisins:-2 * voisins, colonne_y] > filtre_min)
    index_max_or_min, = np.where(max_or_min_filtre)
    moyenne_nuage_max_or_min = _moyenne_nuage_point(index_max_or_min, average_within)
    final_indexes = []
    for index in moyenne_nuage_max_or_min:
        try:
            if derive_premiere[index + voisins - signe_check_range:index + voisins].mean() > 0:
                final_indexes.append(index)
        except IndexError:
            if derive_premiere[index + voisins: index + voisins + signe_check_range].mean() < 0:
                final_indexes.append(index)

    return np.asarray(final_indexes) + 2 * voisins


def _moyenne_nuage_point(indices, range_moyenne):
    liste_a_moyenner = []
    moyenne = []
    for indexes in indices:
        if len(moyenne) == 0:
            moyenne.append(indexes)
        elif indexes - moyenne[0] < range_moyenne:
            moyenne.append(indexes)
        else:
            liste_a_moyenner.append(int(np.asarray(moyenne).mean()))
            moyenne = [indexes]

    liste_a_moyenner.append(int(np.asarray(moyenne).mean()))

    return np.asarray(liste_a_moyenner)


def determiner_indexes_maximums_scipy(valeurs: np.array, colonne_y: int,
                                      hauteur_minimum: int = None,
                                      distance_minumum: int = None):
    """
    Cette méthode utilise la méthode find_peaks de scipy pour trouver les index de l'array correspondant aux maximums.

    :param valeurs: array contenant toutes les valeurs
    :param colonne_y: index de la colonne contenant les valeurs dépendantes
    :param hauteur_minimum: Optionnel! Celui-ci indique la hauteur minimale entre
                            deux pics pour guider l'algorithme de scipy
    :param distance_minumum:Optionnel! Celui-ci indique la distance minimale entre
                            deux pics pour guider l'algorithme de scipy

    :return: liste des index correspondant aux emplacements des maximums
    """
    peaks, _ = find_peaks(valeurs[:, colonne_y], height=hauteur_minimum, distance=distance_minumum)
    return peaks
