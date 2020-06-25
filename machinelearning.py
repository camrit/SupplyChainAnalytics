# dar inja hame chiz mohaseb mishe  20 ta 20 ta joda mikone
from numpy import array
from numpy import hstack

import csv
import math
list0=[]

list=["209223000","211409100","211822000","211881000","212048000","215058000","218019000","218779000","219008000","219010252","219082000",
      "220018000","220289000","220552000","220609000","220614000","228330600","236216000","240244000","240891000","244013009","244267000",
      "244678000","244790522","246397000","246694000","247604000","248095000","248295000","248602000","255623000","255806146","256122000",
      "256757000","257519000","257742000","258764000","259360000","259888000","259890000","259936000","265581970","265724260","265734000",
      "265882000","266209000","266212000","266225000","266235000","273337270","311601000","311814000","419001223","636016188"]
list1=["10","2","26","19","5","19","16","25","33","48","39","7","20","43","20","5","5","1","1","12","7","6","30","1","2","42","6",
       "32","19","30","26","10","12","36","3","37","10","36","15","1","22","5","8","34","14","24","32","2","15","2","2","1","22","37"]
temp="# Timestamp,MMSI,season,day_time,Latitude,Longitude,rain,htsgwsfc_2,perpwsfc_2,precsno_3,qlml_3,speedmax_3,taugwx_3,taugwy_3,tlml_3,ulml_3,vlml_3,dirpwsfc_4,tcc_5,u_6,v_6,hic_7,ui_7,vi_7,rain-month_8,wsp_9,wind_stress_9,wsp_err_9,albedo_10,albvisdf_10,Width,Length,Gross Tonnage,Summer Deadweight,Draught,Navigational status,SOG,COG,Heading,Ship type,di,Actual time"

def extract(mmis):
    list0.clear()
    with open("C:/data set/danmark/16.csv") as f2:
        for line3 in f2:
            if mmis in line3:
                list0.append(line3)

def cordinate():

    tmp=list0[0]
    tmp1=tmp.split(',')
    lat1=tmp1[4]
    lon1=tmp1[5]
    v=len(list0)-1
    tmp2 = list0[v]
    tmp3=tmp2.split(',')
    lat2 = tmp3[4]
    lon2 = tmp3[5]
    valu=distance (lat1, lon1, lat2, lon2)
    return valu,lat1, lon1, lat2, lon2
#####################################################
def distance (lat1, long1, lat2, long2):
    R = 6373.0
    lat1=float(lat1)
    long1=float(long1)
    lat2 = float(lat2)
    long2 = float(long2)
    lat1 = math.radians(lat1)
    lon1 = math.radians(long1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(long2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    distance=float("{:.5f}".format(distance))
    print(distance)

    return distance

def printme( mmis):
    count=-1
    #field = []
    rain = 0
    htsgwsfc_2 = 0
    perpwsfc_2 = 0
    precsno = 0
    qlml = 0
    speedmax = 0
    taugwx = 0
    taugwy = 0
    tlml = 0
    ulml = 0
    vlml = 0
    dirpwsfc = 0
    tcc = 0
    u = 0
    v = 0
    hic = 0
    ui = 0
    vi = 0
    rain_month = 0
    wsp = 0
    wind_stress = 0
    wsp_err = 0
    albedo = 0
    albvisdf = 0
    SOG=COG=Heading=di=0
    kardam=0

    for line2 in list0:
        kardam=0
        #field.clear()
        field = line2.split(",")
        rain = rain + float(field[6])
        htsgwsfc_2 = htsgwsfc_2 + float(field[7])
        perpwsfc_2 = perpwsfc_2 + float(field[8])
        precsno = precsno + float(field[9])
        qlml = qlml + float(field[10])
        speedmax = speedmax + float(field[11])
        taugwx = taugwx + float(field[12])
        taugwy = taugwy + float(field[13])
        tlml = tlml + float(field[14])
        ulml = ulml + float(field[15])
        vlml = vlml + float(field[16])
        dirpwsfc = dirpwsfc + float(field[17])
        tcc = tcc + float(field[18])
        u = u + float(field[19])
        v = v + float(field[20])
        hic = hic + float(field[21])
        ui = ui + float(field[22])
        vi = vi + float(field[23])
        rain_month = rain_month + float(field[24])
        wsp = wsp + float(field[25])
        wind_stress = wind_stress + float(field[26])
        wsp_err = wsp_err + float(field[27])
        albedo = albedo + float(field[28])
        albvisdf = albvisdf + float(field[29])
        SOG = SOG + float(field[36])
        COG = COG + float(field[37])
        di = di + float(field[40])
        # ##################################################add to the field:

    with open("C:/data set/danmark/16.csv") as f2:
        for line3 in f2:
            if mmis in line3:
                field = line3.split(",")
                line1 = temp.split(",")
                field = line2.split(",")
                val, lat1, lon1, lat2, lon2=cordinate()
                tol = len(list0) - 1
                x = field[0]
                x = x + ',' + lat2
                x = x + ',' + lon2

                x=x+','+field[1]
                x = x + ',' + field[2]
                x = x + ',' + field[3]
                x = x + ',' + field[4]
                x = x + ',' + field[5]
                x= x+ ','+ str(rain / tol)
                x= x+ ','+ str(htsgwsfc_2 / tol)
                x= x+ ','+ str(perpwsfc_2 / tol)
                x= x+ ','+ str(precsno / tol)
                x= x+ ','+ str(qlml / tol)
                x= x+ ','+ str(speedmax / tol)
                x= x+ ','+ str(taugwx / tol)
                x = x + ',' + str(taugwy / tol)
                x= x+ ','+ str(tlml / tol)
                x= x+ ','+ str(ulml / tol)
                x=x+ ','+ str(vlml / tol)
                x=x+ ','+ str(dirpwsfc / tol)
                x=x+ ','+ str(tcc / tol)
                x=x+ ','+ str(u / tol)
                x=x+ ','+ str(v / tol)
                x=x+ ','+ str(hic / tol)
                x = x + ',' + str(ui / tol)
                x=x+ ','+ str(vi / tol)
                x=x+ ','+ str(rain_month / tol)
                x=x+ ','+ str(wsp / tol)
                x=x+ ','+ str(wind_stress / tol)
                x = x + ',' + str(wsp_err / tol)
                x=x+ ','+ str(albedo / tol)
                x = x + ',' + str(albvisdf / tol)
                x = x + ',' + field[30]
                x=x+ ','+ field[31]
                x=x+ ','+ field[32]
                x = x + ',' + field[33]
                x = x + ',' + field[34]
                x=x+ ','+ field[35]
                x=x+ ','+ str(SOG / tol)
                x = x + ',' + str(COG / tol)
                x = x + ',' + field[38]
                x=x+ ','+ field[39]
                x = x + ',' + str(val)
                x = x + ',' + field[41]


                #####################################
        # add = 'C:/data set/danmark/' + mmis + '.txt'
                add = 'C:/data set/danmark/' + "asad1" + '.txt'
                with open(add, "a") as file_object:
                    cont = 0
                    mak = ",".join(map(str, line1))
                    mak = mak + "\n"
                    file_object.write(x)
                    lock = 1
                    rain = 0
                    htsgwsfc_2 = 0
                    perpwsfc_2 = 0
                    precsno = 0
                    qlml = 0
                    speedmax = 0
                    taugwx = 0
                    taugwy = 0
                    tlml = 0
                    ulml = 0
                    vlml = 0
                    dirpwsfc = 0
                    tcc = 0
                    u = 0
                    v = 0
                    hic = 0
                    ui = 0
                    vi = 0
                    rain_month = 0
                    wsp = 0
                    wind_stress = 0
                    wsp_err = 0
                    albedo = 0
                    albvisdf = 0
                    SOG = 0
                    COG = 0
                    Heading = 0
                    di = 0
                    if lock == 1:
                        break
    return;

for mmis in list:
    extract(mmis)
    printme(mmis)



