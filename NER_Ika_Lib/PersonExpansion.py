####################################################################################
# PersonExpansion.py
# @Author: Septiviana Savitri
# @Last update: 28 Februari 2017
# Fasilkom Universitas Indonesia
#
# Objective: To expand all the normalized data of Person in DBPedia 
# input: 
#   - File contain each type of normalized data

# output: expanded version of data :
#   - name with 2 words, split into AA and BB
#   - name with n-gram variation
####################################################################################


from function import writeDictToFile, writeListofStringToFile, writeListofListToFile


##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/normalized/person.txt"
inputBin = "dbpedia-new/normalized/tmpBin.txt"
folder = "dbpedia-new/expanded/"
output = folder + "person.txt"
coba= folder + "personcb.txt"
#outputtmp = folder + "tmp.txt"

def nGram(input, n):
  input = input.split(' ')
  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output

def nameGram(kata,n):
   
    arrKata = []
    arrOutput = []
    kataTmp = ""
    for i in range(1,n+1):
        arrKata.append(nGram(kata,i))
   
    for j in range(0,n):
        arrTemp = arrKata[j]
        for k in range(0, len(arrTemp)):
            arrTemp2 = arrTemp[k]
            kataTmp = ""
            for m in range(0,len(arrTemp2)):
                
                kataTmp = kataTmp + (arrTemp2[m] + " ")
                
            if kataTmp[len(kataTmp)-1] == " ":
                kataTmp = kataTmp[:len(kataTmp)-1]
            arrOutput.append(kataTmp)
        # for j in range(0,n)
        #     for k in range(0,)
    
    return arrOutput
#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
arrPerson = []

count = 1
for k in flines:
    k= k.replace("\n","")
    spasiSplit = k.split(" ")
    binSplit = k.split(" Bin ")
    #Jika nama mengandung kata bin
    if len(binSplit) > 1: 
        for i in range(0,len(binSplit)):
            arrPerson.append(binSplit[i])
    # jika lebih dari 1 kata
    elif len(spasiSplit) >1:
        arrGram = nameGram(k, len(spasiSplit))
        for x in range(0,len(arrGram)):
            arrPerson.append(arrGram[x])
        
  
    else:
        arrPerson.append(k)
    count += 1
inputFile.close()


inputFile = open(inputBin, 'r', errors='ignore')
flines = inputFile.readlines()

for k in flines:
    k= k.replace("\n","")
    arrPerson.append(k)
    count += 1
inputFile.close()


writeListofStringToFile(arrPerson, output)
#writeListofStringToFile(newListTmp, outputtmp)



############################################################################
# End of file
############################################################################
