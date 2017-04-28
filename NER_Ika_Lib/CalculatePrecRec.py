
####################################################################################
# CalculatePrecRec.py
# @Author: Septiviana Savitri
# @Last update: 21 April 2017
# Fasilkom Universitas Indonesia
#
# Objective: To calculate the precission and recall for rule-based tagging
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
inputPredict = "newdata/training/ready/ID_tagged_vitri2504-gs.txt"
inputFact = "nospace-goldstandard-0811.txt"


#outputtmp = folder + "tmp.txt"

#########################  begin ################################




dataPredict = open(inputPredict, "r")
dataFact = open(inputFact, "r")
output =   open("resultPrecRec.txt", "w", errors='replace')

data1Lines = dataPredict.readlines()
data2Lines = dataFact.readlines()
print(len(data2Lines))

line1 = []
TPPER = []
TPORG = []
TPLOC = []

counterTPPER = 0
counterTPORG = 0
counterTPLOC = 0

counterFPPER = 0
counterFPORG = 0
counterFPLOC = 0


counterFNPER = 0
counterFNORG = 0
counterFNLOC = 0



counterPER = 0

counterSama = 0
counterBeda = 0
for i in range(0,len(data1Lines)):
	splitPredict = data1Lines[i].split(" ")
	splitFact = data2Lines[i].split("\t")
	splitFact[1] = splitFact[1].replace("\n", "")
	splitPredict[1] = splitPredict[1].replace("\n", "")
	if splitFact[1] == "Person":
		counterPER = counterPER + 1

	if splitPredict[1] == splitFact[1]:

		if splitPredict[1] == "Person":
			#output.write( data1Lines[i].replace("\n", "") + "......" + data2Lines[i])
			counterTPPER = counterTPPER + 1
		elif splitPredict[1] == "Place":
			output.write( data1Lines[i].replace("\n", "") + "......" + data2Lines[i])
			counterTPLOC = counterTPLOC + 1
		elif splitPredict[1] == "Organisation":
			output.write( data1Lines[i].replace("\n", "") + "......" + data2Lines[i])
			counterTPORG = counterTPORG + 1
	else:
		#output.write(data1Lines[i].replace("\n","") + " "+ data2Lines[i].replace("\n","")+ " BERBEDA\n")

		#Cari False Positive
		#Untuk person
			if splitPredict[1] == "Person" and splitFact[1] == "Place":
				counterFPPER = counterFPPER + 1
			elif splitPredict[1] == "Person" and splitFact[1] == "Organisation":
				counterFPPER = counterFPPER + 1
			elif splitPredict[1] == "Person" and splitFact[1] == "O":
				counterFPPER = counterFPPER + 1
		#untuk place
			if splitPredict[1] == "Place" and splitFact[1] == "Person":
				counterFPLOC = counterFPLOC + 1
			if splitPredict[1] == "Place" and splitFact[1] == "Organisation":
				counterFPLOC = counterFPLOC + 1
			if splitPredict[1] == "Place" and splitFact[1] == "O":
				counterFPLOC = counterFPLOC + 1
		#untuk organisation
			if splitPredict[1] == "Organisation" and splitFact[1] == "Place":
				counterFPORG = counterFPORG + 1
			if splitPredict[1] == "Organisation" and splitFact[1] == "Person":
				counterFPORG = counterFPORG + 1
			if splitPredict[1] == "Organisation" and splitFact[1] == "O":
				counterFPORG = counterFPORG + 1

		#Cari False Negative
		#untuk person
			if splitPredict[1] == "Organisation" and splitFact[1] == "Person":
				counterFNPER = counterFNPER + 1
			if splitPredict[1] == "Place" and splitFact[1] == "Person":
				counterFNPER = counterFNPER + 1
			if splitPredict[1] == "O" and splitFact[1] == "Person":
				counterFNPER = counterFNPER + 1
		#untuk place
			if splitPredict[1] == "Organisation" and splitFact[1] == "Place":
				counterFNLOC = counterFNLOC + 1
			if splitPredict[1] == "Person" and splitFact[1] == "Place":
				counterFNLOC = counterFNLOC + 1
			if splitPredict[1] == "O" and splitFact[1] == "Place":
				counterFNLOC = counterFNLOC + 1
		#untuk ORGANISATION
			if splitPredict[1] == "Place" and splitFact[1] == "Organisation":
				counterFNORG = counterFNORG + 1
			if splitPredict[1] == "Person" and splitFact[1] == "Organisation":
				counterFNORG = counterFNORG + 1
			if splitPredict[1] == "O" and splitFact[1] == "organisation":
				counterFNORG = counterFNORG + 1



#precision = tp / (tp+fp)
#recall = tp / (tp+fn)
print("Jumlah TP PER :    "+str(counterTPPER))
print("Jumlah TP LOC :    "+str(counterTPLOC))
print("Jumlah TP ORG :    "+str(counterTPORG))
print("Jumlah FP PER :    "+str(counterFPPER))
print("Jumlah FP LOC :    "+str(counterFPLOC))
print("Jumlah FP ORG :    "+str(counterFPORG))

print("Jumlah FN PER :    "+str(counterFNPER))
print("Jumlah FN LOC :    "+str(counterFNLOC))
print("Jumlah FN ORG :    "+str(counterFNORG))
print("\n")
precPer = counterTPPER / (counterTPPER+counterFPPER)
recPer = counterTPPER / (counterTPPER+counterFNPER)
print("precision Person :    "+str(precPer))
print("RECALL Person 	:    "+str(recPer))
print("F1-Score Person 	:	 "+ str(2 * ((precPer * recPer)/(precPer + recPer))))
print("\n")

precLoc = counterTPLOC / (counterTPLOC+counterFPLOC)
recLoc = counterTPLOC / (counterTPLOC+counterFNLOC)
print("precision Place :    "+str(precLoc))
print("RECALL Place :    "+str(recLoc))
print("F1-Score Place 	:	 "+ str(2 * ((precLoc * recLoc)/(precLoc + recLoc))))
print("\n")

precOrg = counterTPORG / (counterTPORG+counterFPORG)
recOrg = counterTPORG / (counterTPORG+counterFNORG)
print("precision Organisation :    "+str(precOrg))
print("RECALL Organisation :    "+str(precOrg))
print("F1-Score Organisation 	:	 "+ str(2 * ((precOrg * recOrg)/(precOrg + recOrg))))

print("\n")



output.close()



############################################################################
# End of file
############################################################################
