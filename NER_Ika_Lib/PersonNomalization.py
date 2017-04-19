####################################################################################
# PersonNormalization.py
# @Author: Septiviana Savitri
# @Last update: 28 Februari 2017
# Fasilkom Universitas Indonesia
#
# Objective: To normalized the original dbPedia 
# input: 
#   - File contain each type of clean data

# output: normalized version of data :
#   - seperatE AA bin BB into AA and BB
 
####################################################################################


from function import writeListofStringToFile

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/cleansing/person.txt"
folder = "dbpedia-new/normalized/"
output = folder + "person.txt"
outputtmp = folder + "tmp.txt"

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
newListPerson = []
newListTmp = []
count = 1
for k in flines:
  
    binSplit = k.split(" bin ")
    bintiSplit = k.split(" binti ")
    dariSplit = k.split(" dari ")
    daSplit = k.split(" da ")
    doSplit = k.split(" do ")
    dosSplit = k.split(" dos ")
    deSplit = k.split(" de ")
    jrSplit = k.split(" ")
    #Jika nama mengandung kata bin
    if len(binSplit) > 1: 
        for i in range(0, len(binSplit)):
         
            newListPerson.append(binSplit[i])
    #Jika nama mengandung kata binti   
    elif len(bintiSplit) > 1:
        for j in range(0, len(bintiSplit)):
            newListPerson.append(bintiSplit[j])
    #Jika nama mengandung kata dari, kata setelah dari disimpan di tmp
    elif len(dariSplit) > 1:
        newListPerson.append(dariSplit[0])
        newListTmp.append(dariSplit[1])
    elif len(daSplit) > 1:
        newListPerson.append(k)
        newListPerson.append(daSplit[0])
        newListPerson.append(daSplit[1])
    elif len(doSplit) > 1:
        newListPerson.append(k)
        newListPerson.append(doSplit[0])
        newListPerson.append(doSplit[1])
    elif len(dosSplit) > 1:
        newListPerson.append(k)
        newListPerson.append(dosSplit[0])
        newListPerson.append(dosSplit[1])   
    elif len(deSplit) > 1:
        newListPerson.append(k)
        newListPerson.append(deSplit[0])
        newListPerson.append(deSplit[1])
    elif jrSplit[len(jrSplit) - 1] == "Jr.\n":
        newListPerson.append(k.replace(",",""))
        newListPerson.append(k.replace(", Jr.",""))
    elif jrSplit[len(jrSplit) - 1] == "Sr.\n":
        newListPerson.append(k.replace(",",""))
        newListPerson.append(k.replace(", Sr.",""))

    else:
        newListPerson.append(k);
    count += 1
inputFile.close()

writeListofStringToFile(newListPerson, output)
writeListofStringToFile(newListTmp, outputtmp)



############################################################################
# End of file
############################################################################
