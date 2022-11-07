"""
------------------------------------------------------------------------------

Pour vous faciliter la vie, vous pouvez utiliser le code présent dans le dossier
outils_analyse.

_____________________________________________________________________________
"""
"""
------------------------------------------------------------------------------

Mettres vois import ici

_____________________________________________________________________________
"""
from outils_analyse.identification_des_pics import determiner_indexes_maximums_scipy
from outils_analyse.lecture_des_fichiers import lire_csv_a_3_colonnes, crop_pour_conserver_que_la_partie_avec_rampe
from outils_analyse.conversion_temps_en_potentiel import \
    calculer_facteur_conversion_temps_en_potentiel_avec_mesure_rampe
import matplotlib.pyplot as plt
import os
import matplotlib
# Grosseur du text dans les figures
matplotlib.rcParams.update({'font.size': 18})
"""
------------------------------------------------------------------------------

Lire le fichier des résultats et transformer les valeurs en un array numpy

_____________________________________________________________________________
"""
# Mettre votre code ici












# Mettre vos valuers extraites à la place du None.
valeurs_en_array = None  # Array de trois colonnes

"""
_____________________________________________________________________________
"""
# Ne pas modifier cette section!!!

# La figure obtenue devrait correspondre à celle de figures_exemple/lecture_des_donnes_brutes
plt.figure()
plt.plot(valeurs_en_array[:, 0], valeurs_en_array[:, 2], label="Tensions du pico")
plt.plot(valeurs_en_array[:, 0], valeurs_en_array[:, 1], label="Tensions entre la G1 et le ground")
plt.xlabel("Temps [s]")
plt.ylabel("Tension [V]")
plt.legend()
plt.show()

"""
------------------------------------------------------------------------------

Retirer les valeurs qui se trouvent à l'extérieur de l'activation du générateur de rampe.
Ne pas oublier de mettre le début de la rampe comme étant t=0.

_____________________________________________________________________________
"""
# Mettre votre code ici













# Mettre vos données croppé remise à t_0=0 dans cette variable
valeurs_cropped_debutant_par_t0 = None  # Array de trois colonnes

"""
_____________________________________________________________________________
"""
# Ne pas modifier cette section!!!

# La figure obtenue devrait correspondre à celle de figures_exemple/donnes_cropped
plt.figure()
plt.plot(valeurs_cropped_debutant_par_t0[:, 0], valeurs_cropped_debutant_par_t0[:, 2],
         label="Tensions du pico")
plt.plot(valeurs_cropped_debutant_par_t0[:, 0], valeurs_cropped_debutant_par_t0[:, 1],
         label="Tensions entre la G1 et le ground")
plt.xlabel("Temps [s]")
plt.ylabel("Tension [V]")
plt.legend()
plt.show()
"""
------------------------------------------------------------------------------

Calculer la pente de la tension du générateur de rampe et son incertitude.
Afficher cette valeur et son incertitude, puis convertir les valeurs de temps
en valeurs de tension. La valeur devrait être près de: Pente =  -0.44003644585609436 +- 0.031069057062268257 V/s

Ensuite, convertissez les valeurs de tensions du pico en valeur de courant, en considérant que l'échelle
du pico utilisé est de 3nA. 
_____________________________________________________________________________
"""
# Mettre votre code ici







# Mettre vos données avec les bonnes unités à la place et vos informations par rapport à la pente ici
valeurs_avec_bonnes_unites = None  # Array de trois colonnes
facteur_valeur = None  # Nombre à virgule
facteur_incertitude = None  # Nombre à virgule

"""
_____________________________________________________________________________
"""
# Ne pas modifier cette section!!!

print("Pente = ", f"{facteur_valeur} +- {facteur_incertitude}")

# La figure obtenue devrait correspondre à celle de figures_exemple/donnes_avec_bonnes_unités
plt.figure()
plt.plot(valeurs_avec_bonnes_unites[:, 0], valeurs_avec_bonnes_unites[:, 1],
         label="Courant du pico")
plt.xlabel("Tension entre G1 et le ground [V]")
plt.ylabel("Courant mesuré [nA]")
plt.legend()
plt.show()
"""
------------------------------------------------------------------------------

Déterminer l'emplacement approximatif des maximums. Ça devrait être
environ: Estimation des pics: [ 1.9844797  6.902538  11.950019  17.083782 ] V

_____________________________________________________________________________
"""
# Mettre votre code ici












# Mettre vos données avec les bonnes unités à la place du None
valeurs_avec_bonnes_unites_determination_des_pics = None  # Array de trois colonnes
liste_des_indexes_des_pics = None  # Liste de nombres entiers

"""
_____________________________________________________________________________
"""
# Ne pas modifier cette section!!!

print("Estimation des pics:", valeurs_avec_bonnes_unites_determination_des_pics[liste_des_indexes_des_pics, 0])

# La figure obtenue devrait correspondre à celle de figures_exemple/estimation_des_pics
plt.figure()
plt.plot(valeurs_avec_bonnes_unites_determination_des_pics[:, 0],
         valeurs_avec_bonnes_unites_determination_des_pics[:, 1],
         label="Courant du pico")
plt.xlabel("Tension entre G1 et le ground [V]")
plt.scatter(valeurs_avec_bonnes_unites_determination_des_pics[liste_des_indexes_des_pics, 0],
            valeurs_avec_bonnes_unites_determination_des_pics[liste_des_indexes_des_pics, 1],
            label="Estimation des pics")
plt.ylabel("Courant mesuré [nA]")
plt.legend()
plt.show()











