#!/usr/local/bin/python3

from tkinter import *
import os
from Course import *
import pickle


class FrameAddCourse(Frame):
	"""Cette frame contient tous le champs pour ajouter un plat"""
	def __init__(self, parentFrame):
		Frame.__init__(self,parentFrame, width=768, height=567)
		self.pack(fill=BOTH)
		self.parentFrame=parentFrame	
		#On attache une Course a la Frame
		self.Course = Course()
		self.list_course = []
		
		#Champ de saisie du nom de la Course
		self.label = Label(self, text="Nom du plat")
		self.label.grid(row=0,column=0,columnspan=2,padx=20,pady=2)
		self.var_nom = StringVar()		
		self.entree_nom = Entry(self,textvariable=self.var_nom,width=45)
		self.entree_nom.grid(row=1,column=0,columnspan=2,padx=20,pady=2)

		#LabelFrame pour la selection du type de Course
		self.label_frame_type = LabelFrame(self,text="Selection du type")
		self.label_frame_type.grid(row=2,column=0,rowspan=2,sticky=W+N,padx=20,pady=2)
		self.var_legume = IntVar()		
		self.type_legume = Checkbutton(self.label_frame_type,text="Legume",variable=self.var_legume)
		self.type_legume.grid(row=0,column=0,sticky=W)
		self.var_viande = IntVar()		
		self.type_viande = Checkbutton(self.label_frame_type,text="Viande",variable=self.var_viande)
		self.type_viande.grid(row=1,column=0,sticky=W)
		self.var_poisson = IntVar()		
		self.type_poisson = Checkbutton(self.label_frame_type,text="Poisson",variable=self.var_poisson)
		self.type_poisson.grid(row=2,column=0,sticky=W)
		self.var_puree = IntVar()		
		self.type_puree = Checkbutton(self.label_frame_type,text="Puree",variable=self.var_puree)
		self.type_puree.grid(row=3,column=0,sticky=W)
		self.var_soupe = IntVar()		
		self.type_soupe = Checkbutton(self.label_frame_type,text="Soupe",variable=self.var_soupe)
		self.type_soupe.grid(row=4,column=0,sticky=W)
		self.var_salade = IntVar()		
		self.type_salade = Checkbutton(self.label_frame_type,text="Salade",variable=self.var_salade)
		self.type_salade.grid(row=5,column=0,sticky=W)
		self.var_autre = IntVar()		
		self.type_autre = Checkbutton(self.label_frame_type,text="Autre",variable=self.var_autre)
		self.type_autre.grid(row=6,column=0,sticky=W)

		
		#LabelFrame pour la selection de la saison
		self.label_frame_saison = LabelFrame(self,text="Selection de la saison")
		self.label_frame_saison.grid(row=2,column=1,sticky=W+N,padx=20,pady=2)		
		self.var_toutes_saisons = IntVar()		
		self.season_toutes_saisons = Checkbutton(self.label_frame_saison,
			text="Toutes saison",variable=self.var_toutes_saisons)
		self.season_toutes_saisons.grid(row=0,column=0,sticky=W)
		self.var_ete = IntVar()		
		self.season_ete = Checkbutton(self.label_frame_saison,text="Ete",variable=self.var_ete)
		self.season_ete.grid(row=1,column=0,sticky=W)
		self.var_hiver = IntVar()		
		self.season_hiver = Checkbutton(self.label_frame_saison,text="Hiver",variable=self.var_hiver)
		self.season_hiver.grid(row=2,column=0,sticky=W)
		
		#Autres options
		self.label_frame_options = LabelFrame(self,text="Autres options")
		self.label_frame_options.grid(row=3,column=1,sticky=W+N,padx=20,pady=2)
		self.var_OK_invites = IntVar()		
		self.bouton_invite = Checkbutton(self.label_frame_options,
			 text="OK pour les repas avec invites",variable=self.var_OK_invites)
		self.bouton_invite.grid(row=0,column=0,sticky=W)
		self.var_preparer_la_veille = IntVar()		
		self.bouton_laveille = Checkbutton(self.label_frame_options,
			 text="A preparer la veille",variable=self.var_preparer_la_veille)
		self.bouton_laveille.grid(row=1,column=0,sticky=W)

		#Text to handle the recipe text
		self.text_recipe = Text(self, height=20, width=80)
		self.text_recipe.insert(END,"Entrer ici la recette...")
		self.text_recipe.grid(row=2,column=2,rowspan=2,padx=20,pady=2)

		#Text to handle the hyperlink	
		self.text_link = Text(self, height=2, width=80)
		self.text_link.insert(END,"Entrer ici le lien...")
		self.text_link.grid(row=0,column=2,rowspan=2,padx=20,pady=2)

		#Annuler
		self.bouton_quitter = Button(self,text="Annuler", command=parentFrame.destroy)
		self.bouton_quitter.grid(row=6,column=0,padx=2,pady=2)
		
		#Sauvegarder
		self.bouton_save = Button(self,text="Sauvegarder",command=self.save_course)
		self.bouton_save.grid(row=6,column=1,padx=2,pady=2)

	def save_course(self):
		"""Methode qui permet de sauvegarder la Course"""
		print("Course sauvegardee")
		print(self.Course)

		print("self.var_nom : "+self.var_nom.get())
		self.Course.name=self.var_nom.get()
		print("self.vqr_ete : "+str(self.var_ete.get()))
		if(self.var_ete.get()==1):
			self.Course.season = "Seulement ete"
		elif(self.var_hiver.get()==1):
			self.Course.season = "Seulement hiver"
		else:
			self.Course.season = "Toutes"


		if self.var_OK_invites.get() == 1:
			self.Course.OK_for_invitee = True

		if self.var_preparer_la_veille.get() == 1:
			self.Course.prepare_day1 = True

		if self.var_legume.get() == 1:
			self.Course.type_course = "Legume"
		elif self.var_viande.get() == 1:
			self.Course.type_course = "Viande"
		elif self.var_poisson.get() == 1:
			self.Course.type_course = "Poisson"
		elif self.var_puree.get() == 1:
			self.Course.type_course = "Puree"
		elif self.var_soupe.get() == 1:
			self.Course.type_course = "Soupe"
		elif self.var_salade.get() == 1:
			self.Course.type_course = "Salade"
		elif self.var_autre .get() == 1:
			self.Course.type_course = "Autres"
		else:	
			self.Course.type_course = "Autres"
		

		self.Course.recipe = self.text_recipe.get("1.0",END)
		self.Course.link = self.text_link.get("1.0",END)
		print(self.Course)
		
		self.getListOfRecette()
		self.list_course.append(self.Course)
		self.saveListOfRecette()
		#on quitte la fenetreTopLevel	
		self.parentFrame.destroy()
	

	def getListOfRecette(self):
		os.chdir("./")
		with open('sauvegardeRecette.txt','rb') as fichier:
			try:
				monDePickler = pickle.Unpickler(fichier)
				self.list_course = monDePickler.load()
			except pickle.PicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("Unpickler : unknown exception raised")

	def saveListOfRecette(self):
		os.chdir("./")
		with open('sauvegardeRecette.txt','wb') as fichier:
			try:
				monPickler = pickle.Pickler(fichier)
				monPickler.dump(self.list_course)
			except pickle.UnPicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("Pickler : unknown exception raised")
