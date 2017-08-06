
####################################################################################
# CompareDBPediaORG.py
# @Author: Septiviana Savitri
# @Last update: 26 April 2017
# Fasilkom Universitas Indonesia
#
# Objective: To compare the differences between x and y (DBPedia-ORG)
# input: 
#   - each file of DBPedia x and DBPedia y

# output: expanded version of data :
#   - three different version of data (same entity, different entity that only in X, different entity that only in y) 
####################################################################################


from function import writeListofStringToFile,writeDictToFile


##########################################################################
# M A I N
##########################################################################




#set the input and output file
inputX = "dbpedia-v1/expanded/Place_expanded.txt"
inputY = "dbpediaRule/validate/BnoG.txt"



#########################  begin PER ################################

dataX = open(inputX, "r")
dataY = open(inputY, "r")
folder = "cekPerson/validation/withBuIka/"
output =  folder + "resultPERSama.txt"
outputBedaY = folder+  "resultPERBedaY.txt"
outputBedaX =  folder+ "resultPERBedaX.txt"
dictOutputSama = {}
dictOutputBedaX = {}
dictOutputBedaY = {}
countSama =0
countSamaCek =0
countBedaY =0
countBedaX =0
countSamacek = 0
data1Lines = dataX.readlines()
data2Lines = dataY.readlines()

dictX = {}
dictY = {}
for k in data1Lines:
	k  = k.rstrip()
	k = k.replace("_"," ")
	dictX[k] = k
for k in data2Lines:
	k  = k.rstrip()
	dictY[k] = k
for key in dictX.keys():
	if key in dictY.keys():
		countSama = countSama+1
		dictOutputSama[key] = key
	else:
		countBedaX = countBedaX+1
		dictOutputBedaX[key] = key
for key in dictY.keys():
	if key in dictX.keys():
		countSamaCek = countSamaCek+1
	else:
		countBedaY = countBedaY+1
		dictOutputBedaY[key] = key
print("Jumlah entity di X:  " +str(len(dictX)))

print("Jumlah entity di Y:  " +str(len(dictY)))
print(len(dictOutputSama))
sortedDictOutputSama = sorted(dictOutputSama.values())
sortedDictOutputBedaX = sorted(dictOutputBedaX.values())
sortedDictOutputBedaY = sorted(dictOutputBedaY.values())

print("Jumlah PER sama dikedua data 	:" + str(countSama))

print("Jumlah PER sama dikedua data [CEK]	:" + str(countSamaCek))
print("Jumlah PER yang ada di Y tapi tidak ada di X 	:" + str(countBedaY))
print("Jumlah PER yang ada di X tapi tidak ada di Y 	:" + str(countBedaX))
print("\n")



writeListofStringToFile(sortedDictOutputSama, output)

writeListofStringToFile(sortedDictOutputBedaX, outputBedaX)
writeListofStringToFile(sortedDictOutputBedaY, outputBedaY)
############################################################################
# End of PER
############################################################################



#set the input and output file
inputX = "dbpedia/expanded/Place_expanded.txt"
inputY = "dbpedia-new/validate/place.txt"



#########################  begin LOC ################################

dataX = open(inputX, "r")
dataY = open(inputY, "r")
folder = "cekPlace/validation/x-expand/"
output =  folder + "resultLOCSama.txt"
outputBedaY = folder+  "resultLOCBedaY.txt"
outputBedaX =  folder+ "resultLOCBedaX.txt"
dictOutputSama = {}
dictOutputBedaX = {}
dictOutputBedaY = {}
countSama =0
countSamaCek =0
countBedaY =0
countBedaX =0
countSamacek = 0
data1Lines = dataX.readlines()
data2Lines = dataY.readlines()

dictX = {}
dictY = {}
for k in data1Lines:
	k  = k.rstrip()
	k = k.replace("_"," ")
	dictX[k] = k
for k in data2Lines:
	k  = k.rstrip()
	dictY[k] = k
for key in dictX.keys():
	if key in dictY.keys():
		countSama = countSama+1
		dictOutputSama[key] = key
	else:
		countBedaX = countBedaX+1
		dictOutputBedaX[key] = key
for key in dictY.keys():
	if key in dictX.keys():
		countSamaCek = countSamaCek+1
	else:
		countBedaY = countBedaY+1
		dictOutputBedaY[key] = key
print("Jumlah entity di X:  " + str(len(dictX)))
print("Jumlah entity di Y:  " + str(len(dictY)))
print(len(dictOutputSama))
sortedDictOutputSama = sorted(dictOutputSama.values())
sortedDictOutputBedaX = sorted(dictOutputBedaX.values())
sortedDictOutputBedaY = sorted(dictOutputBedaY.values())

print("Jumlah LOC sama dikedua data 	:" + str(countSama))

print("Jumlah LOC sama dikedua data [CEK]	:" + str(countSamaCek))
print("Jumlah LOC yang ada di Y tapi tidak ada di X 	:" + str(countBedaY))
print("Jumlah LOC yang ada di X tapi tidak ada di Y 	:" + str(countBedaX))
print("\n")



writeListofStringToFile(sortedDictOutputSama, output)

writeListofStringToFile(sortedDictOutputBedaX, outputBedaX)
writeListofStringToFile(sortedDictOutputBedaY, outputBedaY)
############################################################################
# End of LOC
############################################################################


#set the input and output file
inputX = "dbpedia/expanded/ORG_expanded.txt"
inputY = "dbpedia-new/validate/organization.txt"



#########################  begin ORG ################################

dataX = open(inputX, "r")
dataY = open(inputY, "r")
folder = "cekOrganisation/validation/x-expand/"
output =  folder + "resultORGSama.txt"
outputBedaY = folder+  "resultORGBedaY.txt"
outputBedaX =  folder+ "resultORGBedaX.txt"
dictOutputSama = {}
dictOutputBedaX = {}
dictOutputBedaY = {}
countSama =0
countSamaCek =0
countBedaY =0
countBedaX =0
countSamacek = 0
data1Lines = dataX.readlines()
data2Lines = dataY.readlines()

dictX = {}
dictY = {}
for k in data1Lines:
	k  = k.rstrip()
	k = k.replace("_"," ")
	dictX[k] = k
for k in data2Lines:
	k  = k.rstrip()
	dictY[k] = k
for key in dictX.keys():
	if key in dictY.keys():
		countSama = countSama+1
		dictOutputSama[key] = key
	else:
		countBedaX = countBedaX+1
		dictOutputBedaX[key] = key
for key in dictY.keys():
	if key in dictX.keys():
		countSamaCek = countSamaCek+1
	else:
		countBedaY = countBedaY+1
		dictOutputBedaY[key] = key
print("Jumlah entity di X:  " + str(len(dictX)))
print("Jumlah entity di :  " + str(len(dictY)))
print(len(dictOutputSama))
sortedDictOutputSama = sorted(dictOutputSama.values())
sortedDictOutputBedaX = sorted(dictOutputBedaX.values())
sortedDictOutputBedaY = sorted(dictOutputBedaY.values())

print("Jumlah ORG sama dikedua data 	:" + str(countSama))

print("Jumlah ORG sama dikedua data [CEK]	:" + str(countSamaCek))
print("Jumlah ORG yang ada di Y tapi tidak ada di X 	:" + str(countBedaY))
print("Jumlah ORG yang ada di X tapi tidak ada di Y 	:" + str(countBedaX))
print("\n")



writeListofStringToFile(sortedDictOutputSama, output)

writeListofStringToFile(sortedDictOutputBedaX, outputBedaX)
writeListofStringToFile(sortedDictOutputBedaY, outputBedaY)
############################################################################
# End of ORG
############################################################################