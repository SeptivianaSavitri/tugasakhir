
####################################################################################
# Library of DBpedia Entities Expansion for Indonesian NER
#
# changeToIOB.py
#
# @Author: Septiviana Savitri
# @Last update: 10 Mei 2017
# Fasilkom Universitas Indonesia
#
# Objective: To transform the IO format into IOB
# input: 
#   - gile that has been tagged but in IO format
#
# output: tagged file in IOB Format
# 
####################################################################################
import re
from function import writeListofStringToFile
inputFile = "newdata/training/ready/ID_tagged5k_vitri0705-kebiasli-nltkasli.txt"
dataIn = open(inputFile, "r", errors = 'ignore')
output =   "newdata/training/ready/ID_tagged5k_vitri1005-IOB.txt"


dataLines = dataIn.readlines()


line = []
for i in range(0,len(dataLines)):
	k=dataLines[i].replace("\n","")
	splitK = re.split(" |\t",k)
	#splitK = k.split("\t")
	if splitK[1] == "O":
		line.append(splitK[0] + "\t"+splitK[1] +"\n")
	elif splitK[1] == "Person":
		kPrev = dataLines[i-1].replace("\n","")
		splitKPrev = re.split(" |\t",kPrev)
		#splitKPrev = kPrev.split("\t")
		if splitKPrev[1] == "Person":
			line.append(splitK[0] + "\t"+ "I-PERSON" +"\n")
		else:
			line.append(splitK[0] + "\t"+ "B-PERSON" +"\n")
	elif splitK[1] == "Place":
		kPrev = dataLines[i-1].replace("\n","")
		splitKPrev = re.split(" |\t",kPrev)
		#splitKPrev = kPrev.split("\t")
		if splitKPrev[1] == "Place":
			line.append(splitK[0] + "\t"+ "I-LOCATION" +"\n")
		else:
			line.append(splitK[0] + "\t"+ "B-LOCATION" +"\n")

	else:
		kPrev = dataLines[i-1].replace("\n","")
		splitKPrev = re.split(" |\t",kPrev)
		#splitKPrev = kPrev.split("\t")
		if splitKPrev[1] == "Organisation":
			line.append(splitK[0] + "\t"+ "I-ORGANIZATION" +"\n")
		else:
			line.append(splitK[0] + "\t"+ "B-ORGANIZATION" +"\n")

writeListofStringToFile(line, output)



