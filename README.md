# Application de Fusion de PDF

Cette application permet de fusionner plusieurs fichiers PDF en un seul document de sortie.

## Fonctionnalités

- Interface graphique intuitive
- Sélection multiple de fichiers PDF
- Réorganisation de l'ordre des fichiers avant fusion
- Vérification de la validité des fichiers PDF
- Gestion des erreurs

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/Yorick-xy/pdf_merger.git
cd pdf-merger
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

Lancez l'application :
```bash
python main.py
```

Dans l'interface graphique :
1. Cliquez sur "Ajouter des fichiers PDF" pour sélectionner vos documents
2. Réorganisez l'ordre des fichiers avec les boutons "Monter" et "Descendre" si nécessaire
3. Cliquez sur "Fusionner les PDF" pour créer le document final
4. Choisissez l'emplacement où enregistrer le fichier fusionné

## Architecture du projet

```
PDF_MERGER/
│
├── requirements.txt             # Dépendances du projet
├── main.py                      # Point d'entrée de l'application
├── app/
│   ├── __init__.py              # Initialisation du package
│   ├── pdf_merger_app.py        # Classe principale de l'application
│   └── utils/
│       ├── __init__.py          # Initialisation du sous-package
│       └── pdf_utils.py         # Fonctions utilitaires pour la manipulation des PDF
├── resources/
│   └── icons/                   # Dossier pour stocker les icônes éventuelles
└── README.md                    # Documentation du projet

```

## Dépendances

- Python 3.6+
- PyPDF2 3.0.1
- tkinter (généralement inclus dans Python)

## Licence