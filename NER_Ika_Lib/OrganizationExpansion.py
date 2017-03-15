
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


from ner_ika import writeDictToFile

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/normalized/organization.txt"
folder = "dbpedia-new/expanded/"
output = folder + "organization.txt"
#outputtmp = folder + "tmp.txt"

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
dictOrganization = {}

count = 1
for k in flines: 
	k= k.replace("\n","")
	komaspasiSplit = k.split(", ")
	if len(komaspasiSplit) > 1: 
		dictOrganization[k] = k
		for i in range(0, len(komaspasiSplit)):
			dictOrganization[komaspasiSplit[0]] = komaspasiSplit[0]
		   
   
	else:
		dictOrganization[k] = k
	count += 1
inputFile.close()



writeDictToFile(dictOrganization, output)



############################################################################
# End of file
############################################################################
