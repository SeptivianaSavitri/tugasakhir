####################################################################################
# PersonValidateCekRule.py
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


from function import writeDictToFile, writeListofStringToFile, writeListofListToFile, diKamus, buatKamus, hitungKapital, lemmaDiCorpus, writeDictWithValueToFile
from nltk.stem.wordnet import WordNetLemmatizer



##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/expanded/person.txt"
#input = "cekPerson/validation/x-expand/resultPERBedaXDikurangiExpand.txt"
folder = "dbpediaRule/validate/"
#folder = "cekPerson/validation/x-expand/"
output = folder + "AWithoutV6.txt"
outputtmp = folder + "tmpperson.txt"
outputtmpEn = folder + "tmppersonEn.txt"
nltk_data = "dbpedia-new/en"
kebi_data = "dbpedia-new/kebi.txt"
english_dict = "dbpedia-new/english_corpus.txt"
dictKebi = {}
dictNLTK = {}
dictEnglish = {}
#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
dictPerson = {}
dictTmp = {}

dictNLTK = buatKamus(dictNLTK, nltk_data)
dictEnglish = buatKamus(dictEnglish, english_dict)
dictKebi = buatKamus(dictKebi, kebi_data)
ROMAWI = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
             "XI", "XII", "XIII", "XIV",
             "XX", "XXX"]
BULAN = ["April", "Juni", "Juli"]
AGAMA = ["Buddha","Hindu","Islam","Katolik","Khonghucu","Kristen","Protestan"]
count = 1
countLema = 0

for k in flines:
    k= k.replace("\n","")
    splitK = k.split(" ")
    
    
        
        
    #Jika nama ada di kebi
    if(diKamus(k, dictKebi)):
        dictTmp[k] = "Kebi"
    #jika nama ada di nltk
    elif(diKamus(k, dictNLTK)):
        dictTmp[k] = "NLTK"
    elif(len(k) <2):
        dictTmp[k] = "Panjang 1"
    elif(k in ROMAWI):
        dictTmp[k] = "Romawi"
    #V6
    # elif(k in BULAN):
    #     dictTmp[k] = "Nama Bulan"
    #V7
    elif(k in AGAMA):
        dictTmp[k] = "Nama agama"
        print(k)
    #untuk entity yang berisi 1 kata
    elif len(splitK) == 1 and "." in k:
        dictTmp[k] = "Satu kata bertitik"
        
    elif len(splitK) == 1 and k.isnumeric():
        dictTmp[k] = "Angka"
    # elif len(k) == 2 and k[1].isupper():
    #     dictTmp[k] = k
    elif len(splitK) == 1  and hitungKapital(k) == len(k):
        dictTmp[k]="Huruf Besar Semua"   
    elif len(splitK) == 1 and lemmaDiCorpus(k,dictNLTK):
        dictTmp[k] = "Lemmatization di nltk"   
    else: 
        dictPerson[k] = k
inputFile.close()

writeDictToFile(dictPerson, output)

writeDictWithValueToFile(dictTmp, outputtmp)
#writeListofStringToFile(newListTmp, outputtmp)



############################################################################
# End of file
############################################################################
