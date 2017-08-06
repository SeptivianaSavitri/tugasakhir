from function import writeListofStringToFile,writeDictToFile


##########################################################################
# M A I N
##########################################################################




#set the input and output file
inputX = "cekPerson/expansion/x-expand/resultPERBedaX.txt"
inputY = "cekPerson/validation/x-expand/resultPERBedaX.txt"



#########################  begin PER ################################

dataX = open(inputX, "r",errors='ignore')
dataY = open(inputY, "r",errors='ignore')
folder = "huft/"
output =  folder + "resultSama.txt"
outputBedaY = folder+  "resultBedaY.txt"
outputBedaX =  folder+ "resultBedaX.txt"
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