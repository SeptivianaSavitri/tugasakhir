####################################################################################
# OrganizationNormalization.py
# @Author: Septiviana Savitri
# @Last update: 1 Maret 2017
# Fasilkom Universitas Indonesia
#
# Objective: To normalized the original dbPedia 
# input: 
#   - File contain each type of clean data

# output: normalized version of data :
#    - remove all the description  (xx) in the middle.
####################################################################################


from function import writeListofStringToFile

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/cleansing/organization.txt"
folder = "dbpedia-new/normalized/"
output = folder + "organization.txt"

def cariBukaKurung(kata, pnjg):
    idx = pnjg
    while (idx != 0):
        if kata[idx] == "(":
            return idx
        idx=idx-1

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
newListOrg = []
count = 1
for k in flines:
    koorBuka = k.find("(")
    koorTutup = k.find(")")
    if koorBuka != -1: 
        awal = k[:koorBuka] 
        awal = awal.strip()
        newListOrg.append(awal)
        newListOrg.append(k[:koorBuka-1] + k[koorTutup+1:]);
        
    
    else:
        newListOrg.append(k);
    count += 1
inputFile.close()

writeListofStringToFile(newListOrg, output)