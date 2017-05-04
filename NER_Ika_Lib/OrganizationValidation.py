####################################################################################
# OrganizationValidation.py
# @Author: Septiviana Savitri
# @Last update: 17 April 2017
# Fasilkom Universitas Indonesia
#
# Objective: To validate the data from expanded file
# input: 
#   - File contain organization expanded and listPartai

# output: unique version of data :
#    - merge all data in dictionary (make sure all entities are unique)
####################################################################################


from function import writeDictToFile, cariBukaKurung, buatKamus, diKamus

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input1 = "dbpedia-new/expanded/organization.txt"
input2 = "dbpedia-new/expanded/listPartai.txt"

input3 = "dbpedia-new/original/listInstansi.txt"
folder = "dbpedia-new/validate/"
output = folder + "organization.txt"
outputtmp = folder + "tmporg.txt"

nltk_data = "dbpedia-new/nltk_clean.txt"
kebi_data = "dbpedia-new/kebi_clean.txt"
dictKebi = {}
dictNLTK = {}



#########################  begin ################################


dictNLTK = buatKamus(dictNLTK, nltk_data)

dictKebi = buatKamus(dictKebi, kebi_data)
ROMAWI = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
             "XI", "XII", "XIII", "XIV",
             "XX", "XXX"]
count = 1

inputFile = open(input1, 'r', errors='ignore')
flines = inputFile.readlines()
newDictOrg = {}
dictTmp = {}
count = 1
for k in flines:
    k= k.replace("\n","")
    if(diKamus(k, dictKebi)):
        dictTmp[k] = k
        
    #jika nama ada di nltk
    elif(diKamus(k, dictNLTK)):
        dictTmp[k] = k
    elif(len(k) <2):
        dictTmp[k] = k
    elif(k in ROMAWI):
        dictTmp[k] = k
    else:
        newDictOrg[k] = k
    count += 1
inputFile.close()

inputFile = open(input2, 'r', errors='ignore')
flines = inputFile.readlines()


for k in flines:
    k= k.replace("\n","")
    if(diKamus(k, dictKebi)):
        dictTmp[k] = k
    #jika nama ada di nltk
    elif(diKamus(k, dictNLTK)):
        dictTmp[k] = k
    elif(len(k) <2):
        dictTmp[k] = k
    elif(k in ROMAWI):
        dictTmp[k] = k
    else:
        newDictOrg[k] = k
    count += 1
inputFile.close()

inputFile = open(input3, 'r', errors='ignore')
flines = inputFile.readlines()


for k in flines:
    k= k.replace("\n","")
    if(diKamus(k, dictKebi)):
        dictTmp[k] = k
    #jika nama ada di nltk
    elif(diKamus(k, dictNLTK)):
        dictTmp[k] = k
    elif(len(k) <2):
        dictTmp[k] = k
    elif(k in ROMAWI):
        dictTmp[k] = k
    else:
        newDictOrg[k] = k
    count += 1
inputFile.close()

writeDictToFile(newDictOrg, output)
writeDictToFile(dictTmp, outputtmp)




#########################  begin ################################


