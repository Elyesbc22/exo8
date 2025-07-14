"""
TO DO

Développer un outil capable de parcourir un dossier et de lister les fichiers et les sous-dossiers qu'il contient.
L'outil doit afficher la structure du dossier et indiquer le nombre de fichiers et de sous-dossiers à chaque niveau.
 doit être utiliser dans main.py

"""

def parcourir_dossier(dossier):
    """Outils pour parcourir un dossier et lister les fichiers et sous-dossiers qu'il contient.

    Args:
        dossier (string): Le chemin du dossier à parcourir

    Returns:
        int: Le nombre de fichiers et de sous-dossiers trouvés
    """
    nombre_fichiers = 0
    nombre_dossiers = 0
    
    """
    TODO:
    - Parcourir le dossier
    - Compter le nombre de fichiers et de sous-dossiers
    """

    return nombre_fichiers, nombre_dossiers

def liste_par_an(dossier = "./acme/section/HR"):
    """liste les années disponibles

    Args:
        dossier (string): exemple  "./acme/section/HR"
        
    returns:
        list: Une liste des années disponibles dans le dossier
        exemple: ['2020', '2021', '2022']
    """
    
    """
    TODO:
    - Lister les années disponibles
    
    Exemple:
    dossier = "./acme/section/HR"
    Retourne:
        ['2020', '2021', '2022']
    """
    
    years = []
    
    return years

def liste_par_mois(dossier):
    """Liste les mois disponibles dans un dossier donné.

    Args:
        dossier (string): Le chemin du dossier à parcourir

    Returns:
        list: Une liste des mois disponibles
        exemple: ['janvier', 'février', 'mars', ...]
    """
    
    liste_mois = []
    
    return liste_mois

def liste_par_jour(dossier):
    """Liste les jours disponibles dans un dossier donné.

    Args:
        dossier (string): Le chemin du dossier à parcourir

    Returns:
        list: Une liste des jours disponibles
        exemple: ['01', '02', '03', ...]
    """
    
    liste_jours = []
    
    return liste_jours