#!/usr/local/bin/python3

import os
import pickle
from recette import recette

def getListOfRecette():
	os.chdir("/home/vincent/Documents/python/Menu")
	with open('sauvegardeRecette.txt','rb') as fichier:
#		print("type of file : {}".format(type(fichier)))
#		print("content of file : {}".format(fichier))
		try:
			monDePickler = pickle.Unpickler(fichier)
			listOfRecette = monDePickler.load()
			return listOfRecette
		except pickle.PicklingError as exc:
			print("Excpetion raised : {}".format(exc))
			return []
		except pickle.PickleError as exc:
			print("Excpetion raised : {}".format(exc))
			return []
		except:
			print("unknown exception raised")
			return []

def saveListOfRecette(iList):
	os.chdir("/home/vincent/Documents/python/Menu")
	with open('sauvegardeRecette.txt','wb') as fichier:
		try:
			monPickler = pickle.Pickler(fichier)
			monPickler.dump(iList)
		except pickle.UnPicklingError as exc:
			print("Excpetion raised : {}".format(exc))
			return []
		except pickle.PickleError as exc:
			print("Excpetion raised : {}".format(exc))
			return []
		except:
			print("unknown exception raised")
			return []
	
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
	print("Size of the list : {}".format(len(listOfRecette)))
	print(listOfRecette)
	for i,elt in enumerate(listOfRecette):
		print("{} - {}".format(i,elt.name))

elif choix==3:
	print("TODO, generer le menu")
else:
	print("mauvais choix")




