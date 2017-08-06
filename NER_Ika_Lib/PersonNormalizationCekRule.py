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
#   - normalized form of name that contains "oe", make the entry that also replaced by "u"
####################################################################################


from function import writeListofStringToFile
import re
##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/cleansing/person.txt"
folder = "dbpediaRule/normalized/"
output = folder + "NA9.txt"
outputtmp = folder + "tmp.txt"
outputBin = folder + "tmpBin.txt"
outputKoma = folder + "tmpKoma.txt"

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
newListPerson = []
newListTmp = []
newListBin = []
newListKoma = []
count = 1
cek = 0
for k in flines:
  
    binSplit = re.split(" bin | Bin ",k)
    vanSplit = re.split(" van | Van ",k)
    vonSplit = re.split(" von | Von ",k)
    bintiSplit = re.split(" binti | Binti ",k)
    dariSplit = k.split(" dari ")
    daSplit = re.split(" da | Da ",k)
    doSplit = re.split(" do | Do ",k)
    dosSplit = re.split(" dos | Dos ",k)
    deSplit = re.split(" de | De ",k)
    spasiSplit = k.split(" ")
    # #NA 8 Jika nama ejaan lama
    # if("oe" in k):
    #     ejaanBaru = k.replace("oe","u")
    #     newListPerson.append(ejaanBaru)
    #     newListPerson.append(k)
        
    # #NA7 jika nama mengandung gelar dan kata sapaan
    # if spasiSplit[0]=="KH" or spasiSplit[0]=="Pak" or spasiSplit[0]=="KH." or spasiSplit[0]=="Dr.":
    #     k = k[(len(spasiSplit[0])+1):]
        
    # #NA1-MODIFIKAI Jika nama mengandung kata bin
    # if len(binSplit) > 1: 
    #     newListBin.append(k)
        
    #     for i in range(0, len(binSplit)):    
    #         newListPerson.append(binSplit[i])
            
    # #NA1-MODIFIKAI  Jika nama mengandung kata binti   
    # elif len(bintiSplit) > 1:
    #     newListBin.append(k)
        
    #     for j in range(0, len(bintiSplit)):
    #         newListPerson.append(bintiSplit[j])
            
    # #Jika nama mengandung kata dari, kata setelah dari disimpan di tmp
    # elif len(dariSplit) > 1:
    #     newListPerson.append(dariSplit[0])
    # #     newListTmp.append(dariSplit[1])
    # # NA3-MODIFIKASI
    # if len(vanSplit) > 1:
    #     newListBin.append(k)
    #     newListPerson.append(vanSplit[0])
    #     newListPerson.append(vanSplit[1])
    # elif len(vonSplit) > 1:
    #     newListBin.append(k)
    #     newListPerson.append(vonSplit[0])
    #     newListPerson.append(vonSplit[1])
    # elif len(daSplit) > 1:
    #     newListBin.append(k)
    #     newListPerson.append(daSplit[0])
    #     newListPerson.append(daSplit[1])
    # elif len(doSplit) > 1:
    #     newListBin.append(k)
    #     newListPerson.append(doSplit[0])
    #     newListPerson.append(doSplit[1])
    # elif len(dosSplit) > 1:
    #     newListBin.append(k)
    #     newListPerson.append(dosSplit[0])
    #     newListPerson.append(dosSplit[1])   
    # elif len(deSplit) > 1:
    #     newListBin.append(k)
    #     newListPerson.append(deSplit[0])
    #     newListPerson.append(deSplit[1])

    # #NA4-MODIFIKASI
    # elif spasiSplit[len(spasiSplit) - 1] == "Jr.\n":
    #     newListPerson.append(k.replace(",",""))
    #     newListPerson.append(k.replace(", Jr.",""))
    # elif spasiSplit[len(spasiSplit) - 1] == "Sr.\n":
    #     newListPerson.append(k.replace(",",""))
    #     newListPerson.append(k.replace(", Sr.",""))
    # #NA 6
    # elif k.find("-") != -1:
    #     for m in range (0, len(spasiSplit)):
    #         tmp = spasiSplit[m]
    #         stripSplit = tmp.split("-")
    #         if len(stripSplit)>1 and stripSplit[0][0].isupper() and stripSplit[1][0].isupper():         
    #             newListPerson.append(k)
    #             hapusStrip = k.replace("-"," ")
    #             newListPerson.append(hapusStrip)
    #         else:
    #             newListPerson.append(k)
    # else:
    
    newListPerson.append(k);
    count += 1
inputFile.close()


writeListofStringToFile(newListPerson, output)
writeListofStringToFile(newListTmp, outputtmp)
writeListofStringToFile(newListBin,outputBin)
inputFile = open(output, errors='ignore')
flines = inputFile.readlines()
newListPerson = []
for name in flines:
    newListPerson.append(name)
for name in flines:
    splitKoma = name.split(",")
    #NA9
    if len(splitKoma)>1:
        3+1;
        if len(splitKoma) == 2:
            newListKoma.append(name)
            newListPerson.remove(name)
            newListPerson.append(splitKoma[0])
        else:

            newListPerson.remove(name)
            for x in splitKoma:
                x = x.replace(" ","")
                x = x.replace("dan","")
                newListPerson.append(x)

inputFile.close()     
writeListofStringToFile(newListKoma,outputKoma)
writeListofStringToFile(newListPerson, output)
print(cek)

############################################################################
# End of file
############################################################################
