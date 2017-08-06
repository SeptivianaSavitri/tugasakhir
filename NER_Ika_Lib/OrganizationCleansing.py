####################################################################################
# OrganizationCleansing.py
# @Author: Septiviana Savitri
# @Last update: 28 Februari 2017
# Fasilkom Universitas Indonesia
#
# Objective: To clean the original dbPedia 
# input: 
#   - File contain each type of original data

# output: clean version of data :
#    - additional data from dataset Person
#    - data cleaning from word contains (xx) at the end of entity
####################################################################################


from function import writeListofStringToFile

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpediaRule/original/organization.txt"
folder = "dbpediaRule/cleansing/"
output = folder + "organizationPC1.txt"
inputtmp = folder + "tmp.txt"

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
cek = 0
for k in flines:
    arrSplit = k.split(" ")
    kurung = arrSplit[len(arrSplit) - 1]
    tutup = kurung[len(kurung)-2]
    if tutup == ")": 
        koorTutup = k.find(tutup) 
        koorBuka = cariBukaKurung(k,koorTutup)
        isiKurung = k[koorBuka+1:koorTutup]
        splitKurung = isiKurung.split(" ")
        
        newListOrg.append(k[:koorBuka]);
    
    else:
        newListOrg.append(k);
    count += 1
inputFile.close()

#Memasukkan data dari tmp
inputFile = open(inputtmp, 'r', errors='ignore')
flines = inputFile.readlines()
#PC-1
for k in flines:
    newListOrg.append(k)
    cek = cek+1
    
inputFile.close()
print(cek)
writeListofStringToFile(newListOrg, output)




############################################################################
# End of file
############################################################################
