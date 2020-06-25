# Accessing a text file - www.101computing.net/mp3-playlist/
import csv
satr=0
list=[]

temp="# Timestamp,Type of mobile,MMSI,Latitude,Longitude,Navigational status,ROT,SOG,COG,Heading,IMO,Callsign,Name,Ship type,Cargo type,Width,Length,Type of position fixing device,Draught,Destination,ETA,Data source type,A,B,C,D"
line1=temp.split(",")
with open("C:/data set/danmark/aisdk2.csv", "w", newline='') as m1:
    writer = csv.writer(m1)
    file = open("C:/data set/danmark/aisdk_2019010111.txt", "r")
    for line in file:
        fields = line.split(",")
        #songTitle = fields[1]
        line1 = temp.split(",")
        line1[0]=fields[1]
        line1[1]=fields[2]
        line1[2]=fields[3]
        line1[3]=fields[4]
        line1[4]=fields[5]
        line1[5] = fields[6]
        line1[6] = fields[7]
        line1[7] = fields[8]
        line1[8] = fields[9]
        line1[9] = fields[10]
        line1[10] = fields[11]
        line1[11] = fields[12]
        line1[12] = fields[13]
        line1[13] = fields[14]
        line1[14] = fields[15]
        line1[15] = fields[16]
        line1[16] = fields[17]
        line1[17] = fields[18]
        line1[18] = fields[19]
        line1[19] = fields[20]
        line1[20] = fields[21]
        line1[21] = fields[22]
        line1[22] = fields[23]
        line1[23] = fields[24]
        line1[24] = fields[25]
        line1[25] = fields[26]

        writer.writerow(line1)
    #if songTitle=="Cargo" or songTitle=="tanker":
        # if songTitle == "246255000":
    # list.append(line)



