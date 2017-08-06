
####################################################################################
# PlaceExpansionCekRule.py
# @Author: Septiviana Savitri
# @Last update: 28 Februari 2017
# Fasilkom Universitas Indonesia
# FOR TESTING ONLY
# Objective: To expand all the normalized data of Person in DBPedia 
# input: 
#   - File contain each type of normalized data

# output: expanded version of data :
#   - place with coma seperator "aa, bb" is seperated into "aa, bb", "aa" and "bb"

 
####################################################################################


from function import writeListofStringToFile, writeDictToFile, nameGramKoma

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/original/place.txt"
folder = "dbpediaRule/expanded/"
output = folder + "placeEB1.txt"
#outputtmp = folder + "tmp.txt"

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
arrPlace = []
cek = 0
count = 1
arrGram = []

for k in flines: 
	k= k.replace("\n","")
	k = k.replace("  "," ")
	komaspasiSplit = k.split(",")
	if len(komaspasiSplit) > 1: 
		#cek = cek+1
		kNormal = k.replace(",","")
		kNormal = kNormal.replace("  "," ")
		arrPlace.append(kNormal)
		kSpasi = k.replace(",","")
		spasiSplit = kSpasi.split(" ")
		arrGram = nameGramKoma(k, len(komaspasiSplit))
		for x in range(0,len(arrGram)):
			masukGram = arrGram[x]
			masukGram = masukGram.replace("  "," ")
			arrPlace.append(arrGram[x])
			cek = cek+1
			#arrPlace.append(komaspasiSplit[i]) 
		   
   
	else:
		#cek = cek+1
		arrPlace.append(k) 
	count += 1
inputFile.close()
writeListofStringToFile(arrPlace, output)



print(cek)
############################################################################
# End of file
############################################################################
