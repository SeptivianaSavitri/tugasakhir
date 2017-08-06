from function import writeListofStringToFile

folder = "newdata/trainingRule/ready/"
in1 = "goldstandard-0811.txt"
in2 = folder + "G2-1.txt"
out = folder + "io/G2-1.txt"
inputFile1 = open(in1, 'r', errors='ignore')
flines1 = inputFile1.readlines()
inputFile2 = open(in2, 'r', errors='ignore')
flines2 = inputFile2.readlines()
listOut = []
ulala = ""
for i in range(0, len(flines1)):
	data = flines1[i].replace("\n","")
	data2 = flines2[i].replace("\n","")
	splitData2 = data2.split(" ")
	ulala = data + "\t" + splitData2[1]
	listOut.append(ulala)


writeListofStringToFile(listOut,out)