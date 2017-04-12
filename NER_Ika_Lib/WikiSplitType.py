####################################################################################
# WikiSplitType.py
# @Author: Septiviana Savitri
# @Last update: 8 Februari 2017
# Fasilkom Universitas Indonesia
#
# Objective: To filter the sentences so that meets certain criterias 
# input: 
#   - a file contains all sentences --> output of Data3_SentencerNLTK.py

# output: a text file contains all selected sentences that meet certain criterias:
#   - sentence has words > minimal number of words in a sentence
#   - sentence has uppercase> minimal number of uppercase in a sentence
 
####################################################################################


import codecs
from ner_ika import writeListofStringToFile

##########################################################################
# M A I N
##########################################################################

#set the input and output file

folder = "dbpedia-new/original/"
#input = "dbpedia-new/cleansing/nyoba.txt"
input = "input.txt"
output1 = folder + "person.txt"
output2 = folder + "place.txt"
output3 = folder + "organization.txt"



#########################  begin ################################

inputFile = codecs.open(input, 'r', errors='ignore')
flines = inputFile.readlines()
newListPerson = []
newListPlace = []
newListOrg = []
count = 1
for k in flines:
    if k[0] == "<":  
        arrLine = k.split(" ")   
        arrType = arrLine[2].split("/")
        arrValue = arrLine[0].split("/")
        dataType = arrType[len(arrType) - 1]
        dataValue = arrValue[len(arrValue) - 1]
        if (dataType[:-1] == "Person")  and (arrType[2]=="dbpedia.org"):
            x = codecs.decode(dataValue[:-1], 'unicode_escape')
            #x = dataValue[:-1]
             
            # if count==90:
            #     print(x.replace('_',' '))
            newListPerson.append(x.replace('_',' '))

        elif (dataType[:-1] == "Place") and (arrType[2]=="dbpedia.org"):
            x = codecs.decode(dataValue[:-1], 'unicode_escape')
            newListPlace.append(x.replace('_',' '))
        elif (dataType[:-1] == "Organisation") and (arrType[2]=="dbpedia.org") :
            x = codecs.decode(dataValue[:-1], 'unicode_escape')
            newListOrg.append(x.replace('_',' '))
    count += 1
inputFile.close()
writeListofStringToFile(newListPerson, output1)

writeListofStringToFile(newListPlace, output2)

writeListofStringToFile(newListOrg, output3)

############################################################################
# End of file
############################################################################
