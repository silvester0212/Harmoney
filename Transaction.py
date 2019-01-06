from datetime import datetime
from dateutil import parser as DateTimeParser

import Global
import Person

class Transaction:
	def __init__(self, _DateTimeStr, _amt, _personName, _category, _business, _acct):
		self.DateTime 	= DateTimeParser.parse(_DateTimeStr)
		self.Amount		= _amt
		self.Person		= Person.getOrMakePerson(_personName)
		self.Category	= _category
		self.Business	= _business
		self.Account	= _acct

	def __repr__(self):
		return (
			"Transaction\n" +
			"DateTime\t" + str(self.DateTime) + "\n" +
			"Amount\t\t" + str(self.Amount) + "\n" +
			""
			"Person\t\t" + self.Person.Name + "\n"
			"Category\t" + self.Category + "\n"
		)


# transDateTime1Str = '1/1/2019 1:12:47 PM'
# person = Person("Silvester Yao", "SY")
# t1 = Transaction(transDateTime1Str, 15.50, person, "Dining",)

# personBoth = Person("Both", "Both")
# personFriend = Person("Friend", "Friend")
# personMenglu = Person("Menglu Gao", "MG")
# personSY = Person("Silvester Yao", "SY")

TransactionsLst = []

print(Global.PersonsDict)

TransactionsLst.append( Transaction('1/1/2019 13:05',		40.00,			"Both",		"Lunch",	"QQ Noodle",				"S Cash"))
TransactionsLst.append( Transaction('1/1/2019 8:09:04P', 	31.50 / 3 * 2,	"Both", 	"Dining", 	"New Tung Kee Noodle", 		"S Chase CSP"))
TransactionsLst.append( Transaction('1/1/2019 8:09:04P', 	31.50 / 3,		"Friend", 	"Dining", 	"New Tung Kee Noodle", 		"S Chase CSP"))
TransactionsLst.append( Transaction('1/1/2019 1:12:47PM',	4.00, 			"Both",   	"Desert", 	"Sheng Kee Bakery & Cafe", 	"S Cash"))
TransactionsLst.append( Transaction('1/1/2019 1:29PM',   	6.90,			"Both", 	"Coffee", 	"Starbucks", 				"GC - Starbucks"))
TransactionsLst.append( Transaction('1/2/2019 11:29 AM',	5.24,			"Both",		"Living",	"USPS",						"M Chase Freedom"))
TransactionsLst.append( Transaction('1/2/2019 11:44 AM', 	40.40,			"Both",		"Gas",		"Costco Gas", 				"S YYZ ICBC"))
TransactionsLst.append( Transaction('1/2/2019 12:12 PM',	65.96,			"Both",		"Living", 	"Costco Wholesale", 		"S YYZ ICBC"))
TransactionsLst.append( Transaction('1/2/2019 1:23 PM',		41.00,			"Both",		"Dining",	"Boiling Point", 			"S Chase CSP"))
TransactionsLst.append( Transaction('1/2/2019 17:26:15', 	17.51,			"Both",		"Living", 	"VIP Cleaners", 			"S YYZ ICBC"))
TransactionsLst.append( Transaction('1/2/2019 17:26:14', 	45,				"Both",		"Living", 	"VIP Cleaners", 			"M Chase IHG"))
TransactionsLst.append( Transaction('1/2/2019 8:51 PM',		34,				"Both",		"Dining",	"Venus Cafe",				"M Venmo"))
TransactionsLst.append( Transaction('1/3/2019 1:47 PM',		95.00,			"MG",		"Hospital",	"Pain Management & Acupuncture Healing",	"S Cash"))
TransactionsLst.append( Transaction('1/3/2019 2:01 PM',		23.00,			"Both",		"Lunch",	"Taiwan Porridge Kingdom",	"S Cash"))
TransactionsLst.append( Transaction('1/3/2019 2:39 PM',		6.15,			"MG",		"Hospital",	"Valley Radiology Imaging",	"S BoA FIA"))
TransactionsLst.append( Transaction('1/3/2019 19:45:42',	33.49,			"Both",		"Dining",	"Chef Liu Restaurant",		"S Chase CSP"))
TransactionsLst.append( Transaction('1/4/2019 9:53',		3.45,			"SY",		"Coffee",	"Starbucks",				"GC - Starbucks"))
TransactionsLst.append( Transaction('1/4/2019 12:07',		98.00,			"MG",		"Beauty",	"La Belle Beauty",			"M Venmo"))
TransactionsLst.append( Transaction('1/4/2019 8:15:39 PM',	50.00,			"Both",		"Living",	"99 Ranch Market",			"S Cash"))
TransactionsLst.append( Transaction('1/4/2019 8:28:22 PM',	8.38,			"Both",		"Living",	"99 Ranch Market",			"S Alipay"))
TransactionsLst.append( Transaction('1/5/2019 0:14',		9.99,			"Both",		"Living",	"Amazon",					"M Chase Freedom"))
TransactionsLst.append( Transaction('1/5/2019 12:00 PM',	33.00,			"Both",		"Lunch",	"Joyheart Cafe",			"S Cash"))
TransactionsLst.append( Transaction('1/5/2019 12:43 PM',	5.41,			"Both",		"Coffee",	"VillaSport Athletic Club",	"S Citi DC"))

print(Global.PersonsDict)

print("\n".join(str(t) for t in TransactionsLst))