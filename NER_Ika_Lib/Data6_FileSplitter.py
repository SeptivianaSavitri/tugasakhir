####################################################################################
# Library of DBpedia Entities Expansion for Indonesian NER
#
# Data6_FileSplitter.py
# @Author: Ika Alfina (ika.alfina@gmail.com)
# @Last update: 19 Agustus 2016
# Fasilkom Universitas Indonesia
#
# Objective: To split a large file into several files based on max number of sentence defined
# input: 
#   - a file that contanins all sentences in Indonesian language --> output of Data5_IndoDetector.java
#   - max number of sentences in a file
#
# output: list of files, names ending with number, example: XXX_01.txt
# 
####################################################################################


from ner_ika import writeList


##########################################################################
# M A I N
##########################################################################

# set the input and output files

folder = "newdata/training/prep/"
input = folder + "all_ID_sentences.txt"
output = folder + "ID_sentences20k_"

#set the maximum number of sentences in a file

maxNumberofSentences = 20000

################################ BEGIN ###################################

inputFile = open(input, "r", errors='replace')

newList = inputFile.readlines()

jum_sentence = len(newList)

print ("-----------------------------------------")
print ("Jumlah kalimat yang akan diproses= " + str(jum_sentence))


# count number of files that will be created

if (jum_sentence % maxNumberofSentences == 0):

    jumlahFile = jum_sentence/maxNumberofSentences

else:

    jumlahFile = jum_sentence/maxNumberofSentences +1

print ("Jumlah File = " + str(jumlahFile))


# copy sentences to files

tmpList = []
fileCounter = 0

for i in range(0, jum_sentence):

    tmpList.append(newList[i])

    len_tmp = len(tmpList)

    if i == jum_sentence -1:
        namafile = output + str(fileCounter) + ".txt"

        print (namafileInput + " --> Jumlah kalimat = " + str(len(tmpList)))

        writeList(tmpList, namafile)

    elif len_tmp == maxNumberofSentences:

        if (fileCounter < 10):
            namafileInput = output + "0" + str(fileCounter) + ".txt"

        else:
            namafileInput = output + str(fileCounter) + ".txt"

        print (namafileInput + " --> Jumlah kalimat = " + str(len(tmpList)))

        writeList(tmpList, namafileInput)

        #siapkan untuk iterasi selanjutnya
        tmpList = []
        fileCounter += 1

print ("-----------------------------------------")

############################################################################
# End of file
############################################################################

