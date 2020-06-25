import csv
list0=[]
list=["209223000","211409100","211822000","211881000","212048000","215058000","218019000","218779000","219008000","219010252","219082000",
"220018000","220289000","220552000","220609000","220614000","228330600","236216000","240244000","240891000","244013009","244267000",
"244678000","244790522","246397000","246694000","247604000","248095000","248295000","248602000","255623000","255806146","256122000",
"256757000","257519000","257742000","258764000","259360000","259888000","259890000","259936000","265581970","265724260","265734000",
"265882000","266209000","266212000","266225000","266235000","273337270","311601000","311814000","419001223","636016188"]
list1=["10","2","26","19","5","19","16","25","33","48","39","7","20","43","20","5","5","1","1","12","7","6","30","1","2","42","6",
       "32","19","30","26","10","12","36","3","37","10","36","15","1","22","5","8","34","14","24","32","2","15","2","2","1","22","37"]
temp="# Timestamp,Type of mobile,MMSI,Latitude,Longitude,Navigational status,ROT,SOG,COG,Heading,IMO,Callsign,Name,Ship type,Cargo type,Width,Length,Type of position fixing device,Draught,Destination,ETA,Data source type,A,B,C,D"
line1=temp.split(",")
  #####################################################
def printme( mmis):
    count=1
    with open("C:/data set/danmark/14.csv") as f2:
        for line3 in f2:
            if mmis in line3:
                count=count+1

    return count

for mmis in list:

    k=printme(mmis)
    list0.append(k)
    print(mmis,': ', k)


list0.sort()
latd_smal=list0[0]
latd_big=list0[len(list0)-1]
print(latd_smal)
print(latd_big)



##################################################
# fit model
model.fit(x, y, epochs=200, verbose=0)
# demonstrate prediction
# x_input = array([[0, 1], [1, 1], [1, 0]])
# x_input = x_input.reshape((1, n_steps, n_features))
yhat = model.predict(x1, verbose=0)
print(yhat)