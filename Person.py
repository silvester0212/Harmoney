import json
import Functions
from Global import *

class Person:
	def __init__ (self, _name, _abrv):
		self.Name = _name
		self.Abbreviation = _abrv

	def __repr__(self):
		return "Person " + self.Name + " w/ Abbreviation " + self.Abbreviation

	def __dict__(self):
		dict = {}
		dict['name'] = self.Name
		dict['abrv'] = self.Abbreviation
		return dict

	def toJSON(self):
		# return json.dumps(self, default=lambda o:o.__dict__(), sort_keys = False, indent = 4)
		return json.dumps(self.__dict__(), indent = 4)


def loadPersons():
	PersonsObj = json.loads(open(PERSONS_FILE).read())
	PersonsLst = []
	# print(Persons)

	for p in PersonsObj:
		personObj = json.loads(p)
		PersonsLst.append(makePersonFromJSON(personObj))

	return PersonsLst

def makePersonFromJSON(jsonObj):
	name = jsonObj["name"]
	abrv = jsonObj["abrv"]
	return Person(name, abrv)

def makePerson(_name, _abrv):
	return Person(_name, _abrv)

def initializePersons():
	# Initialization
	Persons = []
	PersonSY = makePerson("Silvester Yao", "SY")
	PersonMG = makePerson("Menglu Gao", "MG")
	PersonBoth = makePerson("Both", "Both")
	# Functions.makeFile(PERSONS_FILE, json.dumps(PersonSY.__dict__()))
	Persons.append(PersonSY)
	Persons.append(PersonMG)
	Persons.append(PersonBoth)
	Functions.makeFile(PERSONS_FILE, json.dumps([p.toJSON() for p in Persons]))

# initializePersons()

PersonsLst = loadPersons()

for person in PersonsLst:
	print(person)