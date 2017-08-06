####################################################################################
# NER Library for DBpedia Entities Expansion
# @Author: Septiviana Savitri
# @Last update: 19 April 2017
# Fasilkom Universitas Indonesia
####################################################################################

from nltk.stem.wordnet import WordNetLemmatizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re


ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
             "XI", "XII", "XIII", "XIV",
             "XX", "XXX"]


SPECIAL_CHARS = [",", "'"]
factory = StemmerFactory()
stemmer = factory.create_stemmer()


####################################################################################
# Mencari bentuk n gram
####################################################################################
def nGram(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output
####################################################################################
# Mencari bentuk n gram
####################################################################################
def nGramKoma(input, n):
  input = input.split(',')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output

####################################################################################
# Membuat kombinasi n-gram koma untuk n buah kata
####################################################################################
def nameGramKoma(kata,n):
   
    arrKata = []
    arrOutput = []
    kataTmp = ""
    for i in range(1,n+1):
        arrKata.append(nGramKoma(kata,i))
   
    for j in range(0,n):
        arrTemp = arrKata[j]
        for k in range(0, len(arrTemp)):
            arrTemp2 = arrTemp[k]
            kataTmp = ""
            for m in range(0,len(arrTemp2)):
                
                kataTmp = kataTmp + (arrTemp2[m] + " ")
                kataTmp = kataTmp.strip()
                #print("aku kataTmp ke "+str(m)+"  "+ kataTmp)
                
           
            arrOutput.append(kataTmp)
    return arrOutput
#print(nameGramKoma("Aku Depok, Cimanggis, Mekarsari",3))

####################################################################################
# Membuat kombinasi n-gram untuk n buah kata
####################################################################################
def nameGram(kata,n):
   
    arrKata = []
    arrOutput = []
    kataTmp = ""
    for i in range(1,n+1):
        arrKata.append(nGram(kata,i))
   
    for j in range(0,n):
        arrTemp = arrKata[j]
        for k in range(0, len(arrTemp)):
            arrTemp2 = arrTemp[k]
            kataTmp = ""
            for m in range(0,len(arrTemp2)):
                
                kataTmp = kataTmp + (arrTemp2[m] + " ")
                
            if kataTmp[len(kataTmp)-1] == " ":
                kataTmp = kataTmp[:len(kataTmp)-1]
            arrOutput.append(kataTmp)
        # for j in range(0,n)
        #     for k in range(0,)
    
    return arrOutput
#print(nameGram("Aku ceker ayam kampung omaygat",5))
####################################################################################
# Mencari jumlah huruf Kapital dalam suatu kata
####################################################################################
def hitungKapital(kata):
    len_kata = len(kata)
    counter = 0
    i = 0
    while(i < len_kata):
        if kata[i].isupper():
            counter = counter +1

        i = i+1   
    return counter
####################################################################################
# Mencari suatu KATA DASAR dalam dictionary untuk 1 kata [INDONESIA]
####################################################################################
def stemDiCorpus(kata, aDict):
    
    kataLow = kata.lower()
    kataStem = stemmer.stem(kataLow)
    if diKamus(kataStem, aDict):
        return True
    else:
        return False    
####################################################################################
# Mencari suatu lemma dalam dictionary untuk 1 kata
####################################################################################
def lemmaDiCorpus(kata, aDict):
    lm = WordNetLemmatizer()
    kataLow = kata.lower()
    kataVerb = lm.lemmatize(kataLow,'v')
    kataNoun = lm.lemmatize(kataLow,'n')
    kataLema = lm.lemmatize(kataLow)
    if diKamus(kataVerb, aDict) or diKamus(kataNoun, aDict) or diKamus(kataLema, aDict):
        return True
    else:
        return False

####################################################################################
# Mencari suatu lemma dalam dictionary untuk -n kata
####################################################################################
def lemmaLongDiCorpus(kataLong, aDict):
    lm = WordNetLemmatizer()
    k = kataLong.replace("\n","")
    arrSplit = k.split(" ")
    countLemma = 0;
    for word in arrSplit:
        word = word.lower()
        if lemmaDiCorpus(word, aDict):
            countLemma = countLemma + 1 
    
    if (countLemma == len(arrSplit)):
        return True
    else:
        return False


####################################################################################
# Mencari suatu kata spesial pada sebuah entitas
####################################################################################
def findWord(kataLong, kataDicari):
    k = kataLong.replace("\n","")
    arrSplit = k.split(" ")
    countLemma = 0;
    for word in arrSplit:
        word = word.lower()
        word = re.sub(r"[^A-Za-z]+", '', word)
        if word == kataDicari:
            return True
    return False


####################################################################################
# Mencari indeks tanda buka kurung
####################################################################################

def cariBukaKurung(kata, pnjg):
    idx = pnjg
    while (idx != 0):
        if kata[idx] == "(":
            return idx
        idx=idx-1

####################################################################################
# Aturan untuk melihat kamus
####################################################################################


def diKamus(kata, dict):
    if kata in dict.keys() or kata.lower() in dict.keys():
        return True
    
    return False

def buatKamus(dict, fileKata):
    dataFile = open(fileKata, 'r', errors='ignore')
    dict = {}
    for line in dataFile:
        line = line.replace("\n","")
        dict[line] = line
    dataFile.close()
    return dict

####################################################################################
# Membuat Kamus DBpedia Expanded
####################################################################################
def makeExpandedDBpediaDictionary():

    aDict = {}

    person = open("dbpedia-new/validate/person.txt", "r")
    place = open("dbpediaRule/validate/G2.txt", "r")
    org = open("dbpedia-new/validate/organization.txt", "r", encoding = "Latin1")

    personLines = person.readlines()
    placeLines = place.readlines()
    orgLines = org.readlines()

    ambiguNames = {}
    counter = 0
    for name in personLines:
        key = name.strip()
        aDict[key] = "Person"


    for name in placeLines:
        key = name.strip()
        counter = counter+1
        value = "Place"
       
        if key in aDict:

            if aDict[key] == value:
                continue

            ambiguNames[key] = "Person - Place"

            value = "O"

        aDict[key] = value

    for name in orgLines:
        key = name.strip()

        value = "Organisation"

        if key in aDict:

            if aDict[key] == value:
                continue

            if aDict[key] == "O": #menandakan entity yang terdapat di Person, Place dan ORG             
                ambiguNames.pop(key)
                value = "Place"

            else:
                if aDict[key] == "Person":
                    ambiguNames[key] = "Person - ORG"
                    value = "O"
                else:
                    if(key == "Indonesia"):
                        value = "Place"
                    else:
                        ambiguNames[key] = "Place - ORG"
                        value = "O"
                    


        aDict[key] = value
    # for name, type in ambiguNames.iteritems():
    #     print "%s is %s" % (name, type)
    #
    # print "\nJumlah kata ambigu = " + str(len(ambiguNames))
    thefile = open("ambigu.txt", "w", errors='replace')
    counter = 0
    for k, v in ambiguNames.items():
        thefile.write(k + "   ")
        thefile.write(v)
        thefile.write("\n")
        counter = counter + 1

    thefile.write("Terdapat "+str(counter)+" kata ambigu")
    thefile.close()
    return aDict , ambiguNames

x = {}
y = {}
x,y = makeExpandedDBpediaDictionary()
####################################################################################
# Mebuat Kamus DBpedia Asli
####################################################################################

def makeOriginalDBpediaDictionary():

    aDict = {}


    person = open("dbpedia-new/original/person.txt", "r")
    place = open("dbpedia-new/original/place.txt", "r")
    org = open("dbpedia-new/original/organisasi.txt", "r")

    personLines = person.readlines()
    placeLines = place.readlines()
    orgLines = org.readlines()


    for name in personLines:

        namelist = name.split("_")
        namekey = listToString(namelist)
        aDict[namekey] = "Person"

    for name in placeLines:

        value = "Place"

        namelist = name.split("_")
        namekey = listToString(namelist)


        if namekey in aDict:

            if aDict[namekey] == value:
                continue

            value = "O"

        aDict[namekey] = value

    for name in orgLines:
        value = "Organisation"

        namelist = name.split("_")
        namekey = listToString(namelist)

        if namekey in aDict:

            if aDict[namekey] == value:
                continue

            value = "O"

        aDict[namekey] = value

    return aDict

####################################################################################
# Membuat Kamus KEBI
####################################################################################
def makeKEBIDictionary():

    kebi = {}

    input = open("dbpedia-new/kebi.txt")
    inputlines = input.readlines()

    for lemma in inputlines:
        kebi[lemma] = 1

    return kebi

####################################################################################
# Cek apakah sebuah kata ada di Kamus KEBI
####################################################################################


def isInKBBI(aWord, kebi):

    result = False

    if aWord.strip() in kebi or aWord.strip().lower() in kebi:
        result = True

    return result

####################################################################################
# Cek apakah sebuah kata mengandung digit
####################################################################################

def isDigitExist(aWord):

    result = False

    angka = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for a in angka:
        if a in aWord:
            result = True
            break

    return result

####################################################################################
# Cek apakah sebuah kata mengandung invalid char
####################################################################################

def isInvalidCharExist(aWord):

    INVALID_CHARS = ["@", "!", "%", "$", "&", "*", "?", "^"]

    result = False

    for kk in INVALID_CHARS:
        if kk in aWord:
            result = True;
            break;

    return result


####################################################################################
# Cek apakah sebuah kata mengandung special char
####################################################################################

def isSpecCharExist(aWord):
    SPECIAL_CHARS = ["-", "'", "."]

    result = False
    for kk in SPECIAL_CHARS:
        if kk in aWord:
            result = True;
            break;

    return result


##########################################################################
#    Cek apakah nama mengandung koma
##########################################################################

def isAdaKoma(aList):

    result = False
    for i in aList:
        if "," in i:
            result = True
            break

    return result

##########################################################################
#    Cek apakah nama mengandung koma
##########################################################################

def isAdaKomaForString(aString):

    result = False

    if "," in aString:
        result = True


    return result

####################################################################################
# Mengubah List ke String
####################################################################################

def listToString(aList):

    result = ""

    for i in aList:
        if i.isdigit():

            result = result + str(i) + " "

        else:

            result = result + i + " "


    return result.strip()

####################################################################################
# Get article type: return Person, Place, Organisation atau O
####################################################################################

def getArticleType(dbpedia, aName):

    result = "O"

    if aName in dbpedia:
        result = dbpedia[aName]

    return result

##########################################################################
#fungsi membuat list unik tulisan dalam tanda kurung
##########################################################################

def getAllParenthesis(aNameList):
    resultList = []

    for line in aNameList:
        words = line.split("_")

        dd = getParenthesis(words)
        if len(dd) > 0:
            if dd not in resultList:
                resultList.append(dd)

    return resultList

##########################################################################
#fungsi untuk mengekstrak paranthesis dan isinya dari sebuah nama dalaam list
##########################################################################

def getParenthesis(aList): #nama dalam bentuk list

    result = []

    for item in aList:

        if len(item)>=1: #"memastikan item ada isinya"

            if item[0][0] == "(":
                if ")" in item:
                    result.append(item.strip())

                else:
                    cur_index = aList.index(item)

                    for jj in aList[cur_index:]:
                        result.append(jj.strip())

    return result #frase parantesis dalam bentuk list [ (penyanyi, rock)]

##########################################################################
#fungsi untuk mengekstrak paranthesis dan isinya dari sebuah nama dalaam list
##########################################################################

def getDescFromParenthesis(aParenthesis): #list berisi par dan deskripsinya

    newString = listToString(aParenthesis)

    return newString[1:-1]


##########################################################################
#    Membuang phrase dalam pharenthesis dari suatu kalimat
##########################################################################

def removeParenthesis(aList):

    newName = []

    for item in aList:
        if "(" not in item:
            newName.append(item)
        else:
            break

    return newName


##########################################################################
# tulis ke file
##########################################################################

def writeListToFile(aList, filename):

    thefile = open(filename, "w")

    for k in aList:
        thefile.write(listToString(k))
        thefile.write("\n")

    thefile.close()

    return


##########################################################################

def writeList(kebiList, filename):

    thefile = open(filename, "w", errors='replace')

    for k in kebiList:
        thefile.write(k)
        #thefile.write("\n")

    thefile.close()

    return


####################################################################################
# Tulis list ke file
# List berisi list of string: [ [A, B, C], ..., [D, E] ]
####################################################################################

def writeListofListToFile(aList, filename):

    thefile = open(filename, "w")

    for k in aList:
        thefile.write(listToString(k).strip())
        thefile.write("\n")

    thefile.close()

    return
####################################################################################
# Tulis dict ke file
# Dict tersebut berisi {"key":"value"}
####################################################################################

def writeDictToFile(aDict, filename):

    thefile = open(filename, "w")

    for key, value in aDict.items() :
        if key != "":
            thefile.write(key.strip())
            thefile.write("\n")

    thefile.close()

    return

####################################################################################
# Tulis dict ke file beserta valuenya
# Dict tersebut berisi {"key":"value"}
####################################################################################

def writeDictWithValueToFile(aDict, filename):

    thefile = open(filename, "w")

    for key, value in aDict.items() :
        if key != "":
            thefile.write(key.strip() + "\t" + value.strip())
            thefile.write("\n")

    thefile.close()

    return


####################################################################################
# Tulis list ke file
# List berisi string
####################################################################################

def writeListofStringToFile(aList, filename):

    thefile = open(filename, "w", errors='replace')

    for k in aList:
        thefile.write(k.strip())
        thefile.write("\n")

    thefile.close()

    return

##########################################################################
#    menggabungkan list 2 ke list 1
##########################################################################

def combineList (list1, list2):

    for i in list2:
        if i not in list1:
            list1.append(i)

    return;

##########################################################################
#    Buang new line
##########################################################################
def removeNewLineFromList(words):

    nameString = listToString(words)

    return nameString.strip()


##########################################################################
#    Buang new line
##########################################################################
def removeNewLine(aString):

    words = aString.split(" ")
    newName = []

    for kk in words:
        if words.index(kk) == (len(words) - 1):
            newName.append(kk.strip())
        else:
            newName.append(kk)

    return newName

##########################################################################
#    Membuat nama baru dengan buang koma dan di belakangnya
##########################################################################

def removeCommaAndAfter(oldName):

    result = []

    for item in oldName:
        if (",") not in item:
            result.append(item)
        else:
            result.append(item[:-1])
            break

    return result

