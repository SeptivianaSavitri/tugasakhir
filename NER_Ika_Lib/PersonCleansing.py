####################################################################################
# PersonCleansing.py
# @Author: Septiviana Savitri
# @Last update: 28 Februari 2017
# Fasilkom Universitas Indonesia
#
# Objective: To clean the original dbPedia 
# input: 
#   - File contain each type of original data

# output: clean version of data :
#   - every line with (xxx), replaced only by name
#   - every line with (grup xxx)in Person, move to Organization
 
####################################################################################


from function import writeListofStringToFile

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/original/person.txt"
inputPlace = "dbpedia-new/original/place.txt"
folder = "dbpedia-new/cleansing/"
output = folder + "person.txt"
outputtmp = folder + "tmp.txt"
outputPlace = folder + "place.txt"

def cariBukaKurung(kata, pnjg):
    idx = pnjg
    while (idx != 0):
        if kata[idx] == "(":
            return idx
        idx=idx-1

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
newListPerson = []
newListTmp = []
newListPlace = []
count = 1
for k in flines:
    arrSplit = k.split(" ")
    kurung = arrSplit[len(arrSplit) - 1]
    tutup = kurung[len(kurung)-2]
    if tutup == ")": 
        koorTutup = k.find(tutup) 
        koorBuka = cariBukaKurung(k,koorTutup)
        isiKurung = k[koorBuka+1:koorTutup]
        splitKurung = isiKurung.split(" ")
        if((splitKurung[0] == "band") or (splitKurung[0] == "grup")):
            newListTmp.append(k[:koorBuka])
        else:
            newListPerson.append(k[:koorBuka]);
        
    
    else:
        newListPerson.append(k);
    count += 1
inputFile.close()
writeListofStringToFile(newListPerson, output)
writeListofStringToFile(newListTmp, outputtmp)

inputFile = open(inputPlace, 'r', errors='ignore')
flines = inputFile.readlines()
for k in flines:
    newListPlace.append(k)
inputFile.close()
writeListofStringToFile(newListPlace, outputPlace)




############################################################################
# End of file
############################################################################
