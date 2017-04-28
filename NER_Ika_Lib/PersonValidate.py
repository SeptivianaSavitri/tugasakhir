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


from function import writeDictToFile, writeListofStringToFile, writeListofListToFile, diKamus, buatKamus, hitungKapital

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/expanded/person.txt"

folder = "dbpedia-new/validate/"
output = folder + "person.txt"
outputtmp = folder + "tmpperson.txt"
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
print(diKamus(("Rolling"), dictNLTK))
dictKebi = buatKamus(dictKebi, kebi_data)
ROMAWI = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
             "XI", "XII", "XIII", "XIV",
             "XX", "XXX"]
BULAN = ["April", "Juni", "Juli"]
count = 1
for k in flines:
    k= k.replace("\n","")
    splitK = k.split(" ")
    

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
    elif(k in BULAN):
        dictTmp[k] = k
    #untuk entity yang berisi 1 kata
    # elif len(splitK) == 1 and "." in k:
    #     dictTmp[k] = k
    elif len(splitK) == 1 and k.isnumeric():
        dictTmp[k] = k
    elif len(k) == 2 and k[1].isupper():
        dictTmp[k] = k
    else: 
        if k in dictTmp:
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
