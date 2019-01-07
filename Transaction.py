from datetime import datetime
from dateutil import parser as DateTimeParser

import Global
import Person
import Account

class Transaction:
	def __init__(self, _DateTimeStr, _amt, _personName, _category, _business, _acctName):
		self.DateTime 	= DateTimeParser.parse(_DateTimeStr)
		self.Amount		= _amt
		self.Person		= Person.getOrCreatePerson(_personName)
		self.Category	= _category
		self.Business	= _business
		self.Account	= Account.getOrCreateAccount(_acctName)

	def __repr__(self):
		return (
			"Transaction\n" +
			"DateTime = " + str(self.DateTime) + "\n" +
			"Amount   = " + str(self.Amount) + "\n" +
			"Person   = " + self.Person.Name + "\n" +
			"Category = " + self.Category + "\n" +
			"Account  = " + self.Account.AcctName + "\n"
		)


TransactionsLst = []

TransactionsLst.append( Transaction('1/1/2019 13:05',		40.00,			"Both",		"Lunch",	"QQ Noodle",				"S_Cash"))
TransactionsLst.append( Transaction('1/1/2019 8:09:04P', 	31.50 / 3 * 2,	"Both", 	"Dining", 	"New Tung Kee Noodle", 		"S_Chase_CSP"))
TransactionsLst.append( Transaction('1/1/2019 8:09:04P', 	31.50 / 3,		"Friend", 	"Dining", 	"New Tung Kee Noodle", 		"S_Chase_CSP"))
TransactionsLst.append( Transaction('1/1/2019 1:12:47PM',	4.00, 			"Both",   	"Desert", 	"Sheng Kee Bakery & Cafe", 	"S_Cash"))
TransactionsLst.append( Transaction('1/1/2019 1:29PM',   	6.90,			"Both", 	"Coffee", 	"Starbucks", 				"GC_Starbucks"))
TransactionsLst.append( Transaction('1/2/2019 11:29 AM',	5.24,			"Both",		"Living",	"USPS",						"M_Chase_Freedom"))
TransactionsLst.append( Transaction('1/2/2019 11:44 AM', 	40.40,			"Both",		"Gas",		"Costco Gas", 				"S_YYZ_ICBC"))
TransactionsLst.append( Transaction('1/2/2019 12:12 PM',	65.96,			"Both",		"Living", 	"Costco Wholesale", 		"S_YYZ_ICBC"))
TransactionsLst.append( Transaction('1/2/2019 1:23 PM',		41.00,			"Both",		"Dining",	"Boiling Point", 			"S_Chase_CSP"))
TransactionsLst.append( Transaction('1/2/2019 17:26:15', 	17.51,			"Both",		"Living", 	"VIP Cleaners", 			"S_YYZ_ICBC"))
TransactionsLst.append( Transaction('1/2/2019 17:26:14', 	45,				"Both",		"Living", 	"VIP Cleaners", 			"M_Chase_IHG"))
TransactionsLst.append( Transaction('1/2/2019 8:51 PM',		34,				"Both",		"Dining",	"Venus Cafe",				"M_Venmo"))
TransactionsLst.append( Transaction('1/3/2019 1:47 PM',		95.00,			"MG",		"Hospital",	"Pain Management & Acupuncture Healing",	"S_Cash"))
TransactionsLst.append( Transaction('1/3/2019 2:01 PM',		23.00,			"Both",		"Lunch",	"Taiwan Porridge Kingdom",	"S_Cash"))
TransactionsLst.append( Transaction('1/3/2019 2:39 PM',		6.15,			"MG",		"Hospital",	"Valley Radiology Imaging",	"S_BoA_FIA"))
TransactionsLst.append( Transaction('1/3/2019 19:45:42',	33.49,			"Both",		"Dining",	"Chef Liu Restaurant",		"S_Chase_CSP"))
TransactionsLst.append( Transaction('1/4/2019 9:53',		3.45,			"SY",		"Coffee",	"Starbucks",				"GC_Starbucks"))
TransactionsLst.append( Transaction('1/4/2019 12:07',		98.00,			"MG",		"Beauty",	"La Belle Beauty",			"M_Venmo"))
TransactionsLst.append( Transaction('1/4/2019 13:09:18',	43.65,			"Both",		"Lunch",	"Pottastic",				"S_Chase_CSP"))
TransactionsLst.append( Transaction('1/4/2019 1:55 PM',		3.22,			"Both",		"Coffee",	"VillaSport Athletic Club",	"S_Chase_AARP"))
TransactionsLst.append( Transaction('1/4/2019 8:15:39 PM',	50.00,			"Both",		"Living",	"99 Ranch Market",			"S_Cash"))
TransactionsLst.append( Transaction('1/4/2019 8:28:22 PM',	8.38,			"Both",		"Living",	"99 Ranch Market",			"S_Alipay"))
TransactionsLst.append( Transaction('1/5/2019 0:14',		9.99,			"Both",		"Living",	"Amazon",					"M_Chase_Freedom"))
TransactionsLst.append( Transaction('1/5/2019 12:00 PM',	33.00,			"Both",		"Lunch",	"Joyheart Cafe",			"S_Cash"))
TransactionsLst.append( Transaction('1/5/2019 12:43 PM',	5.41,			"Both",		"Coffee",	"VillaSport Athletic Club",	"S_Citi_DC"))
TransactionsLst.append( Transaction('1/5/2019 19:14',		38.00,			"Both",		"Dining",	"Ma's Restaurant",			"S_Venmo"))
TransactionsLst.append( Transaction('1/5/2019 19:52',		151.06,			"Both",		"Living",	"Bliss Wisdom NorCal",		"M_Chase_IHG"))
TransactionsLst.append( Transaction('1/6/2019 1:05 PM',		47.00,			"Both",		"Lunch",	""))
TransactionsLst.append( Transaction('1/6/2019 18:41',		23.00,			"Both",		"Dining",	"Dong Phuong Tofu",			"S_Cash"))

print("\n".join(str(t) for t in TransactionsLst))