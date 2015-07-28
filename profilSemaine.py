#!/usr/local/bin/python3

import os
from tkinter import *
from recette import *
from profilJour import *
import pickle

class Frame_Edit_ProfilSemaine(Frame):
	"""Cette frame contient tous le champs pour voir et editer les recettes"""
	def __init__(self, parentFrame):
		Frame.__init__(self,parentFrame, width=768, height=567)
		self.pack(fill=BOTH)
		self.parentFrame=parentFrame	
		
		#On va creer un list de Frame qui contiendra chaque jour de l'annee
		#Le profil de la semaine sera seriliser grace a pickle car on serilisera
		#la liste des frame
		#On construit la liste qui contient les recettes
		list_repas = ["Samedi midi","Samedi soir",
			"Dimanche midi","Dimanche soir",
			"Lundi midi","Lundi soir",		
			"Mardi midi","Mardi soir",		
			"Mercredi midi","Mercredi soir",		
			"Jeudi midi","Jeudi soir",		
			"Vendredi midi","Vendredi soir"]
		
		self.list_profil_jour=[]
		self.list_frame_profil_jour=[]
		for i,repas in enumerate(list_repas):
			profil_jour=profilJour(repas)
			frame_profil_jour=LabelFrame_ProfilJour(self,profil_jour)
			frame_profil_jour.pack()
			self.list_profil_jour.append(profil_jour)
			self.list_frame_profil_jour.append(frame_profil_jour)
			


class LabelFrame_ProfilJour(LabelFrame):
	"""Cette LabelFrame va etre repete pour chaque repas de la semaine
	elle contient comme attribut un profilJour"""
	def __init__(self,parentFrame,profil_jour):
		LabelFrame.__init__(self,parentFrame,text=profil_jour.nom)
		self.parentFrame=parentFrame
		
		#on attache un profilJour a la labelFrame
		self.profilJour = profil_jour
		#son nom est le nom du jour
		print(self.profilJour)		
		self.label_nom=Label(self,text=self.profilJour.nom)
		self.label_nom.pack(fill=Y,side=LEFT)
	
		var_actif=IntVar()
		var_actif.set(True)	
		self.bouton_actif = Checkbutton(self,text="Actif",onvalue=True,offvalue=False,variable=var_actif)
		if(self.profilJour.actif is True):
			print("actif")
			self.bouton_actif.select()
		else:
			self.bouton_actif.deselect()
		self.bouton_actif.pack(fill=Y,side=LEFT)
		
		var_libre=IntVar()	
		self.bouton_libre = Checkbutton(self,text="Laisser libre")
		if(self.profilJour.free is True):
			self.bouton_libre.select()
		else:
			self.bouton_libre.deselect()
		self.bouton_actif.pack(fill=Y,side=LEFT)
		self.bouton_libre.pack(fill=Y,side=LEFT)
		
		self.bouton_type = Button(self,text="Type")
		self.bouton_type.pack(fill=Y,side=LEFT)

		self.bouton_invite = Button(self,text="OK pour invite")
		self.bouton_invite.pack(fill=Y,side=LEFT)

		self.bouton_saison = Button(self,text="saison")
		self.bouton_actif.pack(fill=Y,side=LEFT)










