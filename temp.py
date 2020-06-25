# z in code baraye  kharej kardane recorde  khas bekar  mire.
import csv
lines = list()
satr = 0
with open("C:/data set/danmark/aisdk_20190101.csv", "r") as f:
        data = list(csv.reader(f))
with open("C:/data set/danmark/tracker_cargo_tanker.csv", "w", newline='') as m1:
        writer = csv.writer(m1)
        for row in data:
            satr = satr + 1
            print(satr)
            k = row[1]
            if ((len(k) != 0) and (row[3]=="Cargo" or row[3]=="Tanker")):
                writer.writerow(row)



##############################################################################################
import csv
lines = list()
satr = 0
with open("C:/data set/danmark/aisdk_20190101.csv", "r") as f:
        data = list(csv.reader(f))
with open("C:/data set/danmark/tracker.csv", "w", newline='') as m1:
        writer = csv.writer(m1)
        for row in data:
            satr = satr + 1
            print(satr)
            k = row[1]
            if len(k) != 0:
                writer.writerow(row)


##################################################################################
import csv
lines = list()
asl_satr=0
nahaee=0
with open('C:/data set/danmark/aisdk_20190101.csv', 'r') as readFile:

    reader = csv.reader(readFile)

    for row in reader:
        nahaee=nahaee+1
        print(nahaee)
        lines.append(row)
        k=row[1]
        if len(k)==0:
            lines.remove(row)

with open('C:/data set/danmark/mycsv.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
