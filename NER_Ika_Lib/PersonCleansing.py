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
dictNLTK= {}
nltk_data = "dbpedia-new/nltk_clean.txt"
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
    else:
        newListPerson.append(k)
    count += 1
print("The Streets\n" in newListPerson)
for k in newListPerson:
    arrSplit = k.split(" ")
    for word in arrSplit:
        kataStem = st.stem(word)
        kataVerb = lm.lemmatize('word','v')
        kataLema = lm.lemmatize('word')
        
        if diKamus(kataStem, dictNLTK) or diKamus(kataVerb, dictNLTK) or diKamus(kataLema, dictNLTK):
            countStem = countStem +1
           
        if kataStem == "the":
            countStem = countStem +1
            newListPerson.remove(k)
            newListPersonStem.append(k)
           
inputFile.close()
writeListofStringToFile(newListPerson, output)
writeListofStringToFile(newListTmp, outputtmp)
writeListofStringToFile(newListPersonStem, outputtmpStem)

inputFile = open(inputPlace, 'r', errors='ignore')
flines = inputFile.readlines()
for k in flines:
    newListPlace.append(k)
inputFile.close()
writeListofStringToFile(newListPlace, outputPlace)




############################################################################
# End of file
############################################################################
