
####################################################################################
# OrganizationExpansion.py
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
import re
##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/normalized/organization.txt"
folder = "dbpediaRule/expanded/"
output = folder + "EC3.txt"
outputtmpkoma = folder + "orgtmpkoma.txt"

outputtmpdi = folder + "orgtmpdi.txt"

outputtmppartai = folder + "orgtmppartai.txt"

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
listOrganization = []
listOrganizationKoma = []
listOrganizationDi = []
listOrganizationPartai = []
cek = 0
count = 1
for k in flines: 
	k= k.replace("\n","")
	komaspasiSplit = k.split(", ")
	diSplit = k.split(" di ")
	

	if len(komaspasiSplit) > 1: 
		cek = cek+1
		listOrganization.append(k)
		kBaru = k.replace(",","")
		listOrganization.append(kBaru)
		listOrganizationKoma.append(kBaru)
		listOrganization.append(komaspasiSplit[0])
		listOrganizationKoma.append(komaspasiSplit[0])
	elif len(diSplit) > 1: 
		cek = cek+1
		listOrganization.append(k)
		kBaru = k.replace(" di "," ")
		listOrganization.append(kBaru)
		listOrganizationDi.append(kBaru)
		listOrganization.append(diSplit[0])
		listOrganizationDi.append(diSplit[0])
		   
   
	else:
		listOrganization.append(k)

	spasiSplit = k.split(" ")
	#EC3
	if(spasiSplit[0] == "Partai"):
		listOrganization.append(k[7:])
		listOrganizationPartai.append(k[7:])
	count += 1
inputFile.close()


print(cek)
writeListofStringToFile(listOrganization, output)
writeListofStringToFile(listOrganizationKoma, outputtmpkoma)
writeListofStringToFile(listOrganizationDi,outputtmpdi)
writeListofStringToFile(listOrganizationPartai, outputtmppartai)



############################################################################
# End of file
############################################################################
