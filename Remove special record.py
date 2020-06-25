# z in code baraye  kharej kardane recorde  khas bekar  mire.
import csv
lines = list()
satr = 0
with open("C:/data set/danmark/tracker_cargo_tanker.csv", "r") as f:
        data = list(csv.reader(f))
with open("C:/data set/danmark/tracker_cargo_tanker_remove record.csv", "w", newline='') as m1:
        writer = csv.writer(m1)
        for row in data:
            satr = satr + 1
            print(satr)
            if not (row[2]=="209155000" or row[2]=="211724850" or row[2]=="212893000" or row[2] == "218576000"
                or row[2] == "219001749" or row[2] == "219002358" or row[2] == "219003452" or row[2] == "219003966"
                or row[2] == "219016838" or row[2] == "219018865" or row[2] == "219019936" or row[2] == "219886000"
                or row[2] == "220439000" or row[2] == "230367000" or row[2] == "231800000" or row[2] == "244144000"
                or row[2] == "244630231" or row[2] == "246330000" or row[2] == "248907000" or row[2] == "253201000"
                or row[2] == "261509000" or row[2] == "261517000" or row[2] == "275463000" or row[2] == "275478000"
                or row[2] == "304877000" or row[2] == "538007384" or row[2] == "538090268" or row[2] == "563047300"
                or row[2] == "636015124" or row[2] == "636092457" or row[2] == "671956000" or row[2] == "219019354"
                or row[2] == "219397000" or row[2] == "220552000" or row[2] == "229192000" or row[2] == "235007690"
                or row[2] == "235102561" or row[2] == "235102583" or row[2] == "236111757" or row[2] == "259095000"
                or row[2] == "265734000" or row[2] == "265882000" or row[2] == "266225000" or row[2] == "636091469"):
                writer.writerow(row)