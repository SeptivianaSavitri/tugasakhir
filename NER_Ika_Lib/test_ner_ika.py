####################################################################################
# NER Library for DBpedia Entities Expansion
# @Author: Ika Alfina
# @Last update: 19 Agustus 2016
# Fasilkom Universitas Indonesia
####################################################################################

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
             "XI", "XII", "XIII", "XIV",
             "XX", "XXX"]


SPECIAL_CHARS = [",", "'"]

####################################################################################
# Membuat Kamus DBpedia Expanded
####################################################################################

def makeExpandedDBpediaDictionary():

    aDict = {}

    person = open("dbpedia-new/validate/person.txt", "r")
    place = open("dbpedia-new/validate/place.txt", "r")
    org = open("dbpedia-new/validate/organization.txt", "r")

    personLines = person.readlines()
    placeLines = place.readlines()
    orgLines = org.readlines()

    ambiguNames = {}

    for name in personLines:
        key = name.strip()
        aDict[key] = "Person"


    for name in placeLines:
        key = name.strip()

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

            if aDict[key] == "O":
                ambiguNames[key] = "Person - Place - ORG"

            else:
                if aDict[key] == "Person":
                    ambiguNames[key] = "Person - ORG"
                else:
                    ambiguNames[key] = "Place - ORG"

            value = "O"


        aDict[key] = value

    # for name, type in ambiguNames.iteritems():
    #     print "%s is %s" % (name, type)
    #
    # print "\nJumlah kata ambigu = " + str(len(ambiguNames))

    return aDict


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
# Dict tersebut berisi {"keu":"value"}
####################################################################################

def writeDictToFile(aDict, filename):

    thefile = open(filename, "w")

    for key, value in dictPlace.items() :
        if key != "":
            thefile.write(key.strip())
            thefile.write("\n")

    thefile.close()

    return
####################################################################################
# Tulis dict ke file
# List berisi list of string: [ [A, B, C], ..., [D, E] ]
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

