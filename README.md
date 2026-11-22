# Citation du jour

Application de bureau en Python qui affiche des citations aléatoires dans une fenêtre graphique. Ce projet a été réalisé pour un devoir en cours de Python en 1ère année d'études, en février 2026.

## Fonctionnement

L'interface s'appuie sur une base locale de 60 citations stockées dans un dictionnaire Python. Au clic sur le bouton Générer, le programme tire une entrée au hasard et affiche le texte, l'auteur et l'année dans la fenêtre (ainsi que dans la console).

Un bouton Copier place la citation affichée dans le presse-papiers du système. Le bouton Quitter demande confirmation avant de fermer la fenêtre.

## Stack technique et prérequis

Le projet utilise uniquement Python 3 et sa bibliothèque standard (`tkinter` pour l'interface graphique et `random` pour le tirage aléatoire). Aucune dépendance externe n'est nécessaire.

Sur Windows et macOS, `tkinter` est généralement installé avec Python. Sous Linux (Debian ou Ubuntu), il faut parfois installer le paquet `python3-tk` séparément.

## Installation et lancement

Clonez le dépôt puis lancez le script principal depuis le dossier du projet :

```bash
git clone <url-du-depot>
cd Citation-du-jour
python Code_CITATION.py
```

Selon votre système, remplacez `python` par `python3`.

## Structure des fichiers

Le dépôt contient deux fichiers Python :

- `Code_CITATION.py` gère la fenêtre Tkinter, les boutons et l'affichage des citations.
- `citations_db.py` contient le dictionnaire `CITATIONS` regroupant les 60 citations (texte, auteur, année et catégorie).
