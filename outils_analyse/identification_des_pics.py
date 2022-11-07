import numpy as np
from scipy.signal import find_peaks


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
