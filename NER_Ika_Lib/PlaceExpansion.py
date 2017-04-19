
####################################################################################
# PlaceExpansion.py
# @Author: Septiviana Savitri
# @Last update: 28 Februari 2017
# Fasilkom Universitas Indonesia
#
# Objective: To expand all the normalized data of Person in DBPedia 
# input: 
#   - File contain each type of normalized data

# output: expanded version of data :
#   - place with coma seperator "aa, bb" is seperated into "aa, bb", "aa" and "bb"

 
####################################################################################


from function import writeListofStringToFile

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/normalized/place.txt"
folder = "dbpedia-new/expanded/"
output = folder + "place.txt"
#outputtmp = folder + "tmp.txt"

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
arrPlace = []

count = 1
for k in flines: 
	k= k.replace("\n","")
	komaspasiSplit = k.split(", ")
	if len(komaspasiSplit) > 1: 	
		for i in range(0, len(komaspasiSplit)):
			arrPlace.append(komaspasiSplit[i]) 
		   
   
	else:
		arrPlace.append(k) 
	count += 1
inputFile.close()



writeListofStringToFile(arrPlace, output)



############################################################################
# End of file
############################################################################
