# Accessing a text file - www.101computing.net/mp3-playlist/
import csv
satr=0
list=[]
file = open("C:/data set/danmark/aisdk_20190101.txt", "r")
for line in file:
    fields = line.split(",")
    songTitle = fields[2]
    satr=satr+1
    print(satr)
    if songTitle=="Cargo" or songTitle=="tanker":
   # if songTitle == "246255000":
        list.append(line)

with open("C:/data set/danmark/aisdk_2019010111.txt", "w") as m1:
    writer = csv.writer(m1)
    writer.writerow(list)
#############################################################


with open("C:/data set/danmark/aisdk_20190101.txt") as f:
    with open("C:/data set/danmark/aisdk_20190101__2.txt", "w") as f1:
        for line in f:
            if "211822000" in line:
                f1.write(line)
                print(line)