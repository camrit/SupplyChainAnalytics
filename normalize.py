import  csv
temp="# Timestamp,MMSI,season,day_time,Latitude,Longitude,rain,htsgwsfc_2,perpwsfc_2,precsno_3,qlml_3,speedmax_3,taugwx_3,taugwy_3,tlml_3,ulml_3,vlml_3,dirpwsfc_4,tcc_5,u_6,v_6,hic_7,ui_7,vi_7,rain-month_8,wsp_9,wind_stress_9,wsp_err_9,albedo_10,albvisdf_10,Width,Length,Gross Tonnage,Summer Deadweight,Draught,Navigational status,SOG,COG,Heading,Ship type,di,Actual time"

def norm1(v):
    a=1
    b=100
    min=131
    max=121579
    v=int(v)
    x1=(v-131) * (b-a)
    x2=(max-min)
    total=(x1/x2) + a
    return total
def norm2(v):
    a=1
    b=100
    min=262
    max=111013
    v=int(v)
    x1=(v-131)* (b-a)
    x2=(max-min)
    total2=(x1/x2) + a
    return total2

with open("C:/data set/danmark/15.csv") as f2:
    for line3 in f2:
        fields = line3.split(",")
        line1 = temp.split(",")
        line1[0] = fields[0]
        line1[1] = fields[1]
        line1[2] = fields[2]
        line1[3] = fields[3]
        line1[4] = fields[4]
        line1[5] = fields[5]
        line1[6] = fields[6]
        line1[7] = fields[7]
        line1[8] = fields[8]
        line1[9] = fields[9]
        line1[10] = fields[10]
        line1[11] = fields[11]
        line1[12] = fields[12]
        line1[13] = fields[13]
        line1[14] = fields[14]
        line1[15] = fields[15]
        line1[16] = fields[16]
        line1[17] = fields[17]
        line1[18] = fields[18]
        line1[19] = fields[19]
        line1[20] = fields[20]
        line1[21] = fields[21]
        line1[22] = fields[22]
        line1[23] = fields[23]
        line1[24] = fields[24]
        line1[25] = fields[25]
        line1[26] = fields[26]
        line1[27] = fields[27]
        line1[28] = fields[28]
        line1[29] = fields[29]
        line1[30] = fields[30]
        line1[31] = fields[31]
        line1[32] = norm1(fields[32])
        line1[33] = norm2(fields[33])
        line1[34] = fields[34]
        line1[35] = fields[35]
        line1[36] = fields[36]
        line1[37] = fields[37]
        line1[38] = fields[38]
        line1[39] = fields[39]
        line1[40] = fields[40]
        line1[41] = fields[41]
        with open("C:/data set/danmark/asad1.txt", "a") as file_object:
            mak = ','.join(map(str, line1))
            file_object.write(mak)
