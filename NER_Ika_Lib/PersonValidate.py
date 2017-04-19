####################################################################################
# PersonValidate.py
# @Author: Septiviana Savitri
# @Last update: 28 Februari 2017
# Fasilkom Universitas Indonesia
#
# Objective: To validate all the expanded data of Person in DBPedia 
# input: 
#   - File contain each type of expanded data

# output: validated version of data , remove all :
   # - word in KBBI or NLTK
   # - word in roman number
   # - word contain period
   # - word length 1
   # - word with all uppercase letter

 
####################################################################################


from function import writeDictToFile, writeListofStringToFile, writeListofListToFile, diKamus, buatKamus

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/expanded/person.txt"

folder = "dbpedia-new/validate/"
output = folder + "person.txt"
outputtmp = folder + "tmp.txt"
nltk_data = "dbpedia-new/nltk_clean.txt"
kebi_data = "dbpedia-new/kebi_clean.txt"
dictKebi = {}
dictNLTK = {}
#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
dictPerson = {}
dictTmp = {}

dictNLTK = buatKamus(dictNLTK, nltk_data)

dictKebi = buatKamus(dictKebi, kebi_data)
ROMAWI = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
             "XI", "XII", "XIII", "XIV",
             "XX", "XXX"]
count = 1
print(diKamus("Superman",dictNLTK ))
for k in flines:
    k= k.replace("\n","")
    #Jika nama ada di kebi
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
        dictPerson[k] = k
inputFile.close()



writeDictToFile(dictPerson, output)

writeDictToFile(dictTmp, outputtmp)
#writeListofStringToFile(newListTmp, outputtmp)



############################################################################
# End of file
############################################################################
