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
from function import writeListofStringToFile, writeDictToFile, writeListofStringToFile, writeListofListToFile, stemDiCorpus, findWord, lemmaLongDiCorpus, lemmaDiCorpus, diKamus, buatKamus
from nltk.stem.wordnet import WordNetLemmatizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory



##########################################################################
# M A I N
##########################################################################

#set the input and output file

input = "dbpediaRule/original/person.txt"
inputPlace = "dbpediaRule/original/place.txt"
folder = "dbpediaRule/cleansing/"
output = folder + "personAll.txt"
outputtmp = folder + "tmp.txt"
outputtmpStem = folder + "tmpStem.txt"
outputtmpThe = folder + "tmpThe.txt"
outputtmpAnd = folder + "tmpAnd.txt"
outputtmpNumber = folder + "tmpNumber.txt"

outputtmpInd = folder + "tmpInd.txt"
dictNLTK= {}
dictKEBI = {}
nltk_data = "dbpedia-new/english_corpus.txt"
kebi_data = "dbpedia-new/kebi_clean.txt"
dictNLTK = buatKamus(dictNLTK, nltk_data)
dictKEBI = buatKamus(dictKEBI, kebi_data)
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
newListPersonThe = []
newListPersonAnd = []
newListPersonNumber = []
newListPersonInd = []
cleanStem = []
countStem = 0;
count = 1
cekStem = {}
countCek = 0
st = LancasterStemmer()
lm = WordNetLemmatizer()
factory = StemmerFactory()
stemmer = factory.create_stemmer()
cekHapusKurung = 0
print(findWord("The Pink Panther", "the"))
for k in flines:

	arrSplit = k.split(" ")
	kurung = arrSplit[len(arrSplit) - 1]
	tutup = kurung[len(kurung)-2]

	#PA-1 MODIFIKASI
	if tutup == ")": 
		cekHapusKurung = cekHapusKurung+1
		koorTutup = k.find(tutup) 
		koorBuka = cariBukaKurung(k,koorTutup)
		isiKurung = k[koorBuka+1:koorTutup]
		splitKurung = isiKurung.split(" ")
		if((splitKurung[0] == "band") or (splitKurung[0] == "grup")):
			newListTmp.append(k[:koorBuka])
			newListPersonInd.append(k[:koorBuka])
			k = ""
		#PN-1
		# else:
		# 	k = k[:koorBuka]

			
	arrSplit = k.split(" ")
	#memastikan bahwa kata bukan yang dipindah ke Organization
	if k!="":
	# 	#PA6
		if(arrSplit[0] == "SMA" or arrSplit[0] == "SMP"):   
			newListTmp.append(k)
	# 	#PA5
		elif(k.find("&")!= -1):
			newListPersonAnd.append(k)
		#PA-2
		if(any(i.isdigit() for i in k)):
			newListPersonNumber.append(k)
	# 	#PA-3
		elif(lemmaLongDiCorpus(k,dictNLTK)):
			newListPersonStem.append(k)
		#PA-4
		elif(findWord(k, "the")):
			newListPersonThe.append(k)
			countCek = countCek+1
		else:
			newListPerson.append(k)
		
		if(stemDiCorpus(k, dictKEBI)):
			newListPersonInd.append(k)
inputFile.close()

writeListofStringToFile(newListPerson, output)
writeListofStringToFile(newListTmp, outputtmp)
writeListofStringToFile(newListPersonStem, outputtmpStem)
writeListofStringToFile(newListPersonThe, outputtmpThe)
writeListofStringToFile(newListPersonAnd, outputtmpAnd)
writeListofStringToFile(newListPersonNumber, outputtmpNumber)

writeListofStringToFile(newListPersonInd, outputtmpInd)
print(cekHapusKurung)
inputFile = open(inputPlace, 'r', errors='ignore')
flines = inputFile.readlines()
for k in flines:
	newListPlace.append(k)
inputFile.close()
writeListofStringToFile(newListPlace, outputPlace)




############################################################################
# End of file
############################################################################
