#!/usr/local/bin/python3

from tkinter import *
import os
from Course import *
from profilSemaine import *
from frameGenerer import *
from FrameEditCourse import *
from FrameAddCourse import *
import pickle


class MainFrame(Frame):
	"""Ma frame generale dans laquelle sont ajoutees les autres frames
	Frame Menu"""
	def __init__(self,parentFrame):
		Frame.__init__(self,parentFrame, width=768, height=567)
		self.pack(fill=BOTH)
		self.frame_menu = FrameMenu(self)
		self.frame_menu.pack(side="left")
		self.frame_course = FrameCourse(self)
		self.frame_course.pack(side="left")
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
	
class FrameMenu(LabelFrame):
	"""This frame contains the buttons to handle the menu
	It is inserted in the main window"""
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
		self.frame_editer_profil = MasterFrameEditProfilSemaine(self.fenetre_editer_profil)

	def generer_menu(self):
		self.fenetre_generer_menu = Toplevel()
		self.fenetre_generer_menu.grab_set()
		self.fenetre_generer_menu.focus()
		self.frame_generer_menu = FrameGenererMenu(self.fenetre_generer_menu)
		


class FrameCourse(LabelFrame):
	"""This frame contains the buttons to handle the courses
	It is inserted in the main window"""
	def __init__(self,parent_frame):	
		LabelFrame.__init__(self,parent_frame,text="Gestion des Courses")
		self.pack(fill=BOTH)
		self.bouton_ajout = Button(self,text="Ajouter un plat",command=self.ajouter_course)	
		self.bouton_ajout.pack()
		self.bouton_editer = Button(self,text="Voir et editer les Courses",command=self.editer_course)	
		self.bouton_editer.pack()
	
	def ajouter_course(self):
		self.fenetre_ajouter_course = Toplevel()
		self.fenetre_ajouter_course.grab_set()
		self.fenetre_ajouter_course.focus()
		self.frame_ajouter_course = FrameAddCourse(self.fenetre_ajouter_course)

	def editer_course(self):
		self.fenetre_editer_course = Toplevel()
		self.fenetre_editer_course.grab_set()
		self.fenetre_editer_course.focus()
		self.frame_editer_course = FrameManageCourse(self.fenetre_editer_course)
		
		
fenetre = Tk()
fenetre.configure(width=2000,height=1000)
#interface = Interface(fenetre)
main_frame = MainFrame(fenetre)


#interface.mainloop()
#interface.destroy()
main_frame.mainloop()
main_frame.destroy()


