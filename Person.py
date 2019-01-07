import json
import os
from pathlib import Path

import Functions
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


def getPersonFromJSON(jsonObj):
	name = jsonObj['Name']
	return Person(name)

def createPersonFromName(_name):
	p = Person(_name)
	Functions.makeFile(_PersonPath + '/' + p.Name + '.json', p.toJSON())
	return p

def readPersons():
	PersonsDict = {}

	if (not (Path(_PersonPath)).is_dir()):
		# Persons Path do not exist
		return PersonsDict

	# Persons Path exists, read persons (one person per file)
	for personJsonFile in os.listdir(_PersonPath):
		if (not personJsonFile.endswith('.json')):
			continue

		personJsonObj = json.loads(open(_PersonPath + '/' + personJsonFile).read())
		curPerson = getPersonFromJSON(personJsonObj)
		PersonsDict[curPerson.Name] = curPerson
		# print(curPerson)

	return PersonsDict

def initializePersons():
	# Initialization of all persons
	PersonSY 		= createPersonFromName("SY")
	PersonMG 		= createPersonFromName("MG")
	PersonBoth 		= createPersonFromName("Both")
	PersonFriend 	= createPersonFromName("Friend")

def getOrCreatePerson(_name):
	if (Global.PersonsDict is None):
		Global.PersonsDict = readPersons()

	if (_name not in Global.PersonsDict):
		newPerson = createPersonFromName(_name)
		Global.PersonsDict[_name] = newPerson

	return Global.PersonsDict[_name]

# initializePersons()

# load Persons to Global
Global.PersonsDict = readPersons()
