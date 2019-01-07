import json
import os
from pathlib import Path

import Global
import Functions

_AcctPath = Global.ACCOUNTS_PATH

class Account:
	def __init__(self, _name, _fullName, _owner, _business, _card):
		self.AcctName 	= _name
		self.FullName 	= _fullName
		self.Owner		= _owner
		self.Business	= _business
		self.Card		= _card

	def __repr__(self):
		return (
			'AcctName = ' + self.AcctName + '\n' +
			'FullName = ' + ('None' if (self.FullName is None) else self.FullName) + '\n' +
			'Owner    = ' + ('None' if (self.Owner is None) else self.Owner) + '\n' +
			'Business = ' + ('None' if (self.Business is None) else self.Business) + '\n' +
			'Card     = ' + ('None' if (self.Card is None) else self.Card) + '\n'
		)

	def __dict__(self):
		acctDict = {}
		acctDict['AcctName'] = self.AcctName
		acctDict['FullName'] = self.FullName
		acctDict['Owner']	 = self.Owner
		acctDict['Business'] = self.Business
		acctDict['Card']	 = self.Card
		return acctDict

	def toJSON(self):
		return json.dumps(self.__dict__(), indent = 4)

def getAccountFromJSON(acctJsonObj):
	_acctName		= acctJsonObj['AcctName']
	_acctFullName	= acctJsonObj['FullName']
	_acctOwner		= acctJsonObj['Owner']
	_acctBusiness	= acctJsonObj['Business']
	_acctCard		= acctJsonObj['Card']

	return Account(_acctName, _acctFullName, _acctOwner, _acctBusiness, _acctCard)

def createAccountFromName(_acctName):
	acct = Account(_acctName, None, None, None, None)
	Functions.makeFile(_AcctPath + '/' + acct.AcctName + '.json', acct.toJSON())
	return acct


def readAccts():
	AcctsDict = {}

	if (not Path(_AcctPath).is_dir()):
		# Account Path do not exist
		return AcctsDict

	# Accounts Path exists, load accounts (one account per file)
	for acctJsonFile in os.listdir(_AcctPath):
		if (not acctJsonFile.endswith('.json')):
			continue

		acctJsonObj = json.loads(open(_AcctPath + '/' + acctJsonFile).read())
		curAcct = getAccountFromJSON(acctJsonObj)
		AcctsDict[curAcct.AcctName] = curAcct
		# print(curAcct)

	return AcctsDict

def getOrCreateAccount(_name):
	if (Global.AcctsDict is None):
		Global.AcctsDict = readPersons()

	if (_name not in Global.AcctsDict):
		newAcct = createAccountFromName(_name)
		Global.AcctsDict[_name] = newAcct

	return Global.AcctsDict[_name]

Global.AcctsDict = readAccts()

# readAccts()