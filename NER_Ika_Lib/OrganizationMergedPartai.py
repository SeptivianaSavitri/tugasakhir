
####################################################################################
# OrganizationMergedPartai.py
# @Author: Septiviana Savitri
# @Last update: 8 Maret 2017
# Fasilkom Universitas Indonesia
#
# Objective: To expand all the normalized data of Organization in DBPedia 
# input: 
#   - File contain each type of normalized data

# output: expanded version of data :
#   - organization with coma seperator "aa, bb" is seperated into "aa, bb" and "aa"  

 
####################################################################################


from function import writeListofStringToFile

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/original/listPartai.txt"
folder = "dbpedia-new/expanded/"
output = folder + "listPartai.txt"
#outputtmp = folder + "tmp.txt"

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
listPartai = []

count = 1
for k in flines: 
	k= k.replace("\n","")
	if k[len(k)-1] == "*":
		k = k[:len(k)-1]
	

	spasiSplit = k.split(" ")
	bukaKurung = k.find("(")
	tutupKurung = k.find(")")
	#memisahkan Partai XX YY (xy) menjadi "Partai XX YY" dan "xy"
	if(bukaKurung != -1):	
		listPartai.append(k[:(bukaKurung-1)])
		listPartai.append(k[(bukaKurung)+1:tutupKurung])
	else:
		listPartai.append(k)
		
	if(spasiSplit[0] == "Partai"):
		if(bukaKurung != -1):
			listPartai.append(k[7:bukaKurung])
		else:
			listPartai.append(k[7:])
		
	count += 1
	
inputFile.close()

	



writeListofStringToFile(listPartai, output)



############################################################################
# End of file
############################################################################
