####################################################################################
# PersonCleansing.py
# @Author: Septiviana Savitri
# @Last update: 28 Februari 2017
# Fasilkom Universitas Indonesia
#
# Objective: To clean the original dbPedia 
# input: 
#   - File contain each type of original data

# output: clean version of data :
#   - every line with (xxx), replaced only by name
#   - every line with (grup xxx)in Person, move to Organization
#   - line that misplaced (SMP and SMA), move to Organization
 
####################################################################################

from __future__ import print_function
from nltk.stem import *
from nltk.stem.lancaster import LancasterStemmer
from function import writeListofStringToFile, writeDictToFile, writeListofStringToFile, writeListofListToFile, diKamus, buatKamus
from nltk.stem.wordnet import WordNetLemmatizer


##########################################################################
# M A I N
##########################################################################

#set the input and output file

input = "dbpedia-new/original/person.txt"
inputPlace = "dbpedia-new/original/place.txt"
folder = "dbpedia-new/cleansing/"
output = folder + "person.txt"
outputtmp = folder + "tmp.txt"
outputtmpStem = folder + "tmpStem.txt"
outputtmpAnd = folder + "tmpAnd.txt"
outputtmpNumber = folder + "tmpNumber.txt"
dictNLTK= {}
nltk_data = "dbpedia-new/english_corpus.txt"
dictNLTK = buatKamus(dictNLTK, nltk_data)
outputPlace = folder + "place.txt"

def cariBukaKurung(kata, pnjg):
	idx = pnjg
	while (idx != 0):
		if kata[idx] == "(":
			return idx
		idx=idx-1

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
newListPerson = []
newListTmp = []
newListPlace = []
newListPersonStem = []
newListPersonAnd = []
newListPersonNumber = []
cleanStem = []
countStem = 0;
count = 1
cekStem = {}

st = LancasterStemmer()
lm = WordNetLemmatizer()

for k in flines:

	arrSplit = k.split(" ")
	kurung = arrSplit[len(arrSplit) - 1]
	tutup = kurung[len(kurung)-2]

	if tutup == ")": 
		koorTutup = k.find(tutup) 
		koorBuka = cariBukaKurung(k,koorTutup)
		isiKurung = k[koorBuka+1:koorTutup]
		splitKurung = isiKurung.split(" ")
		if((splitKurung[0] == "band") or (splitKurung[0] == "grup")):
			newListTmp.append(k[:koorBuka])
		else:
			newListPerson.append(k[:koorBuka])
		
	elif(arrSplit[0] == "SMA" or arrSplit[0] == "SMP"):
		
		newListTmp.append(k)
	elif(k.find("&")!= -1):
		newListPersonAnd.append(k)
	elif(any(i.isdigit() for i in k)):
		newListPersonNumber.append(k)
	else:
		newListPerson.append(k)
	count += 1
print(diKamus("the", dictNLTK))
for k in newListPerson:
	k = k.replace("\n","")
	arrSplit = k.split(" ")
	countStem = 0;
	for word in arrSplit:
		word = word.lower()
		kataVerb = lm.lemmatize(word,'v')
		kataNoun = lm.lemmatize(word,'n')
		kataLema = lm.lemmatize(word)
		
		if diKamus(kataVerb, dictNLTK) or diKamus(kataNoun, dictNLTK) or diKamus(kataLema, dictNLTK):
			countStem = countStem +1

		
	if (countStem == len(arrSplit)):
		newListPersonStem.append(k)
		newListPerson.remove(k+"\n")
for k in newListPerson:
	countThe = 0
	kclean = k.replace("\n","")
	arrSplit = kclean.split(" ")	
	for word in arrSplit:	
		word=word.lower()
		if word =="the" :
			countThe =1
	if countThe!=0:
		
		newListPersonStem.append(k)
		newListPerson.remove(k)
	

		#print(k)
		#u = "LALA"   
# k = "Tony Scott\n"
# k = k.replace("\n","")
# arrSplit = k.split(" ")
# countStem = 0;
# for word in arrSplit:
#     word = word.lower()
#     kataVerb = lm.lemmatize(word,'v')
#     kataNoun = lm.lemmatize(word,'n')
#     kataLema = lm.lemmatize(word)
#     print(kataLema)
#     print(kataVerb)  
#     print(kataNoun)
	
#     if  diKamus(kataVerb, dictNLTK) or diKamus(kataNoun, dictNLTK) or diKamus(kataLema, dictNLTK):
#         countStem = countStem +1

# print("ini countStem " + str(countStem))
# print("ini arrSplit " + str(len(arrSplit)))
# if (countStem == len(arrSplit)):
#     print(k)     
inputFile.close()
writeListofStringToFile(newListPerson, output)
writeListofStringToFile(newListTmp, outputtmp)
writeListofStringToFile(newListPersonStem, outputtmpStem)
writeListofStringToFile(newListPersonAnd, outputtmpAnd)
writeListofStringToFile(newListPersonNumber, outputtmpNumber)

inputFile = open(inputPlace, 'r', errors='ignore')
flines = inputFile.readlines()
for k in flines:
	newListPlace.append(k)
inputFile.close()
writeListofStringToFile(newListPlace, outputPlace)




############################################################################
# End of file
############################################################################
