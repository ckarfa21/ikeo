import tkinter as tk
from tkinter import *
import random as rand
from bdd import BDD
#toto=get fournisseur for products
###########creation de la fenetre
root=tk.Tk()
# Définir un titre pour la fenêtre
root.title("Ikeo")
# Définir la taille de la fenêtre 
root.geometry("400x400") # mettre les pixels suivant ce pattern 0pixels x 0pixels
# Définir le style de la fenêtre
root.configure(bg="#41B77F") # bg = background
# Définir une taille minimale
root.minsize(480, 360)
# Définir une taille maximale
#fenetre.maxsize(600, 600)
########### Pour afficher la fenêtre à l'utilisateur
# Création d'une frame qui contiendra les titres
frame_titre = tk.Frame(root, bg="green") # root est la fenêtre à laquelle la frame est rattachée
# Permet de l'insérer dans la fenêtre
############Permet d'afficher du texte.
frame_titre = tk.Frame(root, bg="green")
frame_titre.pack()
# On définit le texte que l'on veut afficher dans notre frame
titre = tk.Label(frame_titre, text='facture', font=("courrier", 40), bg='grey', fg='black')
frame_titre.pack(expand=YES)
# text = le texte à afficher, font = définir une police particulière et sa taille, 
# bg = couleur de l'arrière plan, et fg = couleur du texte
# Il faut également lui dire de l'afficher dans la frame

titre.pack(pady=10, padx=10) 
# pady et padx sont des marges en pixels sur les axes y et x, 
# c'est-à-dire en vertical et en horizontal respectivement.
# Ces marges nous permettront de voir la couleur de la frame qui comprend notre texte.
root.mainloop()

def roll():
    x = rand.randint(1, 6)
    titre.configure(text=x) 
    fenetre= tk.Tk()


#Nouvelle fenêtre qui contiendra les boutons
frame_bouton = tk.Frame(root, bg="black")
frame_bouton.pack()

titre = tk.Label(frame_titre, text='Cliquez sur le bouton pour lancer le dé.', font=("Helvetica", 20), bg='orange', fg='white')
titre.pack(pady=10, padx=10) 

bouton = tk.Button(frame_bouton, text='Lancer le dé', height=5, width=20, bd=0)
# Il est possible de modifier les propriétés d'un bouton pour lui ajouter une commande
bouton.configure(command=roll) # la fonction appelée ne prend pas d'arguments donc pas de ()
button1 = tk.Button(frame, text="All Products", font=40, command=lambda: label.configure(text=db1.getAllProducts()))
# Afficher le bouton dans la frame
bouton.pack()

