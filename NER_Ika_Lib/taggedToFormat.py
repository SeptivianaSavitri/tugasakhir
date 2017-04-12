####################################################################################
# taggedToFormat.py
# @Author: Septiviana Savitri
# @Last update: 11 April 2017
# Fasilkom Universitas Indonesia
#
# Objective: From data with tag to data without tag
# input: 
#   - File data tagged

# output: clean version of data :
#    - file data formatted
####################################################################################

#set the input and output file
from test_ner_ika import writeListofStringToFile
inputTag = "goldstandard-0811.txt"
output = "formatted-goldstandard-0811.txt"
outputNoSpace = "nospace-goldstandard-0811.txt"

inputFile = open(inputTag, 'r', errors='ignore')
flines = inputFile.readlines()
listToken = []
listGs = []

count = 1
for k in flines:
    count = count + 1
    if count == 887:
        print(k =="\n")
    if k != ("\n"):
        k= k.replace("\n","")
        #Masukan token
        splitK = k.split("\t")
        listToken.append(splitK[0] + "\n")
        listGs.append(k + "\n")
inputFile.close()



writeListofStringToFile(listToken, output)
writeListofStringToFile(listGs, outputNoSpace)