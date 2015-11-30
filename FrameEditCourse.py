#!/usr/local/bin/python3

import os

from tkinter import *
import pickle

from Course import *
from profilSemaine import *
from frameGenerer import *
from FrameAddCourse import *


class FrameManageCourse(Frame):
	"""This frame contains all the features to edit a Course"""
	def __init__(self, parentFrame):
		Frame.__init__(self,parentFrame, width=768, height=567)
		self.pack(fill=BOTH)
		self.parentFrame=parentFrame	
		#the list_course contains the list of available courses
		self.list_course=[]
		
		#On construit la liste qui contient les Courses		
		self.listebox_course = Listbox(self)
		self.listebox_course.pack()
		self.getListOfCourses()
		self.fill_listbox_course()		

		self.label_frame_action = LabelFrame(self,text="Actions")
		self.label_frame_action.pack()
		self.bouton_editer = Button(self.label_frame_action,text="Editer",command=self.edit_course)
		self.bouton_editer.pack()
		self.bouton_supprimer = Button(self.label_frame_action,text="Supprimer",command=self.delete_course)
		self.bouton_supprimer.pack()
		
		#Quitter
		self.bouton_quitter = Button(self,text="Quitter", command=self.parentFrame.destroy)
		self.bouton_quitter.pack()

	def delete_course(self):
		"""This method deletes the selected course"""
		index_course = self.listebox_course.curselection()
		if(not index_course):
			print("Pas de selection,pas d'action")
		else:
			index = index_course[0]
			del self.list_course[index]
			self.fill_listbox_course()
			self.saveListOfCourses()

	def edit_course(self):
		"""This method opens a frame prefilled with the course attributes
		it allows the user to change the values and save it"""
		index_course = self.listebox_course.curselection()
		if(not index_course):
			print("Pas de selection,pas d'action")
		else:
			index = index_course[0]
			print("DEBUG : edit_course; index : {}".format(str(index)))
			self.window_edit_course = Toplevel()
			self.window_edit_course.grab_set()
			self.window_edit_course.focus()
			self.edit_course = FrameEditCourse(self.window_edit_course,
				self.list_course[index])
	
	def fill_listbox_course(self):
		self.listebox_course.delete(0,self.listebox_course.size())
		for i,Course in enumerate(self.list_course):
			self.listebox_course.insert(END, Course.name)
		


			
	def getListOfCourses(self):
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
				print("unknown exception raised")

	def saveListOfCourses(self):
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
				print("unknown exception raised")

class FrameEditCourse(FrameAddCourse):
	"""This class enable to load a Course edit it and save it"""
	def __init__(self,parentFrame,course):
		FrameAddCourse.__init__(self,parentFrame)
		self.course = course
		self.grid(row=0,column=0)
		self.loadCourse()

	def loadCourse(self):

		self.Course.name=self.var_nom.get()
		self.entree_nom.insert(0,self.course.name)	

		if self.course.season == "Seulement ete":
			self.season_ete.select()
		elif self.course.season == "seulement hiver":
			self.season_hiver.select()
		else:
			self.season_toutes_saisons.select()

		if self.course.OK_for_invitee:
			self.bouton_invite.select()

		if self.course.prepare_day1:
			self.bouton_laveille.select()		


		if self.course.type_course == "Legume":
			self.type_legume.select()
		if self.course.type_course == "Viande":
			self.type_viande.select()
		if self.course.type_course == "Poisson":
			self.type_poisson.select()
		if self.course.type_course == "Puree":
			self.type_puree.select()
		if self.course.type_course == "Soupe":
			self.type_soupe.select()
		if self.course.type_course == "Salade":
			self.type_salade.select()
		if self.course.type_course == "Autres":
			self.type_autres.select()
		

