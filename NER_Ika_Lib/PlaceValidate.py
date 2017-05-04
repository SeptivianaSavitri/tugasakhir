####################################################################################
# PlaceValidate.py
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


from function import writeDictToFile, writeListofListToFile, writeListofStringToFile, diKamus, buatKamus, writeDictWithValueToFile


##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/expanded/place.txt"

folder = "dbpedia-new/validate/"
output = folder + "place.txt"
outputtmp = folder + "tmpplace.txt"
nltk_data = "dbpedia-new/nltk_clean.txt"
kebi_data = "dbpedia-new/kebi_clean.txt"
dictKebi = {}
dictNLTK = {}


#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
dictPlace = {}
dictTmp = {}

dictNLTK = buatKamus(dictNLTK, nltk_data)

dictKebi = buatKamus(dictKebi, kebi_data)
ROMAWI = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
             "XI", "XII", "XIII", "XIV",
             "XX", "XXX"]
BULAN = ["April", "Juni", "Juli"]
# print(diKamus("Arab",dictKebi))
count = 1
for k in flines:
    k= k.replace("\n","")
    k = k.replace("  "," ")
    #Jika nama ada di kebi
    if(diKamus(k, dictKebi)):
        dictTmp[k] = "Kebi"
    #jika nama ada di nltk
    elif(diKamus(k, dictNLTK)):
        dictTmp[k] = "NLTK"

    elif(len(k) <2):
        dictTmp[k] = "panjang1"
    elif(k in ROMAWI):
        dictTmp[k] = "romawi"
    elif(k in BULAN):
        dictTmp[k] = "Nama bulan"
    else:
        dictPlace[k] = k
inputFile.close()

data1 = open("dbpedia-new/original/listNegara.txt", "r")
data2 = "dbpedia-new/original/listNegaraWrite.txt"
place = {}
dataBaca = data1.readlines()
for data in dataBaca:
    place[data] = data

writeDictToFile(place,data2)

for placeLine in place:
    dictPlace[placeLine] = placeLine

writeDictToFile(dictPlace, output)
writeDictWithValueToFile(dictTmp, outputtmp)







############################################################################
# End of file
############################################################################
