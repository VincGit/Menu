#!/usr/local/bin/python3

class recette:
	""" This class contains all the attributes and methods of the  recette
	its name,
	its list of (ingredients)
	its properties """
	def __init__(self):
		self.name = ""
		self.prepare_day1 = False
		self.OK_for_invitee = False
		self.season = ""
		self.type_recipe = ""

	def __repr__(self):
		return "recette : {}; type : {}; saison : {}; OK for invitee ? : {} ".format(self.name,
			self.type_recipe,self.season,self.OK_for_invitee)


