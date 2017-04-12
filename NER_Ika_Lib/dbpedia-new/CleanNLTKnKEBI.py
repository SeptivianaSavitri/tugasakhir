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


def writeDictToFile(aDict, filename):

    thefile = open(filename, "w")

    for key, value in aDict.items() :
        if key != "":
            thefile.write(key.strip())
            thefile.write("\n")

    thefile.close()

    return

##########################################################################
# M A I N
##########################################################################

#set the input and output file
inputNLTK = "en"
inputKEBI = "kebi.txt"
outputNLTK = "nltk_clean.txt"
outputKEBI = "kebi_clean.txt"
outputTMP ="tmp_clean.txt"


inputFile = open(inputNLTK, 'r', errors='ignore')
flines = inputFile.readlines()
dictNLTK = {}
dictTmp = {}
dictKEBI = {}

count = 1
for k in flines:
    k= k.replace("\n","")
    #Jika huruf besar ada di NLTK
    
    if(k[0].isupper()):
        dictTmp[k] = k
    else:
        dictNLTK[k] = k
inputFile.close()

inputFile = open(inputKEBI, 'r', errors='ignore')
flines = inputFile.readlines()


for k in flines:
    k= k.replace("\n","")
    #Jika huruf besar ada di KEBI
    if(k[0].isupper()):
        dictTmp[k] = k
    else:
        dictKEBI[k] = k
inputFile.close()


writeDictToFile(dictNLTK, outputNLTK)
writeDictToFile(dictKEBI, outputKEBI)

writeDictToFile(dictTmp, outputTMP)