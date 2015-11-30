#!/usr/local/bin/python3


def main():
	aCourse = Course()
	aCourse.name = "My test name"
	aCourse.prepare_day1 = True
	aCourse.OK_for_invite = False
	aCourse.season = "hiver"
	aCourse.type_course = "soupe"
	aCourse.recipe = "The recipe"
	aCourse.link = "http://myLink.com"
	aCourse.list_ingredient.append("Eggs")

	print(aCourse)    


class Course:
	""" This class contains all the attributes and methods of the  Course
	its name,
	its list of (ingredients)
	its properties """
	def __init__(self):
		self.name = ""
		self.prepare_day1 = False
		self.OK_for_invitee = False
		self.season = ""
		self.type_course = ""
		self.list_ingredient = []
		self.recipe = ""
		self.link = ""

	def __repr__(self):
		return "Course name: {}; type: {}; season: {}; OK for invitee ?: \
{}; Prepare the day before ?: {}; recipe: {}; link: {} ".format(self.name,self.type_course,
			self.season,self.OK_for_invitee,self.prepare_day1,self.recipe,self.link)


if __name__ == '__main__':
	main()



