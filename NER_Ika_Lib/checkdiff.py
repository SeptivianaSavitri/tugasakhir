
from function import writeListofStringToFile
data1 = open("newdata/training/ready/ID_tagged5k.txt", "r")
data2 = open("data/training/ready/ID_tagged5k.txt", "r")

outputdata1 =  "newdata/training/ready/withTab_ID_tagged1_gs.txt"
output =   open("different.txt", "w", errors='replace')
outputBeda =   open("differentBeda.txt", "w", errors='replace')

data1Lines = data1.readlines()
data2Lines = data2.readlines()
print(len(data2Lines))

line1 = []
for k in data1Lines:
	k=k.replace("\n","")
	splitK = k.split(" ")
	line1.append(splitK[0] + "\t"+splitK[1] +"\n")
	
writeListofStringToFile(line1, outputdata1)




counterSama = 0
counterBeda = 0
for i in range(0,len(data1Lines)):
        if data1Lines[i] == data2Lines[i]:
            output.write( data1Lines[i].replace("\n","")+" SAMA\n")
            counterSama = counterSama + 1
        else:
            output.write(data1Lines[i].replace("\n","") + " "+ data2Lines[i].replace("\n","")+ " BERBEDA\n")
            outputBeda.write(data1Lines[i].replace("\n","") + " "+ data2Lines[i].replace("\n","")+ " BERBEDA\n")
            counterBeda = counterBeda + 1

print("Jumlah kata sama  :    "+str(counterSama))
print("Jumlah kata beda   :    "+str(counterBeda))
output.close()