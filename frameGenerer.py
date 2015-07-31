#!/usr/local/bin/python3

import os
from tkinter import *
from recette import *
from profilJour import *
import pickle
import random

class Frame_generer_menu(Frame):
	"""Cette class est la frame qui permet de generer le menu de la semaine"""
	def __init__(self,parentFrame):
		Frame.__init__(self,parentFrame)
		self.pack()
		self.liste_preferences = []
		self.liste_frame_menu_jour=[]
		self.getPreferences()
		self.getListOfRecette()
		print(self.liste_recette)
		for i,jour in enumerate(self.liste_preferences):
			if jour.actif==True:
				self.determine_plat(jour)
				frame_menu_jour = Frame_menu_jour(self,jour)
				frame_menu_jour.pack(side=TOP)	
				self.liste_frame_menu_jour.append(frame_menu_jour)
				

	def getPreferences(self):
		print("getPreferences")
		os.chdir("./")
		with open('sauvegardeProfil.txt','rb') as fichier:
			try:
				monDePickler = pickle.Unpickler(fichier)
				self.liste_preferences = monDePickler.load()
			except pickle.PicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("unknown exception raised")
	
	def determine_plat(self,profilJour):
		"""cette methode scanne les recettes pour determiner un plat qui correspond aux criteres"""
		liste_recette_match = []
		print("DEBUG : determine_plat")
		print("DEBUG : self.liste_recette")
		print(self.liste_recette)
		if profilJour.invite == True:
			print("DEBUG : profil invite True")
			liste_recette_match = [recette for recette in self.liste_recette if recette.OK_for_invitee == True]
		else:
			liste_recette_match=self.liste_recette
		print("DEBUG : liste_recette_match")
		print(liste_recette_match)
		profilJour.plat = random.choice(liste_recette_match)

	def getListOfRecette(self):
		os.chdir("./")
		with open('sauvegardeRecette.txt','rb') as fichier:
			try:
				monDePickler = pickle.Unpickler(fichier)
				self.liste_recette = monDePickler.load()
			except pickle.PicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("unknown exception raised")
				

class Frame_menu_jour(Frame):
	"""Cette classe contient la ligne de menu de la journee"""
	def __init__(self,parentFrame,profilJour):
		Frame.__init__(self,parentFrame)
		print("init Frame_menu_jour")
		print(profilJour)		
		#Nom de la journee
		self.jour=Label(self,text=profilJour.nom)
		self.jour.pack(side=LEFT)
	
		#Le plat choisi
		self.plat=Label(self,text=profilJour.plat.name)
		self.plat.pack(side=LEFT)

		#Un bouton pour afficher les details du plat
		self.detail=Button(self,text="Details")
		self.detail.pack(side=LEFT)

		#Un bouton pour demander une autre proposition
		self.propose=Button(self,text="Proposer autre chose")
		self.propose.pack(side=LEFT)
