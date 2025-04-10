"""
Module contenant la classe principale de l'application de fusion de PDF.
"""
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from app.utils.pdf_utils import merge_pdf_files, is_valid_pdf

class PDFMergerApp:
    """
    Classe principale de l'application de fusion de PDF.
    Gère l'interface graphique et les interactions utilisateur.
    """
    def __init__(self, root):
        """
        Initialise l'application avec la fenêtre racine Tkinter.
        
        Args:
            root: La fenêtre racine Tkinter
        """
        self.root = root
        self.root.title("Fusion de PDF")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Liste des fichiers PDF sélectionnés
        self.pdf_files = []
        
        self.create_widgets()
        
    def create_widgets(self):
        """Crée et dispose tous les widgets de l'interface."""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Bouton pour ajouter des fichiers
        ttk.Button(main_frame, text="Ajouter des fichiers PDF", command=self.add_files).pack(pady=10)
        
        # Frame pour la liste des fichiers
        files_frame = ttk.LabelFrame(main_frame, text="Fichiers sélectionnés")
        files_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Scrollbar pour la liste
        scrollbar = ttk.Scrollbar(files_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Liste des fichiers
        self.files_listbox = tk.Listbox(files_frame, height=10, width=70, yscrollcommand=scrollbar.set)
        self.files_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.files_listbox.yview)
        
        # Boutons pour réorganiser la liste
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(buttons_frame, text="Monter", command=self.move_up).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Descendre", command=self.move_down).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Supprimer", command=self.remove_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Tout effacer", command=self.clear_files).pack(side=tk.LEFT, padx=5)
        
        # Frame pour les options de fusion
        merge_frame = ttk.LabelFrame(main_frame, text="Options de fusion")
        merge_frame.pack(fill=tk.X, pady=10)
        
        # Bouton pour fusionner
        ttk.Button(merge_frame, text="Fusionner les PDF", command=self.merge_pdfs).pack(pady=10)
    
    def add_files(self):
        """Ouvre un sélecteur de fichiers pour ajouter des PDF à la liste."""
        files = filedialog.askopenfilenames(
            title="Sélectionner des fichiers PDF",
            filetypes=[("Fichiers PDF", "*.pdf")]
        )
        
        if files:
            for file in files:
                if file not in self.pdf_files:
                    self.pdf_files.append(file)
                    self.files_listbox.insert(tk.END, os.path.basename(file))
    
    def move_up(self):
        """Déplace le fichier sélectionné vers le haut dans la liste."""
        selected_idx = self.files_listbox.curselection()
        if not selected_idx or selected_idx[0] == 0:
            return
        
        idx = selected_idx[0]
        # Échange dans la liste des fichiers
        self.pdf_files[idx], self.pdf_files[idx-1] = self.pdf_files[idx-1], self.pdf_files[idx]
        
        # Mise à jour de l'affichage
        file_name = self.files_listbox.get(idx)
        self.files_listbox.delete(idx)
        self.files_listbox.insert(idx-1, file_name)
        self.files_listbox.selection_clear(0, tk.END)
        self.files_listbox.selection_set(idx-1)
    
    def move_down(self):
        """Déplace le fichier sélectionné vers le bas dans la liste."""
        selected_idx = self.files_listbox.curselection()
        if not selected_idx or selected_idx[0] == len(self.pdf_files) - 1:
            return
        
        idx = selected_idx[0]
        # Échange dans la liste des fichiers
        self.pdf_files[idx], self.pdf_files[idx+1] = self.pdf_files[idx+1], self.pdf_files[idx]
        
        # Mise à jour de l'affichage
        file_name = self.files_listbox.get(idx)
        self.files_listbox.delete(idx)
        self.files_listbox.insert(idx+1, file_name)
        self.files_listbox.selection_clear(0, tk.END)
        self.files_listbox.selection_set(idx+1)
    
    def remove_file(self):
        """Supprime le fichier sélectionné de la liste."""
        selected_idx = self.files_listbox.curselection()
        if not selected_idx:
            return
        
        idx = selected_idx[0]
        self.files_listbox.delete(idx)
        self.pdf_files.pop(idx)
    
    def clear_files(self):
        """Efface tous les fichiers de la liste."""
        self.files_listbox.delete(0, tk.END)
        self.pdf_files = []
    
    def merge_pdfs(self):
        """Fusionne les fichiers PDF sélectionnés."""
        if not self.pdf_files:
            messagebox.showwarning("Attention", "Aucun fichier PDF sélectionné !")
            return
        
        output_file = filedialog.asksaveasfilename(
            title="Enregistrer le PDF fusionné",
            defaultextension=".pdf",
            filetypes=[("Fichier PDF", "*.pdf")]
        )
        
        if not output_file:
            return
        
        try:
            # Vérifier que tous les fichiers sont des PDF valides
            invalid_files = []
            for pdf_file in self.pdf_files:
                if not is_valid_pdf(pdf_file):
                    invalid_files.append(os.path.basename(pdf_file))
            
            if invalid_files:
                messagebox.showerror("Erreur", f"Les fichiers suivants ne sont pas des PDF valides :\n{', '.join(invalid_files)}")
                return
            
            # Fusionner les PDF
            merge_pdf_files(self.pdf_files, output_file)
            
            messagebox.showinfo("Succès", f"Les PDF ont été fusionnés avec succès !\nFichier de sortie : {output_file}")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la fusion : {str(e)}")