import random
import tkinter as tk
from tkinter import messagebox
from citations_db import CITATIONS

# ============================================
# IMPORTATION DE LA BASE DE DONNÉES
# ============================================
# Les citations sont importées depuis citations_db.py

citations = CITATIONS

# Variable pour stocker la citation actuelle
citation_actuelle = None


# ============================================
# FONCTION DE FORMATAGE CENTRALISÉE
# ============================================
def formater_citation(citation_dict):
    """Formate une citation en texte lisible"""
    return (f"« {citation_dict['texte']} »\n\n"
            f"— {citation_dict['auteur']} ({citation_dict['annee']})")


# ============================================
# FONCTION POUR GÉNÉRER UNE CITATION
# ============================================
def generer_citation():
    """Génère une nouvelle citation aléatoire et l'affiche"""
    global citation_actuelle
    
    if not citations:
        messagebox.showerror("Erreur", "Aucune citation disponible!")
        return
    
    citation_actuelle = random.choice(list(citations.values()))
    texte_formate = formater_citation(citation_actuelle)
    
    # Mise à jour de l'affichage GUI
    citation_label.config(text=citation_actuelle['texte'], fg='#333333')
    auteur_label.config(text=f"— {citation_actuelle['auteur']} ({citation_actuelle['annee']})")
    
    # Affichage dans la console
    print(f"✨ Citation: {texte_formate}\n")


# ============================================
# FONCTION POUR COPIER LA CITATION
# ============================================
def copier_citation():
    """Copie la citation actuelle dans le presse-papiers"""
    if citation_actuelle is None:
        messagebox.showwarning("Attention", "Générez d'abord une citation!")
        return
    
    texte = formater_citation(citation_actuelle)
    fenetre.clipboard_clear()
    fenetre.clipboard_append(texte)
    fenetre.update()
    messagebox.showinfo("Succès", "Citation copiée dans le presse-papiers!")


# ============================================
# FONCTION POUR QUITTER L'APPLICATION
# ============================================
def quitter_app():
    """Ferme l'application"""
    if messagebox.askokcancel("Quitter", "Êtes-vous sûr de vouloir quitter?"):
        fenetre.destroy()


# ============================================
# CRÉATION DE LA FENÊTRE PRINCIPALE
# ============================================
fenetre = tk.Tk()
fenetre.title("💡 Une Citation par Jour")
fenetre.geometry("700x600")
fenetre.resizable(False, False)
fenetre.config(bg='#f0f0f0')

# Icône et couleur de fenêtre
fenetre.config(bg='#f8f9fa')


# ============================================
# FRAME SUPÉRIEUR - TITRE
# ============================================
frame_titre = tk.Frame(fenetre, bg='#2c3e50', height=100)
frame_titre.pack(fill=tk.X, padx=0, pady=0)

titre = tk.Label(
    frame_titre,
    text="💡 Une Citation par Jour",
    font=('Arial', 28, 'bold'),
    bg='#2c3e50',
    fg='white'
)
titre.pack(pady=15)

sous_titre = tk.Label(
    frame_titre,
    text="Trouvez l'inspiration chaque jour",
    font=('Arial', 11, 'italic'),
    bg='#2c3e50',
    fg='#ecf0f1'
)
sous_titre.pack(pady=(0, 10))


# ============================================
# FRAME CENTRAL - CITATION
# ============================================
frame_citation = tk.Frame(fenetre, bg='white')
frame_citation.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Label pour la citation (le texte principal)
citation_label = tk.Label(
    frame_citation,
    text="Cliquez sur 'Générer' pour afficher une citation",
    font=('Georgia', 16, 'italic'),
    bg='white',
    fg='#555555',
    wraplength=600,
    justify='center',
    pady=40
)
citation_label.pack(fill=tk.BOTH, expand=True)

# Label pour l'auteur et l'année
auteur_label = tk.Label(
    frame_citation,
    text="",
    font=('Arial', 12),
    bg='white',
    fg='#7f8c8d',
    justify='center'
)
auteur_label.pack(pady=20)


# ============================================
# FRAME INFÉRIEUR - BOUTONS
# ============================================
frame_boutons = tk.Frame(fenetre, bg='#f8f9fa')
frame_boutons.pack(fill=tk.X, padx=20, pady=15)

# Bouton Générer
bouton_generer = tk.Button(
    frame_boutons,
    text="🎲 Générer",
    font=('Arial', 12, 'bold'),
    command=generer_citation,
    bg='#27ae60',
    fg='white',
    activebackground='#229954',
    padx=30,
    pady=12,
    relief=tk.RAISED,
    cursor='hand2'
)
bouton_generer.pack(side=tk.LEFT, padx=5)

# Bouton Copier
bouton_copier = tk.Button(
    frame_boutons,
    text="📋 Copier",
    font=('Arial', 12, 'bold'),
    command=copier_citation,
    bg='#3498db',
    fg='white',
    activebackground='#2980b9',
    padx=30,
    pady=12,
    relief=tk.RAISED,
    cursor='hand2'
)
bouton_copier.pack(side=tk.LEFT, padx=5)

# Bouton Quitter
bouton_quitter = tk.Button(
    frame_boutons,
    text="❌ Quitter",
    font=('Arial', 12, 'bold'),
    command=quitter_app,
    bg='#e74c3c',
    fg='white',
    activebackground='#c0392b',
    padx=30,
    pady=12,
    relief=tk.RAISED,
    cursor='hand2'
)
bouton_quitter.pack(side=tk.RIGHT, padx=5)

# Label informatif
info_label = tk.Label(
    fenetre,
    text=f"📚 {len(citations)} citations disponibles",
    font=('Arial', 10),
    bg='#f8f9fa',
    fg='#95a5a6'
)
info_label.pack(pady=5)


# ============================================
# LANCEMENT DE L'APPLICATION
# ============================================
if __name__ == "__main__":
    fenetre.mainloop()
