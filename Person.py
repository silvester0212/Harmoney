import json
import os
import Functions
from pathlib import Path

import Global

_PersonPath = Global.PERSONS_PATH

class Person:
	def __init__ (self, _name):
		self.Name = _name

	def __repr__(self):
		return "Person " + self.Name

	def __dict__(self):
		dict = {}
		dict['Name'] = self.Name
		return dict

	def toJSON(self):
		return json.dumps(self.__dict__(), indent = 4)


def loadPersons():
	PersonsDict = {}

	if (not (Path(_PersonPath)).is_dir()):
		# Persons Path do not exist
		return PersonsDict

	# Persons Path exists, load persons (one person per file)
	for personJsonFile in os.listdir(_PersonPath):
		if (not personJsonFile.endswith('.json')):
			continue

		personJsonObj = json.loads(open(_PersonPath + '/' + personJsonFile).read())
		curPerson = makePersonFromJSON(personJsonObj)
		PersonsDict[curPerson.Name] = curPerson
		print(curPerson)

	return PersonsDict

def makePersonFromJSON(jsonObj):
	name = jsonObj['Name']
	return Person(name)

def makePerson(_name):
	p = Person(_name)
	Functions.makeFile(_PersonPath + '/' + p.Name + '.json', p.toJSON())
	return p

def initializePersons():
	# Initialization of all persons
	PersonSY 		= makePerson("SY")
	PersonMG 		= makePerson("MG")
	PersonBoth 		= makePerson("Both")
	PersonFriend 	= makePerson("Friend")

def getOrMakePerson(_name):
	if (Global.PersonsDict is None):
		Global.PersonsDict = loadPersons()

	if (_name not in Global.PersonsDict):
		newPerson = makePerson(_name)
		Global.PersonsDict[_name] = newPerson

	return Global.PersonsDict[_name]

# initializePersons()

# load Persons to Global
Global.PersonsDict = loadPersons()
