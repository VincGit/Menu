#!/usr/local/bin/python3

import os
import pickle
from recette import recette

def getListOfRecette():
	os.chdir("/home/vincent/Documents/python/menu")
	with open('sauvegardeRecette.txt','rb') as fichier:
		monDePickler = pickle.Unpickler(fichier)
	try:
		listOfRecette = monDePickler.load()
		print("return a list"+listOfRecette)
		return listOfRecette
	except:
		print("exc")
		return []

def saveListOfRecette(iList):
	os.chdir("/home/vincent/Documents/python/menu")

	try:
		with open('sauvegardeRecette.txt','wb') as fichier:
			monPickler = pickle.Pickler(fichier)
			monPickler.dump(iList)
	except :
		print("saveList exc")
	
print("Que voulez vous faire ?")
print("Pour entrer un recette, taper 1")
print("Pour voir les recettes taper 2")
print("Pour voir le menu de la semaine, taper 3")
choix = int(input("Alors ?"))

print("choix :{} ".format(choix))


if choix==1:
	nom = input("nom de la recette :")
	Recette = recette(nom)

	print("nom de la recette : {} ".format(Recette.name))

	#sauvegarder la recette
	listOfRecette = getListOfRecette()
	listOfRecette.append(Recette)
	saveListOfRecette(listOfRecette)	

elif choix==2:
	listOfRecette = getListOfRecette()
	for i,elt in enumerate(listOfRecette):
		print("{} - {}".format(i,elt))

elif choix==3:
	print("TODO, generer le menu")
else:
	print("mauvais choix")




