"""
Module contenant des fonctions utilitaires pour la manipulation des fichiers PDF.
"""
from PyPDF2 import PdfMerger, PdfReader

def is_valid_pdf(file_path):
    """
    Vérifie si un fichier est un PDF valide.
    
    Args:
        file_path (str): Chemin vers le fichier à vérifier
        
    Returns:
        bool: True si le fichier est un PDF valide, False sinon
    """
    try:
        PdfReader(file_path)
        return True
    except Exception:
        return False

def merge_pdf_files(input_files, output_file):
    """
    Fusionne plusieurs fichiers PDF en un seul.
    
    Args:
        input_files (list): Liste des chemins des fichiers PDF à fusionner
        output_file (str): Chemin du fichier PDF de sortie
        
    Raises:
        Exception: Si une erreur se produit pendant la fusion
    """
    merger = PdfMerger()
    
    try:
        # Ajouter chaque PDF au merger
        for pdf_file in input_files:
            merger.append(pdf_file)
        
        # Écrire le fichier fusionné
        merger.write(output_file)
    finally:
        # Toujours fermer le merger
        merger.close()