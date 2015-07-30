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
				"Jeudi midi","Jeudi soir"]		
				#"Vendredi midi","Vendredi soir"]
		
		self.list_profil_jour=[]
		self.list_frame_profil_jour=[]
		for i,repas in enumerate(list_repas):
			profil_jour=profilJour(repas)
			frame_profil_jour=LabelFrame_ProfilJour(self,profil_jour)
			frame_profil_jour.pack()
			self.list_profil_jour.append(profil_jour)
			self.list_frame_profil_jour.append(frame_profil_jour)
		self.test()		
	
		self.bouton_sauver = Button(self,text="Sauvegarder",command=self.test)
		self.bouton_sauver.pack()

		self.bouton_quitter = Button(self,text="Quitter sans sauvegarder",command=self.parentFrame.destroy)
		self.bouton_quitter.pack()

	def test(self):
		"""Cette methode parcourt toutes les frames du profil de repas de la semaine
		Pour chacune elle va initialiser les boutons avec les preferences enregistrees"""

		for i,frame in enumerate(self.list_frame_profil_jour):
			#on initialise le bouton actif
			if(frame.profilJour.actif is True):
				frame.bouton_actif.select()
			else:
				frame.bouton_actif.deselect()
			#on initialise le bouton, repas libre
			if(frame.profilJour.free is True):
				frame.bouton_libre.select()
			else:
				frame.bouton_libre.deselect()
			#on initialise le bouton, "il y a des invites"
			if(frame.profilJour.invite is True):
				frame.bouton_invite.select()
			else:
				frame.bouton_invite.deselect()

			#on initialise le type de repas
			liste_repas_frame = list(frame.liste_type.get(0, END))
			print(liste_repas_frame)
			for i,type_repas in enumerate(liste_repas_frame):
				if(type_repas in frame.profilJour.type_repas):
					print(type_repas+"active")
					frame.liste_type.selection_set(i)	
				
			#on initialise la saison
			liste_saison_frame = list(frame.liste_saison.get(0, END))
			print(liste_saison_frame)
			for i,saison in enumerate(liste_saison_frame):
				if(saison in frame.profilJour.saison):
					print(saison+"active")
					frame.liste_saison.selection_set(i)	




class LabelFrame_ProfilJour(LabelFrame):
	"""Cette LabelFrame va etre repete pour chaque repas de la semaine
	elle contient comme attribut un profilJour"""
	def __init__(self,parentFrame,profil_jour):
		LabelFrame.__init__(self,parentFrame,text=profil_jour.nom)
		self.parentFrame=parentFrame
		
		#on attache un profilJour a la labelFrame
		self.profilJour = profil_jour
		#son nom est le nom du jour
		self.label_nom=Label(self,text=self.profilJour.nom)
		self.label_nom.pack(fill=Y,side=LEFT)
	
		#La check box pour l'etat actif/inactif
		var_actif=IntVar()
		self.bouton_actif = Checkbutton(self,text="Actif",variable=var_actif)
		self.bouton_actif.pack(fill=Y,side=LEFT)
		

		#La check box pour laisser le choix libre
		var_libre=IntVar()	
		self.bouton_libre = Checkbutton(self,text="Laisser le choix libre")
		self.bouton_libre.pack(fill=Y,side=LEFT)
		

		#Le choix de la saison
		scrollbar_saison = Scrollbar(self, orient=VERTICAL)
		self.liste_saison = Listbox(self,height = 2,selectmode=SINGLE,exportselection=False,
			yscrollcommand=scrollbar_saison.set)
		scrollbar_saison.config(command=self.liste_saison.yview)
		self.liste_saison.insert(END,"Toutes")
		self.liste_saison.insert(END,"Seulement ete")
		self.liste_saison.insert(END,"Seulement hiver")
		self.liste_saison.pack(fill=Y,side=LEFT)
		scrollbar_saison.pack(fill=Y,side=LEFT)
		

		#La list box pour le type de repas
		scrollbar_type = Scrollbar(self, orient=VERTICAL)
		self.liste_type = Listbox(self,height=2,selectmode=MULTIPLE,exportselection=False,
			yscrollcommand=scrollbar_type.set)
		scrollbar_type.config(command=self.liste_type.yview)
		self.liste_type.insert(END,"Legume")
		self.liste_type.insert(END,"Viande")
		self.liste_type.insert(END,"Poisson")
		self.liste_type.insert(END,"Soupe")
		self.liste_type.insert(END,"Salade")
		self.liste_type.insert(END,"Puree")
		self.liste_type.insert(END,"Autres")
		self.liste_type.pack(fill=Y,side=LEFT)
		scrollbar_type.pack(fill=Y,side=LEFT)
		

		#La check box pour indiquer si on a des invites
		var_invite=IntVar()
		self.bouton_invite = Checkbutton(self,text="Des invites sont prevus",variable=var_invite)
		self.bouton_invite.pack(fill=Y,side=LEFT)










