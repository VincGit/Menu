#!/usr/local/bin/python3

import os
from tkinter import *
from recette import *
from profilJour import *
import pickle

class Frame_Edit_ProfilSemaine(Frame):
	"""Cette frame contient tous le champs pour voir et editer les recettes"""
	def __init__(self, parentFrame):
		Frame.__init__(self,parentFrame, width=768, height=867)
		self.pack(fill=BOTH)
		self.parentFrame=parentFrame	
		
		self.bouton_sauver = Button(self,text="Sauvegarder",command=self.sauvegarderProfil)
		self.bouton_sauver.pack()

		self.bouton_quitter = Button(self,text="Quitter",command=self.parentFrame.destroy)
		self.bouton_quitter.pack()
		
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
		
		self.getProfil()
		if len(self.list_profil_jour) == 0:
			#la sauvegarde/load de profil s'est mal passe
			#on recreer les profil de 0
			print("getProfil en erreur, on cree les profils de 0")
			for i,repas in enumerate(list_repas):
				profil_jour=profilJour(repas)
				frame_profil_jour=LabelFrame_ProfilJour(self,profil_jour)
				frame_profil_jour.pack()
				self.list_profil_jour.append(profil_jour)
				self.list_frame_profil_jour.append(frame_profil_jour)
		else:
			#la sauvegarde/recuperation de profil est OK
			#on creer la frame a partir des profils retrouves
			print("les profils sont retrouves")
			for i,profil in enumerate(self.list_profil_jour):
				frame_profil_jour=LabelFrame_ProfilJour(self,profil)
				frame_profil_jour.pack()
				self.list_frame_profil_jour.append(frame_profil_jour)

		#on charge les profils sauvegardes dans la frame		
		self.loadConfig()		
	

	def sauvegarderProfil(self):
		"""Cette methode va sauver la liste des profils jour dans un fichier"""
		print("sauvegarderProfil")
		self.getConfig()
		os.chdir("./")
		with open('sauvegardeProfil.txt','wb') as fichier:
			try:
				monPickler = pickle.Pickler(fichier)
				monPickler.dump(self.list_profil_jour)
			except pickle.UnPicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("unknown exception raised")
	
	def getProfil(self):
		print("getProfil")
		os.chdir("./")
		with open('sauvegardeProfil.txt','rb') as fichier:
			try:
				monDePickler = pickle.Unpickler(fichier)
				self.list_profil_jour = monDePickler.load()
			except pickle.PicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("unknown exception raised")

	def getConfig(self):
		"""Cette methode va lire chaque frame et sauver la configuration
		dans le profil_jour associe"""
		print("getConfig")
		for i,frame in enumerate(self.list_frame_profil_jour):
			#on initialise le bouton actif
			if frame.var_actif.get() == 1:
				frame.profilJour.actif = True
			else:
				frame.profilJour.actif = False
			
			if frame.var_libre.get() == 1:
				frame.profilJour.free = True
			else:
				frame.profilJour.free = False

			if frame.var_invite.get() == 1:
				frame.profilJour.invite = True
			else:
				frame.profilJour.invite = False
			

			liste_type = frame.liste_type.curselection()
			print(liste_type)
			del frame.profilJour.type_repas[:]
			for i,type_repas in enumerate(liste_type):
				frame.profilJour.type_repas.append(frame.liste_type.get(type_repas))
				print(frame.liste_type.get(type_repas)+ "has been added")
				
			liste_saison = frame.liste_saison.curselection()
			print(liste_saison)
			del frame.profilJour.saison[:]
			for i,saison in enumerate(liste_saison):
				frame.profilJour.saison.append(frame.liste_saison.get(saison))
				print(frame.liste_saison.get(saison)+ "has been added")

		

	def loadConfig(self):
		"""Cette methode parcourt toutes les frames du profil de repas de la semaine
		Pour chacune elle va initialiser les boutons avec les preferences enregistrees"""
		print("loadConfig")
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
			for i,type_repas in enumerate(liste_repas_frame):
				if(type_repas in frame.profilJour.type_repas):
					frame.liste_type.selection_set(i)	
				
			#on initialise la saison
			liste_saison_frame = list(frame.liste_saison.get(0, END))
			for i,saison in enumerate(liste_saison_frame):
				if(saison in frame.profilJour.saison):
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
		self.var_actif=IntVar()
		self.bouton_actif = Checkbutton(self,text="Actif",variable=self.var_actif)
		self.bouton_actif.pack(fill=Y,side=LEFT)
		

		#La check box pour laisser le choix libre
		self.var_libre=IntVar()	
		self.bouton_libre = Checkbutton(self,text="Laisser le choix libre",variable=self.var_libre)
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
		self.var_invite=IntVar()
		self.bouton_invite = Checkbutton(self,text="Des invites sont prevus",variable=self.var_invite)
		self.bouton_invite.pack(fill=Y,side=LEFT)










