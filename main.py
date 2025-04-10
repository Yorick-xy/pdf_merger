# auteur: Yorick MAPET
# date: 11-04-2025
# description: Application de fusion de fichiers PDF
# version: 1.0
# -*- coding: utf-8 -*-

"""
Lancement de l'interface graphique de l'application.
"""
import tkinter as tk
from app.pdf_merger_app import PDFMergerApp

def main():
    """Fonction principale qui initialise et lance l'application."""
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()