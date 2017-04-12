####################################################################################
# Library of DBpedia Entities Expansion for Indonesian NER
#
# NERIka_Tagger.py
#
# @Author: Ika Alfina (ika.alfina@gmail.com)
# @Last update: 19 Agustus 2016
# Fasilkom Universitas Indonesia
#
# Objective: To tag a file contains formatted data in Stanford NER format
# input: 
#   - all files contains selected pragraphs --> output of Data1_ArticleAndParagraphsSelector.py
#
# output: a text file contains all selected paragraphs
# 
# Limitation of this program: 
#  - the input file should be named in certain format, starting from XXX_00 and so on
#  - you sould specify number of files to be combined
####################################################################################

#coding: utf8
from ner_ika import makeExpandedDBpediaDictionary, listToString, getArticleType, writeListToFile

##########################################################################
#    Melakukan Splitting N-Gram
##########################################################################

def nGramsIndex(aName, start):


    result = []

    pjg = len(aName)

    i = pjg

    for i in range (0, pjg): #jumlah kata
        #tmp = []
        for j in range(0, i+1): # index mulai
            tmp = []
            kk = []
            for k in range(j, j+pjg-i):
                kk.append(aName[k])

            tmp.append(kk)
            tmp.append(start+j)

            result.append(tmp)

    return result


# [[[ABC]0],[[AB]0],[[BC]1]

# [[[ABC]0], [[AB],0,[BC],1],

############################################################################
# M A I N
############################################################################


############## set the parameter ####################

# create dbpedia version: original, expanded or normalized

dbpedia = makeExpandedDBpediaDictionary()

# set the input file

folder = "data/training/"
inputfile = folder + "prep/ID_formatted1_01.txt"

# set the output file

outputfile = folder + "ready/ID_tagged1_buika.txt"


############################ BEGIN ###########################

input = open(inputfile, "r", errors='replace')

inputLines = input.readlines()

len_input = len(inputLines)
print ("Jumlah term " + str(len(inputLines)))

wordList = []

#buat list of (kata, jenis) dan inisialisi type-nya dengan "O" for Other

for i in inputLines:

    kk = []
    kk.append(i.strip())
    kk.append("O")
    wordList.append(kk)

#mulai melakukan tagging

i = 0
while i < len(wordList):

    percen = float(i)/float(len_input)
    print ("Now ... " + str(i) + " of " + str(len_input) + "          (" + str(percen) + ")")

    kata = wordList[i][0]

    if kata[0].isupper(): #jika diawali huruf kapital

        tmp = []
        tmp.append(kata)

        j = i+1
        while j < len(wordList):

            kata2 = wordList[j][0]
            if kata2[0].isupper(): #jika next-nya masih huruf kapital

                tmp.append(kata2)
                j+=1

            else:
                break

        #didapatkan kandidat named entity tersimpan di tmp

        print ("Candidate NE: ")
        print (tmp)

        if len(tmp) == 1:
            kata = tmp[0].strip()

            # if kata.isupper() and len(kata) > 2:
            #     wordList[i][1] = "Organisation"
            #
            # else:

            title = getArticleType(dbpedia, kata)

            if title is not "O":

                print ("Nama Panjang 1 : " + kata + "   " + title)


                wordList[i][1] = title


        else: # len(tmp)> 1:

            candidates = nGramsIndex(tmp, i)        #[[[A,B,C],i],[[A,B],i],[[B,C],i+1],...[[C],i+2]]

            for aCandidate in candidates:

                namasaja = aCandidate[0]  # salin entri nama kandidat yang berupa list of kata

                if len(namasaja) == 1: #proses nama terdiri dari 1 kata

                    namanya = namasaja[0] # salin namanya saja
                    type = getArticleType(dbpedia, namanya.strip())

                    if type is not "O":

                        print ("N-gram candidate panjang 1 --- ")
                        print (aCandidate[0])
                        print (type)

                        wordList[aCandidate[1]][1] = type

                        j = aCandidate[1]+1

                        break

                else: #jika kandidat terdiri dari lebih 1 kata

                    namastring = listToString(namasaja)
                    type = getArticleType(dbpedia, namastring.strip())

                    if type is not "O":

                        #copy type ke setiap kata
                        print ("N-gram candidate panjang N --- ")
                        print (aCandidate[0])
                        print (type)


                        c_len = len(aCandidate[0])
                        start = aCandidate[1]
                        end = aCandidate[1] + c_len

                        for g in range(start, end):
                            wordList[g][1] = type

                        #i=5,j=i+4,c_len=2,tmp=ABCD,

                        j = end

                        break

        i = j # akhir dari bagian {jika diawali huruf kapita
    else:
        i+= 1


#writeListData(wordList, outputfile)

writeListToFile(wordList, outputfile)

############################################################################
# End of file
############################################################################

