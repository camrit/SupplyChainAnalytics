# dar inja hame chiz mohaseb mishe  20 ta 20 ta joda mikone
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
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
temp="# Timestamp,Type of mobile,MMSI,Latitude,Longitude,Navigational status,ROT,SOG,COG,Heading,IMO,Callsign,Name,Ship type,Cargo type,Width,Length,Type of position fixing device,Draught,Destination,ETA,Data source type,A,B,C,D"
line1=temp.split(",")

def extract(mmis):
    list0.clear()
    with open("C:/data set/danmark/13.csv") as f2:
        for line3 in f2:
            if mmis in line3:
                list0.append(line3)

def cordinate(count1):

    count2=count1 % 20
    if count2==0:
        index=count1-20
    elif count2 !=0:
        tagh = int(count1 / 20)
        tagh = count1 - (20 * tagh)
        index=count1 - tagh

    tmp=list0[index]
    tmp1=tmp.split(',')
    lat1=tmp1[2]
    lon1=tmp1[3]
    tmp2 = list0[count1]
    tmp3=tmp2.split(',')
    lat2 = tmp3[2]
    lon2 = tmp3[3]
    valu=distance (lat1, lon1, lat2, lon2)
    return valu
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
    SOG=COG=Heading=0
    kardam=0

    for line3 in list0:
        kardam=1
        count=count + 1
        if count == 0:

            #add = 'C:/data set/danmark/' + mmis + '.txt'
            add = 'C:/data set/danmark/' + "asad1" + '.txt'
            with open(add, "a") as file_object:
                kardam = 0
                line3 = line3.split(",")
                line3[42]="0"
                mak = ','.join(map(str, line3))
                mak=mak + "\n"

                file_object.write(mak)

        elif (count % 20 == 0):
            kardam=0
            field.clear()
            field = line3.split(",")
            rain = rain + float(field[4])
            htsgwsfc_2 = htsgwsfc_2 + float(field[5])
            perpwsfc_2 = perpwsfc_2 + float(field[6])
            precsno = precsno + float(field[7])
            qlml = qlml + float(field[8])
            speedmax = speedmax + float(field[9])
            taugwx = taugwx + float(field[10])
            taugwy = taugwy + float(field[11])
            tlml = tlml + float(field[12])
            ulml = ulml + float(field[13])
            vlml = vlml + float(field[14])
            dirpwsfc = dirpwsfc + float(field[15])
            tcc = tcc + float(field[16])
            u = u + float(field[17])
            v = v + float(field[18])
            hic = hic + float(field[19])
            ui = ui + float(field[20])
            vi = vi + float(field[21])
            rain_month = rain_month + float(field[22])
            wsp = wsp + float(field[3])
            wind_stress = wind_stress + float(field[23])
            wsp_err = wsp_err + float(field[24])
            albedo = albedo + float(field[25])
            albvisdf = albvisdf + float(field[26])
            SOG = SOG + float(field[38])
            COG = COG + float(field[39])
            Heading = Heading + float(field[40])
            # ##################################################add to the field:
            field[4] = rain / count
            field[5] = htsgwsfc_2 / 20
            field[6] = perpwsfc_2 / 20
            field[7] = precsno / 20
            field[8] = qlml / 20
            field[9] = speedmax /20
            field[10] = taugwx / 20
            field[11] = taugwy / 20
            field[12] = tlml / 20
            field[13] = ulml / 20
            field[14] = vlml / 20
            field[15] = dirpwsfc /20
            field[16] = tcc / 20
            field[17] = u / 20
            field[18] = v / 20
            field[19] = hic / 20
            field[20] = ui / 20
            field[21] = vi / 20
            field[22] = rain_month / 20
            field[23] = wsp / 20
            field[24] = wind_stress / 20
            field[25] = wsp_err / 20
            field[26] = albedo / 20
            field[27] = albvisdf / 20
            field[38] = SOG / 20
            field[39] = COG / 20
            field[40] = Heading / 20
            field[42] = cordinate(count)

            #add = 'C:/data set/danmark/' + mmis + '.txt'
            add = 'C:/data set/danmark/' + "asad1" + '.txt'
            with open(add, "a") as file_object:
                cont = 0
                mak = ','.join(map(str, field))
                mak=mak+ "\n"
                file_object.write(mak)
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

        else:

            field = line3.split(",")
            rain = rain + float(field[4])
            htsgwsfc_2 = htsgwsfc_2 + float(field[5])
            perpwsfc_2 = perpwsfc_2 + float(field[6])
            precsno = precsno + float(field[7])
            qlml = qlml + float(field[8])
            speedmax = speedmax + float(field[9])
            taugwx = taugwx + float(field[10])
            taugwy = taugwy + float(field[11])
            tlml = tlml + float(field[12])
            ulml = ulml + float(field[13])
            vlml = vlml + float(field[14])
            dirpwsfc = dirpwsfc + float(field[15])
            tcc = tcc + float(field[16])
            u = u + float(field[17])
            v = v + float(field[18])
            hic = hic + float(field[19])
            ui = ui + float(field[20])
            vi = vi + float(field[21])
            rain_month = rain_month + float(field[22])
            wsp = wsp + float(field[23])
            wind_stress = wind_stress + float(field[24])
            wsp_err = wsp_err + float(field[25])
            albedo = albedo + float(field[26])
            albvisdf = albvisdf + float(field[27])
            SOG = SOG + float(field[38])
            COG = COG + float(field[39])
            Heading = Heading + float(field[40])

    if kardam==1:

        if count>=20:
            taghsim=int(count/20)
            taghsim=count-(20 * taghsim)
        elif count<20:
            taghsim =count
        field.clear()
        field = line3.split(",")
        rain = rain + float(field[4])
        htsgwsfc_2 = htsgwsfc_2 + float(field[5])
        perpwsfc_2 = perpwsfc_2 + float(field[6])
        precsno = precsno + float(field[7])
        qlml = qlml + float(field[8])
        speedmax = speedmax + float(field[9])
        taugwx = taugwx + float(field[10])
        taugwy = taugwy + float(field[11])
        tlml = tlml + float(field[12])
        ulml = ulml + float(field[13])
        vlml = vlml + float(field[14])
        dirpwsfc = dirpwsfc + float(field[15])
        tcc = tcc + float(field[16])
        u = u + float(field[17])
        v = v + float(field[18])
        hic = hic + float(field[19])
        ui = ui + float(field[20])
        vi = vi + float(field[21])
        rain_month = rain_month + float(field[22])
        wsp = wsp + float(field[3])
        wind_stress = wind_stress + float(field[23])
        wsp_err = wsp_err + float(field[24])
        albedo = albedo + float(field[25])
        albvisdf = albvisdf + float(field[26])
        SOG = SOG + float(field[38])
        COG = COG + float(field[39])
        Heading = Heading + float(field[40])
        # ##################################################add to the field:
        field[4] = rain / taghsim
        field[5] = htsgwsfc_2 / taghsim
        field[6] = perpwsfc_2 / taghsim
        field[7] = precsno / taghsim
        field[8] = qlml / taghsim
        field[9] = speedmax / taghsim
        field[10] = taugwx / taghsim
        field[11] = taugwy / taghsim
        field[12] = tlml / taghsim
        field[13] = ulml / taghsim
        field[14] = vlml / taghsim
        field[15] = dirpwsfc / taghsim
        field[16] = tcc / taghsim
        field[17] = u / taghsim
        field[18] = v / taghsim
        field[19] = hic / taghsim
        field[20] = ui / taghsim
        field[21] = vi / taghsim
        field[22] = rain_month /taghsim
        field[23] = wsp / taghsim
        field[24] = wind_stress /taghsim
        field[25] = wsp_err / taghsim
        field[26] = albedo / taghsim
        field[27] = albvisdf / taghsim
        field[38] = SOG / taghsim
        field[39] = COG / taghsim
        field[40] = Heading / taghsim
        field[42] = cordinate(count)
       # add = 'C:/data set/danmark/' + mmis + '.txt'
        add = 'C:/data set/danmark/' + "asad1" + '.txt'
        with open(add, "a") as file_object:
            cont = 0
            mak = ','.join(map(str, field))
            mak = mak + "\n"
            file_object.write(mak)
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

    return;

for mmis in list:
    extract(mmis)
    printme(mmis)







        line1[38] = '0'
        x4 = field[0]
        line1[0] = x4
        x4 = field[1]
        line1[1] = x4
        x4 = field[2]
        line1[2] = x4
        x4 = field[3]
        line1[3] = x4
        x4 = field[4]
        line1[4] = x4
        x4 = field[5]
        line1[5] = x4
        x4 = field[30]
        line1[30] = x4
        x4 = field[31]
        line1[31] = x4
        x4 = field[32]
        line1[32] = x4
        x4 = field[33]
        line1[33] = x4
        x4 = field[34]
        line1[34] = x4
        line1[35] = '0'
        x4 = field[39]
        line1[39] = x4
        x4 = str(cordinate())
        line1[40] = x4
        x4 = field[41]
        line1[41] = x4



