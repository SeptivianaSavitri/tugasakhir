####################################################################################
# Library of DBpedia Entities Expansion for Indonesian NER
#
# NormalTagger.py
#
# Tagging NER tanpa mengatasi masalah ambiguitas
####################################################################################

#coding: utf8
from function import makeExpandedDBpediaDictionary, listToString, getArticleType, writeListToFile

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

dbpedia, ambigu = makeExpandedDBpediaDictionary()

# set the input file

folder = "newdata/trainingRule/"
#inputfile = "input_tagging.txt"

inputfile = folder + "prep/formatted-goldstandard-0811.txt"

# set the output file

outputfile = folder + "ready/DB-normaltag.txt"

outputfile = "output_tagging.txt"


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
ptrAmbigu = 0
i = 0
print(len(wordList))
while i < len(wordList):

    percen = float(i)/float(len_input)
    print ("Now ... " + str(i) + " of " + str(len_input) + "          (" + str(percen) + ")")

    kata = wordList[i][0]
    kata_next=""
    if i < len(wordList) - 1:
        kata_next = wordList[i+1][0]
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

            # if kata in ambigu.keys():
            #     titleAmbigu = getArticleType(ambigu,kata)
            #     if titleAmbigu == "Person - Place":

            #         if (wordList[i-1][0] == "di") or (wordList[i-1][0] == "ke") or (wordList[i-1][0] == "dari"):
                        
            #             wordList[i][1] = "Place"
            #             title = "Place"
            #         else: title = "O"
            #     else:
            #         wordList[i][1] = "O"
            #         title = "O"

            # if (kata == "SD") or (kata == "SDN" or (kata == "SMP") or (kata == "SMPN") or (kata == "SMA") or (kata == "SMAN")):
            #     if kata_next != "" :
            #         if(kata_next.isnumeric() or kata_next.isupper()):
            #             title = "Organisation"

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

                    # if namanya in ambigu.keys():
                    #     titleAmbigu = getArticleType(ambigu,namanya)
                    #     if titleAmbigu == "Person - Place":
                    #         print("Ini adalah ambigu :" + namanya)
                    # if (type != "Place") or (type != "Person") or (type != "Organisation"):

                    #     if type == "Per-Pl":

                    #         if (wordList[i-1][0] == "di") or (wordList[i-1][0] == "ke") or (wordList[i-1][0] == "dari"):
                        
                    #             wordList[i][1] = "Place"
                    #             type = "Place"
                    #     else:
                    #         wordList[i][1] = "O"
                    #         type = "O"

                    if type is not "O":

                        print ("N-gram candidate panjang 1 --- ")
                        print (aCandidate[0])
                        print (type)

                        wordList[aCandidate[1]][1] = type

                        j = aCandidate[1]+1

                        break

                else: #jika kandidat terdiri dari lebih 1 kata
                    ptrAmbigu = i
                    namastring = listToString(namasaja)
                    type = getArticleType(dbpedia, namastring.strip())
                    # if namastring in ambigu.keys():
                    #     titleAmbigu = getArticleType(ambigu,namastring)
                    #     if titleAmbigu == "Person - Place":
                    #         print("Ini adalah ambigu di panjang N:" + namastring)
                    #         print(wordList[ptrAmbigu][0])
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

        i = j # akhir dari bagian {jika diawali huruf kapital)
    else:
        i+= 1


#writeListData(wordList, outputfile)

writeListToFile(wordList, outputfile)

############################################################################
# End of file
############################################################################

