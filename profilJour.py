#!/usr/local/bin/python3


def main():
	profil = profilJour("Samedi Soir")
	profil.nom = "Samedi midi"
	profil.type_repas="salade"

	print(profil)

class profilJour:
	"""Cette classe suavegarde le profile de chaque jour de la semaine
	Elle est sauvegardee dans une liste pour constituer le profile de la semaine"""

	def __init__(self,nom):
		self.nom = nom
		self.actif = True
		self.free = False
		self.invite = False
		self.saison = []
		self.plat = "test"
		self.type_repas = []

	def __repr__(self):
		return "Le repas de : {} est actif ? : {}. Le choix est libre ? : {}. \
On veut une {}.  On a des invites ? : {}. \
La saison est {}. Le plat choisi est : {}".format(str(self.nom), str(self.actif), str(self.free), str(self.type_repas),
			str(self.invite), str(self.saison),str(self.plat))


if __name__ == "__main__":
    main()

