"""
Helper pour gérer les rôles utilisateur basés sur les matricules
"""

# Configuration des matricules par rôle
SUPER_USER_MATRICULES = [
    '2351882',
    '8742647',
    '9307037',
]

BETA_TESTER_MATRICULES = [
    '8640426',
    '0101010',
    '9390449',
    '0101683',
    '1505113',
]

def get_role_from_matricule(matricule):
    """
    Détermine le rôle d'un utilisateur basé sur son matricule
    
    Args:
        matricule (str): Le matricule de l'utilisateur
        
    Returns:
        str: Le rôle de l'utilisateur ('super_user', 'beta_tester', ou 'normal_user')
    """
    if not matricule:
        return 'normal_user'
    
    if matricule in SUPER_USER_MATRICULES:
        return 'super_user'
    elif matricule in BETA_TESTER_MATRICULES:
        return 'beta_tester'
    else:
        return 'normal_user'

def add_super_user_matricule(matricule):
    """
    Ajoute un matricule à la liste des Super Users
    
    Args:
        matricule (str): Le matricule à ajouter
        
    Returns:
        bool: True si ajouté avec succès, False si déjà présent
    """
    if matricule not in SUPER_USER_MATRICULES:
        SUPER_USER_MATRICULES.append(matricule)
        return True
    return False

def remove_super_user_matricule(matricule):
    """
    Supprime un matricule de la liste des Super Users
    
    Args:
        matricule (str): Le matricule à supprimer
        
    Returns:
        bool: True si supprimé avec succès, False si non trouvé
    """
    if matricule in SUPER_USER_MATRICULES:
        SUPER_USER_MATRICULES.remove(matricule)
        return True
    return False

def add_beta_tester_matricule(matricule):
    """
    Ajoute un matricule à la liste des Bêta testeurs
    
    Args:
        matricule (str): Le matricule à ajouter
        
    Returns:
        bool: True si ajouté avec succès, False si déjà présent
    """
    if matricule not in BETA_TESTER_MATRICULES:
        BETA_TESTER_MATRICULES.append(matricule)
        return True
    return False

def remove_beta_tester_matricule(matricule):
    """
    Supprime un matricule de la liste des Bêta testeurs
    
    Args:
        matricule (str): Le matricule à supprimer
        
    Returns:
        bool: True si supprimé avec succès, False si non trouvé
    """
    if matricule in BETA_TESTER_MATRICULES:
        BETA_TESTER_MATRICULES.remove(matricule)
        return True
    return False

def get_all_super_user_matricules():
    """
    Retourne tous les matricules des Super Users
    
    Returns:
        list: Liste des matricules des Super Users
    """
    return SUPER_USER_MATRICULES.copy()

def get_all_beta_tester_matricules():
    """
    Retourne tous les matricules des Bêta testeurs
    
    Returns:
        list: Liste des matricules des Bêta testeurs
    """
    return BETA_TESTER_MATRICULES.copy()

def is_super_user_matricule(matricule):
    """
    Vérifie si un matricule appartient à un Super User
    
    Args:
        matricule (str): Le matricule à vérifier
        
    Returns:
        bool: True si c'est un Super User, False sinon
    """
    return matricule in SUPER_USER_MATRICULES

def is_beta_tester_matricule(matricule):
    """
    Vérifie si un matricule appartient à un Bêta testeur
    
    Args:
        matricule (str): Le matricule à vérifier
        
    Returns:
        bool: True si c'est un Bêta testeur, False sinon
    """
    return matricule in BETA_TESTER_MATRICULES
