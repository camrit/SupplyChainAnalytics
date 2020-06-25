
#https://machinelearningmastery.com/understanding-stateful-lstm-recurrent-neural-networks-python-keras/
#baraye khoroji
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
import numpy as np
from numpy import array
from numpy import hstack
import numpy

from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics

y = list()
y1 = list()
predict=list()
predict1=list()

list = ["211409100", "218779000", "219082000", "236216000", "240244000", "244267000", "244790522", "255623000",
        "255806146", "256122000", "257519000", "259890000","259936000", "311601000"]  # N0 of ships
list1 = ["311601000","266225000"]
############################################################################create empty matrix (15,101,39)
arr = []
for i in range(37):  # tedade ship  or tedade  sample ha dar halate kolli
    arr.append([])
    for h in range(41):  # tedade feature  ha az har  sample.
            arr[i].append(0)
x = np.array(arr)

# print(x.shape)
i1=-1
#################################################@################################## Training data
i1=i1+1
with open("C:/data set/danmark/machin1.csv") as f2:
    for line3 in f2:
        line3 = line3.split(",")
        if i1==0:
            sub = line3[0]
            sub = sub[3:]
        else:
            sub = line3[0]

        arr[i1][0] = sub
        arr[i1][1] = line3[1]
        arr[i1][2] = line3[2]
        arr[i1][3] = line3[3]
        arr[i1][4] = line3[4]
        arr[i1][5] = line3[5]
        arr[i1][6] = line3[6]
        arr[i1][7] = line3[7]
        arr[i1][8] = line3[8]
        arr[i1][9] = line3[9]
        arr[i1][10] = line3[10]
        arr[i1][11] = line3[11]
        arr[i1][12] = line3[12]
        arr[i1][13] = line3[13]
        arr[i1][14] = line3[14]
        arr[i1][15] = line3[15]
        arr[i1][16] = line3[16]
        arr[i1][17] = line3[17]
        arr[i1][18] = line3[18]
        arr[i1][19] = line3[19]
        arr[i1][20] = line3[20]
        arr[i1][21] = line3[21]
        arr[i1][22] = line3[22]
        arr[i1][23] = line3[23]
        arr[i1][24] = line3[24]
        arr[i1][25] = line3[25]
        arr[i1][26] = line3[26]
        arr[i1][27] = line3[27]
        arr[i1][28] = line3[28]
        arr[i1][29] = line3[29]
        arr[i1][30] = line3[30]
        arr[i1][31] = line3[31]
        arr[i1][32] = line3[32]
        arr[i1][33] = line3[33]
        arr[i1][34] = line3[34]
        arr[i1][35] = line3[35]
        arr[i1][36] = line3[36]
        arr[i1][37] = line3[37]
        arr[i1][38] = line3[38]
        arr[i1][39] = line3[39]
        arr[i1][40] = line3[40]
        actual_time = line3[41]
        y.append(actual_time)
        i1 = i1 + 1

y_train = np.array(y)
x_train = np.array(arr)


# print(x.shape)
# for i in range(len(x)):
#	print(x[i], y[i])
##################################################################################### testing data
arr1 = []
i1=-1
for i in range(17):  # tedade ship  or tedade  sample ha dar halate kolli
    arr1.append([])
    for h in range(41):
        arr1[i].append(0)
x1 = np.array(arr1)
print(x1.shape)

i1=i1+1
with open("C:/data set/danmark/machin2.csv") as f2:
    for line3 in f2:
        line3 = line3.split(",")
        if i1==0:
            sub = line3[0]
            sub = sub[3:]
        else:
            sub = line3[0]

        arr1[i1][0] = sub
        arr1[i1][1] = line3[1]
        arr1[i1][2] = line3[2]
        arr1[i1][3] = line3[3]
        arr1[i1][4] = line3[4]
        arr1[i1][5] = line3[5]
        arr1[i1][6] = line3[6]
        arr1[i1][7] = line3[7]
        arr1[i1][8] = line3[8]
        arr1[i1][9] = line3[9]
        arr1[i1][10] = line3[10]
        arr1[i1][11] = line3[11]
        arr1[i1][12] = line3[12]
        arr1[i1][13] = line3[13]
        arr1[i1][14] = line3[14]
        arr1[i1][15] = line3[15]
        arr1[i1][16] = line3[16]
        arr1[i1][17] = line3[17]
        arr1[i1][18] = line3[18]
        arr1[i1][19] = line3[19]
        arr1[i1][20] = line3[20]
        arr1[i1][21] = line3[21]
        arr1[i1][22] = line3[22]
        arr1[i1][23] = line3[23]
        arr1[i1][24] = line3[24]
        arr1[i1][25] = line3[25]
        arr1[i1][26] = line3[26]
        arr1[i1][27] = line3[27]
        arr1[i1][28] = line3[28]
        arr1[i1][29] = line3[29]
        arr1[i1][30] = line3[30]
        arr1[i1][31] = line3[31]
        arr1[i1][32] = line3[32]
        arr1[i1][33] = line3[33]
        arr1[i1][34] = line3[34]
        arr1[i1][35] = line3[35]
        arr1[i1][36] = line3[36]
        arr1[i1][37] = line3[37]
        arr1[i1][38] = line3[38]
        arr1[i1][39] = line3[39]
        arr1[i1][40] = line3[40]
        actual_time = line3[41]
        y1.append(actual_time)
        i1 = i1 + 1
y1 = np.array(y1)
x1 = np.array(arr1)
####################################################  SVM

svclassifier = SVC(kernel='sigmoid')
svclassifier.fit(x_train, y_train)

for i in range(17):
    m = np.array(x1[i])
    x_input = m.reshape(1, -1)
    y_pred = svclassifier.predict(x_input)
    predict.append(y_pred)
print(predict, "\n")
print(y1)

#######################3RF

clf=RandomForestClassifier(n_estimators=100)
clf.fit(x_train,y_train)

for i in range(17):
    m = np.array(x1[i])
    x_input = m.reshape(1, -1)
    y_pred = clf.predict(x_input)
    predict1.append(y_pred)
print("random forest")
print(predict1)
print(y1)

