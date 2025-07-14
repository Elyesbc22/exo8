"""
Programme principal pour tester les outils de parcours de dossiers.
"""

import os
from tools.lecture import parcourir_dossier, liste_par_an, liste_par_mois, liste_par_jour

def main():
    """Fonction principale pour tester les outils."""
    
    # Chemin vers le dossier section
    dossier_section = os.path.join(os.path.dirname(__file__), "section")
    
    print("=== TEST DES OUTILS DE PARCOURS ===")
    print()
    
    # 1. Parcours complet de la structure
    print("1. PARCOURS COMPLET")
    print("-" * 30)
    resultat = parcourir_dossier(dossier_section)
    print("Nombre total d'éléments:", resultat[0] + resultat[1])
    print()
    
    # 2. Liste des fichiers par année
    print("2. FICHIERS PAR ANNÉE")
    print("-" * 30)
    nb_annees = liste_par_an(dossier_section)
    print("Nombre d'années trouvées:", len(nb_annees))
    print("Années disponibles:", nb_annees)
    print()
    
    # 3. Liste des fichiers par mois
    print("3. FICHIERS PAR MOIS")
    print("-" * 30)
    nb_mois = liste_par_mois(dossier_section)
    print("Nombre de mois trouvés:", len(nb_mois))
    print("Mois disponibles:", nb_mois)
    print()
    
    # 3. Liste des fichiers par mois
    print("4. FICHIERS PAR JOURS")
    print("-" * 30)
    nb_jours = liste_par_jour(dossier_section)
    print("Nombre de jours trouvés:", len(nb_jours))
    print("Jours disponibles:", nb_jours)
    print()
    
    print("=== FIN DU TEST ===")
    return 0

main()