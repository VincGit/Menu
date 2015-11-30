#!/usr/local/bin/python3

import os
from tkinter import *
from Course import *
from profilJour import *
import pickle
import random

class FrameGenererMenu(Frame):
	"""Cette class est la frame qui permet de generer le menu de la semaine"""
	def __init__(self,parentFrame):
		Frame.__init__(self,parentFrame)
		self.grid(row=0,column=0,columnspan=3)
		self.parentFrame=parentFrame
		self.liste_preferences = []
		self.liste_menu_jour=[]
		self.getPreferences()
		self.getListOfRecette()
		print(self.liste_course)
		print(self.liste_preferences)
	
		self.frame_menu = Frame(self)
		self.frame_menu.grid(row=0,column=0)

		self.frame_menu.bouton_quitter = Button(self.frame_menu,text="Quitter",command=self.parentFrame.destroy)
		self.frame_menu.bouton_quitter.grid(row=0,column=0)
		
		self.frame_menu.bouton_imprimer = Button(self.frame_menu,text="Imprimer")
		self.frame_menu.bouton_imprimer.grid(row=0,column=1)


		for i,day in enumerate(self.liste_preferences):
			if day.actif is True:
				self.determine_plat(day,i)
		
		self.display_daily_menu()
	
	def display_daily_menu(self):
		for i,day in enumerate(self.liste_menu_jour):
			if day.plat is not None:	
				frame_menu_jour = FrameMenuDay(self,day,i)
				frame_menu_jour.grid(row=i+1,column=0)	
			else:
				print("DEBUG le plat du jour est null")
				frame_menu_jour = FrameEmptyDay(self,day,i)
				frame_menu_jour.grid(row=i+1,column=0,sticky=W)


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
	
	def determine_plat(self,profilJour,index):
		"""cette methode scanne les Courses pour determiner un plat qui correspond aux criteres"""
		liste_course_match = []
		print("DEBUG : determine_plat")
		print("DEBUG : self.liste_course")
		print(self.liste_course)
		liste_course_match=self.liste_course
		#si on a des invites on filtre uniquement les Courses qui correspondent
		if profilJour.invite == True:
			print("DEBUG : profil invite True")
			liste_course_match = [Course for Course in liste_course_match if Course.OK_for_invitee == True]
		print(liste_course_match)
		
		#The above piece of code filters only the course that fits the season
		print("DEBUG : filter on season")
		print(profilJour.saison)
		if "Toutes" not in profilJour.saison:
			print("DEBUG : filter on season oui")
			liste_course_match = [Course for Course in liste_course_match if Course.season in
				profilJour.saison or Course.season == "Toutes"] 		
		print("DEBUG : liste_course_match")
		print(liste_course_match)		

		#The above piece of code filters only the courses that fits the type of course from profile
		print("DEBUG : filter on course type")
		liste_course_match = [Course for Course in liste_course_match if Course.type_course in
			profilJour.type_repas] 		
		print("DEBUG : liste_course_match")
		print(liste_course_match)		

		#on a applique tous les filtres, on choisit une Course au hasard parmi les restantes
		if len(liste_course_match) == 0:
			profilJour.plat=None
			print("DEBUG : pas de plat trouve")
		else:
			profilJour.plat = random.choice(liste_course_match)
		if index < len(self.liste_menu_jour):
			self.liste_menu_jour[index]=profilJour
		else:
			self.liste_menu_jour.append(profilJour)
	def getListOfRecette(self):
		os.chdir("./")
		with open('sauvegardeRecette.txt','rb') as fichier:
			try:
				monDePickler = pickle.Unpickler(fichier)
				self.liste_course = monDePickler.load()
			except pickle.PicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("unknown exception raised")
class FrameEmptyDay(Frame):
	"""This class allows to display a day when no course has been found"""
	def __init__(self,parentFrame,profilJour,index):
		Frame.__init__(self,parentFrame,bd=2)
		self.jour=Label(self,text=profilJour.nom+" : pas de Course trouvee")
		self.jour.grid(row=0,column=0,sticky=E)
			

class FrameMenuDay(Frame):
	"""Cette classe contient la ligne de menu de la journee"""
	def __init__(self,parentFrame,profilJour,index):
		Frame.__init__(self,parentFrame,bd=2)
		print("init Frame_menu_jour")
		print(profilJour)	

		self.parentFrame=parentFrame	
		#Nom de la journee
		self.jour=Label(self,text=profilJour.nom+" : ")
		self.jour.grid(row=0,column=0)
	
		#Le plat choisi
		self.plat=Label(self,text=profilJour.plat.name)
		self.plat.grid(row=0,column=1)

		#Un bouton pour afficher les details du plat
		self.detail=Button(self,text="Details")
		self.detail.grid(row=0,column=2)

		#Un bouton pour demander une autre proposition
		self.propose=Button(self,text="Proposer autre chose",
			command=lambda : self.determine_new_course(profilJour,index))
		self.propose.grid(row=0,column=3)

	def determine_new_course(self,profilJour,index):
		print("DEBUG : determiner_new_course")
		self.parentFrame.determine_plat(profilJour,index)
		self.parentFrame.display_daily_menu()
