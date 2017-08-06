####################################################################################
# CleanNLTKnKEBI.py
# @Author: Septiviana Savitri
# @Last update: 5 April 2017
# Fasilkom Universitas Indonesia
#
# Objective: To clean the input of corpora in NLTK and KEBI
# input: 
#   - File NLTK and KEBI

# output: clean version of data :
#    - no uppercase in first word
####################################################################################
import operator

def writeDictToFile(aDict, filename):

    thefile = open(filename, "w")

    for key, value in aDict.items() :
        if key != "":
            thefile.write(key.strip())
            thefile.write("\n")

    thefile.close()

    return

def writeListofStringToFile(aList, filename):

    thefile = open(filename, "w", errors='replace')

    for k in aList:
        thefile.write(k.strip())
        thefile.write("\n")

    thefile.close()

    return

##########################################################################
# M A I N
##########################################################################

#set the input and output file
inputNLTK = "en"
inputKEBI = "kebi.txt"
inputAgama = "listAgama.txt"
outputNLTK = "nltk_clean.txt"
outputKEBI = "kebi_clean.txt"
outputTMPNLTK ="tmp_cleanNLTK.txt"
outputTMPKEBI ="tmp_cleanKEBI.txt"

inputFile = open(inputNLTK, 'r', errors='ignore')
flines = inputFile.readlines()
dictNLTK = {}
dictTmpNLTK = {}
dictTmpKEBI = {}
dictKEBI = {}
soretedNLTK={}

count = 1
for k in flines:
    k= k.replace("\n","")
    #Jika huruf besar ada di NLTK
    
    if(k[0].isupper()):
        dictTmpNLTK[k] = k
    else:
        dictNLTK[k] = k
inputFile.close()

inputFile = open(inputKEBI, 'r', errors='ignore')
flines = inputFile.readlines()


for k in flines:
    k= k.replace("\n","")
    #Jika huruf besar ada di KEBI
    if(k[0].isupper()):
        dictTmpKEBI[k] = k
    else:
        dictKEBI[k] = k

inputFile.close()
inputFile = open(inputAgama, "r", errors="ignore")
flines = inputFile.readlines()
for k in flines:
    dictKEBI[k] = k
sortedNLTK = sorted(dictNLTK.values())
sortedKEBI = sorted(dictKEBI.values())
sortedTmpNLTK = sorted(dictTmpNLTK.values())
sortedTmpKEBI = sorted(dictTmpKEBI.values())
writeListofStringToFile(sortedNLTK, outputNLTK)
writeListofStringToFile(sortedKEBI, outputKEBI)

writeListofStringToFile(sortedTmpNLTK, outputTMPNLTK)
writeListofStringToFile(sortedTmpKEBI, outputTMPKEBI)