####################################################################################
# Library of DBpedia Entities Expansion for Indonesian NER
#
# Data4_SentencesFilter.py
# @Author: Ika Alfina (ika.alfina@gmail.com)
# @Last update: 19 Agustus 2016
# Fasilkom Universitas Indonesia
#
# Objective: To filter the sentences so that meets certain criterias 
# input: 
#   - a file contains all sentences --> output of Data3_SentencerNLTK.py

# output: a text file contains all selected sentences that meet certain criterias:
#   - sentence has words > minimal number of words in a sentence
#   - sentence has uppercase> minimal number of uppercase in a sentence
 
####################################################################################


from ner_ika import writeList

##########################################################################
# M A I N
##########################################################################

#set the input and output file
folder = "newdata/training/prep/"
input = folder + "allSentences.txt"
output = folder + "all_good_sentences1.txt"

#set the minimal number of words in a sentence
minNumberofWords = 15

#set the minimal number of uppercase in a sentence
minNumberofUppercases = 5

#########################  begin ################################

inputFile = open(input, "r")
flines = inputFile.readlines()

print ("------------------------------------------")
print ("Jumlah kalimat yang akan diproses= " + str(len(flines)))


total = 0

for k in flines:
    ll = k.split(" ")
    total += len(ll)

rata2 = float(total)/len(flines)
print ("Jumlah kata rata-rata pada semua kalimat = " + str(rata2))

newList = []

for k in flines:
    ll = k.split(" ")
    if len(ll) >= minNumberofWords: 
        upper = 0
        for k1 in k:
            if k1.istitle():
                upper+=1

        if upper >= minNumberofUppercases: 
            kataSatu = ll[0]
            kataAkhir = ll[-1]
            if kataSatu.istitle() and kataAkhir.strip().endswith("."): #kalimat harus diawali huruf kapital
                newList.append(k)

                list_len = len(newList)


jum_sentence = len(newList)

print ("Total jumlah kalimat hasil seleksi = " + str(jum_sentence))

print ("------------------------------------------")

writeList(newList, output)

############################################################################
# End of file
############################################################################
