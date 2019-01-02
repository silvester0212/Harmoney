import json

class Person:
	def __init__ (self, _name, _abrv):
		self.Name = _name
		self.Abbreviation = _abrv

	def toJson(self):
		data = {}
		data['name'] = self.Name
		data['abrv'] = self.Abbreviation
		return data


def makePerson(_name, _abrv):
	p = Person(_name, _abrv)
	print(p.toJson())


makePerson("Silvester Yao", "SY")