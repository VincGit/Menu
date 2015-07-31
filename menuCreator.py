#!/usr/local/bin/python3

import os
from tkinter import *
from recette import *
from profilSemaine import *
from frameGenerer import *
import pickle

class Frame_Edit_Recette(Frame):
	"""Cette frame contient tous le champs pour voir et editer les recettes"""
	def __init__(self, parentFrame):
		Frame.__init__(self,parentFrame, width=768, height=567)
		self.pack(fill=BOTH)
		self.parentFrame=parentFrame	
		

		#On construit la liste qui contient les recettes		
		self.listebox_recette = Listbox(self)
		self.listebox_recette.pack()
		self.getListOfRecette()
		self.fill_listbox_recette()		

		self.label_frame_action = LabelFrame(self,text="Actions")
		self.label_frame_action.pack()
		self.bouton_editer = Button(self.label_frame_action,text="Editer")
		self.bouton_editer.pack()
		self.bouton_supprimer = Button(self.label_frame_action,text="Supprimer",command=self.delete_recette)
		self.bouton_supprimer.pack()
		

		#Quitter
		self.bouton_quitter = Button(self,text="Quitter", command=self.parentFrame.destroy)
		self.bouton_quitter.pack()

	def delete_recette(self):
		#self.list_recette.remove(recette)
		index_recette = self.listebox_recette.curselection()
		index= index_recette[0]
		print(index_recette) 	
		print(index)
		del self.list_recette[index]
		self.fill_listbox_recette()
		self.saveListOfRecette()

	def fill_listbox_recette(self):
		self.listebox_recette.delete(0,self.listebox_recette.size())
		for i,recette in enumerate(self.list_recette):
			self.listebox_recette.insert(END, recette.name)
		


			
	def getListOfRecette(self):
		os.chdir("./")
		with open('sauvegardeRecette.txt','rb') as fichier:
			try:
				monDePickler = pickle.Unpickler(fichier)
				self.list_recette = monDePickler.load()
			except pickle.PicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("unknown exception raised")

	def saveListOfRecette(self):
		os.chdir("./")
		with open('sauvegardeRecette.txt','wb') as fichier:
			try:
				monPickler = pickle.Pickler(fichier)
				monPickler.dump(self.list_recette)
			except pickle.UnPicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("unknown exception raised")


class Frame_Ajout_Recette(Frame):
	"""Cette frame contient tous le champs pour ajouter une recette"""
	def __init__(self, parentFrame):
		Frame.__init__(self,parentFrame, width=768, height=567)
		self.pack(fill=BOTH)
		self.parentFrame=parentFrame	
		#On attache une recette a la Frame
		self.recette = recette()
		
		#Champ de saisie du nom de la recette
		self.label = Label(self, text="Nom de la recette")
		self.label.pack()
		self.var_nom = StringVar()		
		self.entree_nom = Entry(self,textvariable=self.var_nom,width=75)
		self.entree_nom.pack()

		#LabelFrame pour la selection du type de recette
		self.label_frame_type = LabelFrame(self,text="Selection du type")
		self.label_frame_type.pack()
		self.var_legume = IntVar()		
		self.type_legume = Checkbutton(self.label_frame_type,text="Legume",variable=self.var_legume)
		self.type_legume.pack()
		self.var_viande = IntVar()		
		self.type_viande = Checkbutton(self.label_frame_type,text="Viande",variable=self.var_viande)
		self.type_viande.pack()
		self.var_poisson = IntVar()		
		self.type_poisson = Checkbutton(self.label_frame_type,text="Poisson",variable=self.var_poisson)
		self.type_poisson.pack()
		self.var_puree = IntVar()		
		self.type_puree = Checkbutton(self.label_frame_type,text="Puree",variable=self.var_puree)
		self.type_puree.pack()
		self.var_soupe = IntVar()		
		self.type_soupe = Checkbutton(self.label_frame_type,text="Soupe",variable=self.var_soupe)
		self.type_soupe.pack()
		self.var_salade = IntVar()		
		self.type_salade = Checkbutton(self.label_frame_type,text="Salade",variable=self.var_salade)
		self.type_salade.pack()
		self.var_autre = IntVar()		
		self.type_autre = Checkbutton(self.label_frame_type,text="Autre",variable=self.var_autre)
		self.type_autre.pack()

		
		#LabelFrame pour la selection de la saison
		self.label_frame_saison = LabelFrame(self,text="Selection de la saison")
		self.label_frame_saison.pack()		
		self.var_toutes_saisons = IntVar()		
		self.season_toutes_saisons = Checkbutton(self.label_frame_saison,
			text="Toutes saison",variable=self.var_toutes_saisons)
		self.season_toutes_saisons.pack()
		self.var_ete = IntVar()		
		self.season_ete = Checkbutton(self.label_frame_saison,text="Ete",variable=self.var_ete)
		self.season_ete.pack()
		self.var_hiver = IntVar()		
		self.season_hiver = Checkbutton(self.label_frame_saison,text="Hiver",variable=self.var_hiver)
		self.season_hiver.pack()
		
		#Autres options
		self.var_OK_invites = IntVar()		
		self.bouton_invite = Checkbutton(self, text="OK pour les repas avec invites",variable=self.var_OK_invites)
		self.bouton_invite.pack()
		self.var_preparer_la_veille = IntVar()		
		self.bouton_laveille = Checkbutton(self, text="A preparer la veille",variable=self.var_preparer_la_veille)
		self.bouton_laveille.pack()

		#Annuler
		self.bouton_quitter = Button(self,text="Annuler", command=parentFrame.destroy)
		self.bouton_quitter.pack()
		
		#Sauvegarder
		self.bouton_save = Button(self,text="Sauvegarder",command=self.save_recette)
		self.bouton_save.pack()

	def save_recette(self):
		"""Methode qui permet de sauvegarder la recette"""
		print("recette sauvegardee")
		print(self.recette)

		print("self.var_nom : "+self.var_nom.get())
		self.recette.name=self.var_nom.get()
		print("self.vqr_ete : "+str(self.var_ete.get()))
		if(self.var_ete.get()==1):
			self.recette.season = "ete"
		elif(self.var_hiver.get()==1):
			self.recette.season = "hiver"
		else:
			self.recette.season = "all"


		if self.var_OK_invites.get() == 1:
			self.recette.OK_for_invitee = True

		if self.var_preparer_la_veille.get() == 1:
			self.recette.prepare_day1 = True

		if self.var_legume.get() == 1:
			self.recette.type_recipe = "legume"
		elif self.var_viande.get() == 1:
			self.recette.type_recipe = "viande"
		elif self.var_poisson.get() == 1:
			self.recette.type_recipe = "poisson"
		elif self.var_puree.get() == 1:
			self.recette.type_recipe = "puree"
		elif self.var_soupe.get() == 1:
			self.recette.type_recipe = "soupe"
		elif self.var_salade.get() == 1:
			self.recette.type_recipe = "salade"
		elif self.var_autre .get() == 1:
			self.recette.type_recipe = "autre"
		else:	
			self.recette.type_recipe = "autre"
		
		print(self.recette)

		self.getListOfRecette()
		self.list_recette.append(self.recette)
		self.saveListOfRecette()





		#on quitte la fenetreTopLevel	
		self.parentFrame.destroy()
	

	def getListOfRecette(self):
		os.chdir("./")
		with open('sauvegardeRecette.txt','rb') as fichier:
			try:
				monDePickler = pickle.Unpickler(fichier)
				self.list_recette = monDePickler.load()
			except pickle.PicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("unknown exception raised")

	def saveListOfRecette(self):
		os.chdir("./")
		with open('sauvegardeRecette.txt','wb') as fichier:
			try:
				monPickler = pickle.Pickler(fichier)
				monPickler.dump(self.list_recette)
			except pickle.UnPicklingError as exc:
				print("Excpetion raised : {}".format(exc))
			except pickle.PickleError as exc:
				print("Excpetion raised : {}".format(exc))
			except:
				print("unknown exception raised")




class Main_frame(Frame):
	"""Ma frame generale dans laquelle sont ajoutees les autres frames
	Frame Menu"""
	def __init__(self,parentFrame):
		Frame.__init__(self,parentFrame, width=768, height=567)
		self.pack(fill=BOTH)
		self.frame_menu = Frame_Menu(self)
		self.frame_menu.pack(side="left")
		self.frame_recette = Frame_Recette(self)
		self.frame_recette.pack(side="left")
		self.bouton_aide = Button(self,text="Aide")
		self.bouton_aide.pack(side="left")
		self.bouton_quitter = Button(self,text="Quitter", command=self.quit)
		self.bouton_quitter.pack(side="left")
#		self.menu= Menu(self)
#		self.menu.pack(side="left")
#		photo = PhotoImage(file="chef.png")
#		canvas = Canvas(self,width=80, height=80)
#		canvas.create_image(80, 80, image=photo)
#		canvas.pack(side="bottom")
	
class Frame_Menu(LabelFrame):
	"""La frame qui contient les boutons de gestion du menu"""
	def __init__(self,parent_frame):	
		LabelFrame.__init__(self,parent_frame,text="Generation des menus")
		self.pack(fill=BOTH)
		self.bouton_generer = Button(self,text="Generer le menu",command=self.generer_menu)	
		self.bouton_generer.pack()
		self.bouton_editer = Button(self,text="Editer le profil",command=self.editer_profil_menu)	
		self.bouton_editer.pack()


	def editer_profil_menu(self):
		self.fenetre_editer_profil = Toplevel()
		self.fenetre_editer_profil.grab_set()
		self.fenetre_editer_profil.focus()
		self.frame_editer_profil = Frame_Edit_ProfilSemaine(self.fenetre_editer_profil)

	def generer_menu(self):
		self.fenetre_generer_menu = Toplevel()
		self.fenetre_generer_menu.grab_set()
		self.fenetre_generer_menu.focus()
		self.frame_generer_menu = Frame_generer_menu(self.fenetre_generer_menu)
		


class Frame_Recette(LabelFrame):
	"""La frame qui contient les boutons de gestion du menu"""
	def __init__(self,parent_frame):	
		LabelFrame.__init__(self,parent_frame,text="Gestion des recettes")
		self.pack(fill=BOTH)
		self.bouton_ajout = Button(self,text="Ajouter une recette",command=self.ajouter_recette)	
		self.bouton_ajout.pack()
		self.bouton_editer = Button(self,text="Voir et editer les recettes",command=self.editer_recette)	
		self.bouton_editer.pack()
	
	def ajouter_recette(self):
		self.fenetre_ajouter_recette = Toplevel()
		self.fenetre_ajouter_recette.grab_set()
		self.fenetre_ajouter_recette.focus()
		self.frame_ajouter_recette = Frame_Ajout_Recette(self.fenetre_ajouter_recette)

	def editer_recette(self):
		self.fenetre_editer_recette = Toplevel()
		self.fenetre_editer_recette.grab_set()
		self.fenetre_editer_recette.focus()
		self.frame_editer_recette = Frame_Edit_Recette(self.fenetre_editer_recette)
		
		
fenetre = Tk()
fenetre.configure(width=2000,height=1000)
#interface = Interface(fenetre)
main_frame = Main_frame(fenetre)


#interface.mainloop()
#interface.destroy()
main_frame.mainloop()
main_frame.destroy()


