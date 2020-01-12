# Cost of NPR - 4000 Crore Rupees or 40 Billion Rupees or 563 Million US Dollars just approved :)

"""
Definition of NPR - 

The NPR is a list of "usual residents" of the country. 
A "usual resident" is defined for the purposes of NPR as a person who has resided in a local area 
for the past six months or more or a person who intends to reside in that area for 
the next six months or more.


****************NO SUPPORTING DOCS PROOF REQUIRED***********************

Read more at:
https://economictimes.indiatimes.com/news/politics-and-nation/all-about-national-population-register/articleshow/72953749.cms?utm_source=contentofinterest&utm_medium=text&utm_campaign=cppst
"""

"""
National Register of Citizens (NRC) is a register of all Indian citizens
create the NRC based on the data gathered in the National Population Register (NPR)
List of NPR is checked whether they are citizens or not. to identify illegal immigrants.
Citizens are marked if they are on NPR list but not on NRC.
Basically difference between Population register and Citizen register.
"""


# Citizenship (Amendment) Act, 2019
# official document from Ministry of Law & Justice
# https://www.thehinducentre.com/resources/article30327343.ece
# is it loophole ?
# https://theprint.in/opinion/caa-rules-must-offer-citizenship-only-to-real-not-imagined-refugees/342476/
def createCitizenRecord(religion, date_entered, proof_of_stay_supporting_docs):
	print("Date Entered by the Person : {}".format(date_entered))

	stay_duration = date_of_processing - date_entered

	print("Number of years stayed by the Person in India : {}".format(stay_duration))	
	provide_docs = []

	if religion in ["Hindu", "Sikh", "Jain" "Christian", "Buddhist", "Parsi"]:
		if date_entered <= "31-12-2014" or stay_duration > 6:
			provide_docs.append("Citizen Record Documents")
			return provide_docs
		else:
			print("Wait to complete 6 years in India currently stayed: {}".format(stay_duration))	
			return None
	else:
		if stay_duration > 12 and proof_of_stay_supporting_docs:

			# verification of supporting docs if all good
			provide_docs.append("Citizen Record Documents")
			return provide_docs
		else:
			return None


def createNRCRecord(is_citizen, supporting_docs):
	if is_citizen:
		return True
	else:
		print
		return False 

def getNPRList():
	pass


def getNRCList():
	pass

def isIllegalImmigrant(is_citizen, supporting_docs):
	if is_citizen:
		if supporting_docs:
			if "Citizen Record Documents" in supporting_docs:
				return True
			else:
				# if not valid docs
				return False
	else:
		supporting_docs = createCitizenRecord(religion, date_entered, proof_of_stay_supporting_docs)
		if "Citizen Record Documents" in supporting_docs:
			return True
		else:
			# if not valid docs
			return False 


#chronology 

"""
https://www.businessinsider.in/india/news/what-is-npr-national-population-register-the-center-says-npr-will-be-updated-before-september-2020/articleshow/72963649.cms?utm_source=contentofinterest&utm_medium=text&utm_campaign=cppst
"""
person_1 = {
	religion:"Hindu",
	date_entered: "01-01-2017",
	proof_of_stay_supporting_docs: False
}


person_2 = {
	religion:"Not Hindu",
	date_entered: "01-01-2017",
	proof_of_stay_supporting_docs: False
}

# Now its open..... get the indian citizenship............

# for person 1 
supporting_docs_1 = createCitizenRecord(religion, date_entered, proof_of_stay_supporting_docs)
person_1["supporting_docs"] = createCitizenRecord(religion, date_entered, proof_of_stay_supporting_docs)

# for person 2 
supporting_docs = createCitizenRecord(religion, date_entered, proof_of_stay_supporting_docs)
person_2["supporting_docs"] = createCitizenRecord(religion, date_entered, proof_of_stay_supporting_docs)

# NPR already done in 2010, Updated in 2015 while Aadhar card linking
npr_list = getNPRList() # Home minister said it will be updated September 2020 

nrc_list = getNRCList() # OLD NRC List 

# checking the both list
doubtful_citizens = npr_list - nrc_list

detention_center = []

# updating the NRC
# Home minister said it will be done Nationwide on 1st May 
for person in doubtful_citizens:
	if isIllegalImmigrant(is_citizen, supporting_docs):
		pass
	else:
		detention_center.append(person)


for person in detention_center:
	# deport ?


# view detention center
print(detention_center)
[person_2]
