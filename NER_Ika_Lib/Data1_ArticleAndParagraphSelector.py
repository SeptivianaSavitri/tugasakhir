####################################################################################
# Library of DBpedia Entities Expansion for Indonesian NER
#
# Data1_ArticleAndParagraphSelector.py
# @Author: Ika Alfina (ika.alfina@gmail.com)
# @Last update: 19 Agustus 2016
# Fasilkom Universitas Indonesia
#
# Objective: To select articles and paragpahs that have good quality for NER training
#            from an extracted wipedia folder, output of WikiExtractor.py program
# input: 
#   - an extracted Wikipedia folder --> output of WikiExtractor.py
#   - original dbpedia : smaller dbpedia, as the reference to check article type
#   - expanded dbpedia : larger dbpedia, as the reference to check article type
#   
# output: text file contains all paragraphs that meet the criterias:
#         1. article is a about a Named Entity (Person,Place, ORG)
#         2. article has  > minimal number of paragraphs in each article 
#         3. selected paragraphs has > min number words
# 
####################################################################################


from ner_ika import makeOriginalDBpediaDictionary, getArticleType, writeListofStringToFile, makeExpandedDBpediaDictionary

############################################################################
# Apakah sebuah baris mengandung "title" artikel Wikipedia
############################################################################

def isTitlePart(aLine):

    result = False

    tokenList = aLine.split(" ")

   # print tokenList

    if len(tokenList) > 1:
        #print tokenList[0]
        if tokenList[0].strip() == "<doc":
            result = True


    return result

############################################################################
# Mengambil bagian judul dari sebuah article WIKI
############################################################################

def getTitle(aLine):

    result = ""
    kkk = aLine.split(" ") #list kata pada string berisi judul
    kkk_len = len(kkk) #jumlah kata

    kata1_len = len("title=\"")
    start = 3 #index pertama mengandung title

    if kkk_len == (start + 1): #judul artikel hanya terdiri dari 1 kata
        kata1 = kkk[start]
        tmp = kata1[kata1_len:]
        index = tmp.index("\"")
        result = tmp[:index]
    else:

        kata1 = kkk[start]
        result = result + kata1[kata1_len:]

        for i in range(start+1, kkk_len):
            if i != kkk_len -1:
                result = result + " " + kkk[i]
            else:
                tmp = kkk[i]
                index = tmp.index(">")
                result = result + " " + tmp[:index-1]

    return result

############################################################################
# M A I N
############################################################################

############################ SET THE PARAMETER #############################

# set the dbpedia

dbpediaAsli = makeOriginalDBpediaDictionary()
dbpediaExpanded = makeExpandedDBpediaDictionary()

# set the input folder and output file

folderinput = "extracted/AH/"
fileoutput = "newdata/training/prep/paragraphs_07.txt"

# set the minimal number of paragraphs in selected articles

minNumberofParagraphs = 5

#set the number of paragraphs that will be selected from selected articles

numberofSelectedParagraphs = 3

#set the minimal number of words in selected paragraphs
minNumberofWords = 50

############################### BEGIN ####################################

selected = []

namafileInput = ""

for i in range (0, 100):
    print("ini adalah i : " + str(i))
    if (i<10):
        namafileInput = folderinput + "wiki_0" + str(i)

    else:
        namafileInput = folderinput + "wiki_" + str(i)

    print (namafileInput)

    theFile = open(namafileInput, "r", errors='replace')
    
    lines = theFile.readlines()
    
    lines_len = len(lines)
   

    for i in range(0, lines_len):

        currentLine = lines[i]

        #pastikan ini adalah paragraf berisi title

        if isTitlePart(currentLine):

            title = getTitle(currentLine)
            type = getArticleType(dbpediaAsli, title)
            # print "Iter 1: " + type
            if type == "O":
                type = getArticleType(dbpediaExpanded, title)
                # print "Iter 2: " + type

            #pilih hanya artikel yang termasuk named entity (Person, Place, ORG)

            if type != "O":

                # salin isi article ke dalam list of paragraphs
                isi = []
               
                for j in range (i+2, lines_len):

                    tmpLines = lines[j]
                    if tmpLines is "</doc>":
                        break
                    else:
                        isi.append(tmpLines)

                #pilih hanya artikel yang punya paragraf lebih dari batas minimal tertentu(artikel berkualitas)

                if len(isi) > minNumberofParagraphs:

                    #tidak semua paragraf dari artikel dipilih akan diambil
                    #hanya akan diambil sebanyak jumlah tertentu
                    counter = 0

                    for j in range (i+2, lines_len):
                        tmp = lines[j]

                        if "</doc>" in tmp.strip(): #jika sudah ketemu akhir artikel
                            i = j
                            break

                        else:
                            if counter < numberofSelectedParagraphs: 

                                #paragraf terpilih harus cukup panjang

                                tmp_len = len(tmp.split(" ")) #jumlah kata pada paragraf

                                #jika jumlah kata dari paragraf memenuhi baru diambil
                                if tmp_len >= minNumberofWords:  
                                    selected.append(tmp)
                                    counter +=1

                            j +=1

	
print ("Jumlah paragraf terpilih = " + str(len(selected)))

writeListofStringToFile(selected, fileoutput)

############################################################################
# End of file
############################################################################
