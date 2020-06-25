import datetime

list=["209223000","211409100","211822000","211881000","212048000","215058000","218019000","218779000","219008000","219010252","219082000",
"220018000","220289000","220552000","220609000","220614000","228330600","236216000","240244000","240891000","244013009","244267000",
"244678000","244790522","246397000","246694000","247604000","248095000","248295000","248602000","255623000","255806146","256122000",
"256757000","257519000","257742000","258764000","259360000","259888000","259890000","259936000","265581970","265724260","265734000",
"265882000","266209000","266212000","266225000","266235000","273337270","311601000","311814000","419001223","636016188"]

temp="# Timestamp,	MMSI,	season,	day_time,	Latitude,	Longitude,	rain,	htsgwsfc_2,	perpwsfc_2,	precsno_3,	qlml_3,	speedmax_3,	taugwx_3,	taugwy_3,	 tlml_3,	ulml_3,	 vlml_3,	dirpwsfc_4,	tcc_5,	u_6,	v_6,	hic_7,	ui_7,	vi_7,	rain-month_8,	wsp_9,	wind_stress_9,	wsp_err_9,	albedo_10,	albvisdf_10,	Width,	Length,	Gross Tonnage,	Summer Deadweight,	Draught,	Navigational status,	ROT,	SOG,	COG,	Heading,	Ship type,	di,	Actual time"
def season(dat):
    s = dat
    date=s.split(" ")
    month=date[0].split("/")[1]
    hour=date[1].split(":")[0]
    if month in ['03','04','05']:
        add=1
    elif month in ['06','07','08']:
        add=2
    elif month in ['09','10','11']:
        add=3
    elif month in ['12','01','02']:
        add=4

    if hour>='00' and hour<='06':
        time=1
    elif hour>'06' and hour<='12':
        time=2
    elif hour>'12' and hour<='18':
        time=3
    elif hour>'18' and hour<='24':
        time=4
    return add, time

def printme( mmis):
    with open("C:/data set/danmark/14.csv") as f2:
        for line3 in f2:
            if mmis in line3:
                fields = line3.split(",")
                line1 = temp.split(",")
                line1[0] = fields[0]
                line1[1] = fields[1]
                x,y= season(fields[0])
                line1[2] = x
                line1[3] = y
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
                line1[32] = fields[32]
                line1[33] = fields[33]
                line1[34] = fields[34]
                line1[35] = fields[35]
                line1[36] = fields[36]
                line1[37] = fields[37]
                line1[38] = fields[38]
                line1[39] = fields[39]
                line1[40] = fields[40]
                line1[41] = fields[41]
                line1[42] = fields[42]

                with open("C:/data set/danmark/asad1.txt", "a") as file_object:
                    mak = ','.join(map(str, line1))
                    file_object.write(mak)
    return;


for mmis in list:
    printme(mmis)
    print(mmis)