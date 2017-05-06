
####################################################################################
# CompareDBPediaList.py
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
inputX = "dbpedia-new/original/person.txt"
inputY = "dbpedia-new/cleansing/person.txt"



#########################  begin PER ################################

dataX = open(inputX, "r")
dataY = open(inputY, "r")
folder = "cekPerson/cleansing/y-ori/"
output =  folder + "resultPERSama.txt"
outputcek =  folder + "resultPERSamaCek.txt"
outputBedaY = folder+  "resultPERBedaY.txt"
outputBedaX =  folder+ "resultPERBedaX.txt"
dictOutputSama = []
dictOutputSamaCek = []
dictOutputBedaX = []
dictOutputBedaY = []
countSama =0
countSamaCek =0
countBedaY =0
countBedaX =0
countSamacek = 0
data1Lines = dataX.readlines()
data2Lines = dataY.readlines()

dictX = []
dictY = []
for k in data1Lines:
	k  = k.rstrip()
	k = k.replace("_"," ")
	dictX.append(k)
print(len(dictX))
for k in data2Lines:
	k  = k.rstrip()
	dictY.append(k)
print(len(dictY))
for key in dictX:
	if key in dictY:
		countSama = countSama+1
		dictOutputSama.append(key)
	else:
		countBedaX = countBedaX+1
		dictOutputBedaX.append(key)
print(len(dictOutputSama))
for key in dictY:
	if key in dictX:
		countSamaCek = countSamaCek+1
		dictOutputSamaCek.append(key)
	else:
		countBedaY = countBedaY+1
		dictOutputBedaY.append(key)
print(len(dictOutputSamaCek))
print("Jumlah entity di X:  " +str(len(dictX)))

print("Jumlah entity di Y:  " +str(len(dictY)))


print("Jumlah PER sama dikedua data 	:" + str(countSama))

print("Jumlah PER sama dikedua data [CEK]	:" + str(countSamaCek))
print("Jumlah PER yang ada di Y tapi tidak ada di X 	:" + str(countBedaY))
print("Jumlah PER yang ada di X tapi tidak ada di Y 	:" + str(countBedaX))
print("\n")



writeListofStringToFile(dictOutputSama, output)

writeListofStringToFile(dictOutputSamaCek, outputcek)
writeListofStringToFile(dictOutputBedaX, outputBedaX)
writeListofStringToFile(dictOutputBedaY, outputBedaY)
############################################################################
# End of PER
############################################################################