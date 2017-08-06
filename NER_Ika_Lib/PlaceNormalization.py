####################################################################################
# PlaceNormalization.py
# @Author: Septiviana Savitri
# @Last update: 1 Maret 2017
# Fasilkom Universitas Indonesia
#
# Objective: To normalized the original dbPedia 
# input: 
#   - File contain each type of clean data

# output: normalized version of data :
#    - remove all the description in (xx)
#   
####################################################################################


from function import writeListofStringToFile,findWord

##########################################################################
# M A I N
##########################################################################

#set the input and output file
input = "dbpedia-new/cleansing/place.txt"
folder = "dbpedia-new/normalized/"
output = folder + "place.txt"

outputnor = folder + "placeNOR.txt"
outputkur = folder + "placeKUR.txt"

#########################  begin ################################

inputFile = open(input, 'r', errors='ignore')
flines = inputFile.readlines()
newListPlace = []
newListPlaceNor = []
newListPlaceKur = []
count = 0
cek = 0
for k in flines:
	koorBuka = k.find("(")
	koorTutup = k.find(")")
	if koorBuka != -1: 
		k  = k[:koorBuka-1]
		newListPlace.append(k)
		newListPlaceKur.append(k)
		if k.find("Kabupaten Administrasi") != -1 or k.find("Kabupaten") != -1 or k.find("Kota Administrasi") != -1 or findWord(k,"kota") or k.find("Provinsi") != -1 or k.find("Kecamatan") != -1 or k.find("Desa") != -1:
			count = count+1
	

	if k.find("Kabupaten Administrasi") != -1:
		kBaru = k.replace("Kabupaten Administrasi","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k) 
		cek = cek + 1
	elif k.find("Kabupaten") != -1:
		kBaru = k.replace("Kabupaten","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k)
		cek = cek + 1
	elif k.find("Departemen") != -1:
		kBaru = k.replace("Departemen","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k) 
		cek = cek + 1
	elif k.find("Distrik") != -1:
		kBaru = k.replace("Distrik","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k) 
		cek = cek + 1
	elif k.find("Negara Bagian") != -1:
		kBaru = k.replace("Negara Bagian","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k) 
		cek = cek + 1
	elif k.find("Negara bagian") != -1:
		kBaru = k.replace("Negara bagian","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k) 
		cek = cek + 1
	elif k.find("Region") != -1:
		kBaru = k.replace("Region","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k) 
		cek = cek + 1
	elif k.find("Kota Administrasi") != -1:
		kBaru = k.replace("Kota Administrasi","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k) 
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k)
		cek = cek + 1
	elif k.find("Ibu Kota") != -1:
		kBaru = k.replace("Ibu Kota","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k) 
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k)
		cek = cek + 1
	elif findWord(k,"kota"):
		kBaru = k.replace("Kota","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k)
		cek = cek + 1
	elif k.find("Provinsi") != -1:
		kBaru = k.replace("Provinsi","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k)
		cek = cek + 1

	elif k.find("Kecamatan") != -1:
		kBaru = k.replace("Kecamatan","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k)
		cek = cek + 1
	elif k.find("Desa") != -1:
		kBaru = k.replace("Desa","")
		kBaru = kBaru.replace("  "," ")
		newListPlace.append(kBaru)
		newListPlace.append(k)
		newListPlaceNor.append(kBaru)
		newListPlaceNor.append(k)
		cek = cek + 1
	else:
		k = k.replace("  "," ")
		newListPlace.append(k);
	

inputFile.close()
writeListofStringToFile(newListPlace, output)
writeListofStringToFile(newListPlaceNor, outputnor)
writeListofStringToFile(newListPlaceKur, outputkur)