from ner_ika import writeDictToFile

data1 = open("dbpedia-new/original/listNegara.txt", "r")
data2 = "dbpedia-new/original/listNegaraWrite.txt"
place = {}
dataBaca = data1.readlines()
for data in dataBaca:
	place[data] = data

writeDictToFile(place,data2)
placeExpand = {}
data3 = open("dbpedia-new/expanded/place.txt", "r")
data4 = "dbpedia-new/validate/place.txt"
data3List = data3.readlines()
for placeIter in data3List:
	placeExpand[placeIter] = placeIter
for placeLine in place:
	placeExpand[placeLine] = placeLine
writeDictToFile(placeExpand, data4)