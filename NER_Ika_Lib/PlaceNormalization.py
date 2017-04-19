####################################################################################
# PlaceNormalization.py
# @Author: Septiviana Savitri
# @Last update: 1 Maret 2017
# Fasilkom Universitas Indonesia
#
# Objective: To normalized the original dbPedia 
# input: 
#   - File contain each type of clean data

# output: normalized version of data :
#    - remove all the description in (xx)
#    - get the data from Person
####################################################################################


from function import writeListofStringToFile

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/cleansing/place.txt"
folder = "dbpedia-new/normalized/"
output = folder + "place.txt"


#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
newListPlace = []
count = 1
for k in flines:
    koorBuka = k.find("(")
    koorTutup = k.find(")")
    if koorBuka != -1: 
       
        newListPlace.append(k[:koorBuka-1]);
        
    
    else:
        newListPlace.append(k);
    count += 1
inputFile.close()

writeListofStringToFile(newListPlace, output)