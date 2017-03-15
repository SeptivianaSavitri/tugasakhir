####################################################################################
# Library of DBpedia Entities Expansion for Indonesian NER
#
# Data2_FileCombiner.py
#
# @Author: Ika Alfina (ika.alfina@gmail.com)
# @Last update: 19 Agustus 2016
# Fasilkom Universitas Indonesia
#
# Objective: To combine all of file contains selected paragraphs
# input: 
#   - all files contains selected pragraphs --> output of Data1_ArticleAndParagraphsSelector.py
#
# output: a text file contains all selected paragraphs
# 
# Limitation of this program: 
#  - the input file should be named in certain format, starting from XXX_00 and so on
#  - you sould specify number of files to be combined
####################################################################################


from ner_ika import writeListofStringToFile, listToString, writeListofListToFile


##########################################################################
# M A I N
##########################################################################

# set input and output

folder = "newdata/training/prep/"
input = folder + "paragraphs_"
output = folder + "allParagraphs.txt"

# set the number of files tobe combined

numberofFiles = 7

###################### BEGIN #################################

result = []

for i in range(0, numberofFiles):

    if (i < 10):
        namafileInput = input + "0" + str(i) + ".txt"

    else:
        namafileInput = input + str(i) + ".txt"

    mulai = len (result)

    f = open(namafileInput, "r", errors='replace')
    flines = f.readlines()

    for k in flines:
        result.append(k)

    akhir = len(result)
    
    jumlah = akhir - mulai
    print ("Total paragraf di " + namafileInput + " = " + str(jumlah))


print ("Total paragraf = " + str(len(result)))


writeListofStringToFile(result, output )


############################################################################
# End of file
############################################################################

