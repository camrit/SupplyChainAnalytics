import numpy as np
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import numpy
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.optimizers import SGD
from keras.optimizers import Adadelta
import numpy
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.constraints import maxnorm
import numpy
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

y = list()
y1 = list()
list = ["211409100", "218779000", "219082000", "236216000", "240244000", "244267000", "244790522", "255623000",
        "255806146", "256122000", "257519000", "259890000",
        "259936000", "266225000", "311601000"]  # N0 of ships
list1 = ["311601000"]
############################################################################create empty matrix (15,101,39)
arr = []
for i in range(15):  # tedade ship  or tedade  sample ha dar halate kolli
    arr.append([])
    for j in range(101):  # tedade time step   or tedade  samples az har keshty or  tedade  satr az har  keshti
        arr[i].append([])
        for h in range(39):  # tedade feature  ha az har  sample.
            arr[i][j].append(0)
x = np.array(arr)
n_steps = 101
n_features = x.shape[2]
# print(x.shape)

#################################################@################################## Training data
for mmis in list:
    j = -1
    with open("16.csv") as f2:
        for line3 in f2:
            if mmis in line3:
                line3 = line3.split(",")
                j = j + 1
                i1 = list.index(mmis)
                arr[i1][j][0] = line3[2]
                arr[i1][j][1] = line3[3]
                arr[i1][j][2] = line3[4]
                arr[i1][j][3] = line3[5]
                arr[i1][j][4] = line3[6]
                arr[i1][j][5] = line3[7]
                arr[i1][j][6] = line3[8]
                arr[i1][j][7] = line3[9]
                arr[i1][j][8] = line3[10]
                arr[i1][j][9] = line3[11]
                arr[i1][j][10] = line3[12]
                arr[i1][j][11] = line3[13]
                arr[i1][j][12] = line3[14]
                arr[i1][j][13] = line3[15]
                arr[i1][j][14] = line3[16]
                arr[i1][j][15] = line3[17]
                arr[i1][j][16] = line3[18]
                arr[i1][j][17] = line3[19]
                arr[i1][j][18] = line3[20]
                arr[i1][j][19] = line3[21]
                arr[i1][j][20] = line3[22]
                arr[i1][j][21] = line3[23]
                arr[i1][j][22] = line3[24]
                arr[i1][j][23] = line3[25]
                arr[i1][j][24] = line3[26]
                arr[i1][j][25] = line3[27]
                arr[i1][j][26] = line3[28]
                arr[i1][j][27] = line3[29]
                arr[i1][j][28] = line3[30]
                arr[i1][j][29] = line3[31]
                arr[i1][j][30] = line3[32]
                arr[i1][j][31] = line3[33]
                arr[i1][j][32] = line3[34]
                arr[i1][j][33] = line3[35]
                arr[i1][j][34] = line3[36]
                arr[i1][j][35] = line3[37]
                arr[i1][j][36] = line3[38]
                arr[i1][j][37] = line3[39]
                arr[i1][j][38] = line3[40]
                actual_time = line3[41]
    y.append(actual_time)
y_train = np.array(y)
x_train = np.array(arr)
n_steps = 101
n_features = x_train.shape[2]
# print(x.shape)
# for i in range(len(x)):
#	print(x[i], y[i])
##################################################################################### testing data
arr1 = []
for i in range(1):  # tedade ship  or tedade  sample ha dar halate kolli
    arr1.append([])
    for j in range(101):  # tedade time step   or tedade  samples az har keshty or  tedade  satr az har  keshti
        arr1[i].append([])
        for h in range(39):  # tedade feature  ha az har  sample.
            arr1[i][j].append(0)
x1 = np.array(arr1)
print(x1.shape)
mmis = "311601000"
j = -1
i1 = 0
with open("16.csv") as f2:
    for line3 in f2:
        if mmis in line3:
            line3 = line3.split(",")
            j = j + 1
            arr1[i1][j][0] = line3[2]
            arr1[i1][j][1] = line3[3]
            arr1[i1][j][2] = line3[4]
            arr1[i1][j][3] = line3[5]
            arr1[i1][j][4] = line3[6]
            arr1[i1][j][5] = line3[7]
            arr1[i1][j][6] = line3[8]
            arr1[i1][j][7] = line3[9]
            arr1[i1][j][8] = line3[10]
            arr1[i1][j][9] = line3[11]
            arr1[i1][j][10] = line3[12]
            arr1[i1][j][11] = line3[13]
            arr1[i1][j][12] = line3[14]
            arr1[i1][j][13] = line3[15]
            arr1[i1][j][14] = line3[16]
            arr1[i1][j][15] = line3[17]
            arr1[i1][j][16] = line3[18]
            arr1[i1][j][17] = line3[19]
            arr1[i1][j][18] = line3[20]
            arr1[i1][j][19] = line3[21]
            arr1[i1][j][20] = line3[22]
            arr1[i1][j][21] = line3[23]
            arr1[i1][j][22] = line3[24]
            arr1[i1][j][23] = line3[25]
            arr1[i1][j][24] = line3[26]
            arr1[i1][j][25] = line3[27]
            arr1[i1][j][26] = line3[28]
            arr1[i1][j][27] = line3[29]
            arr1[i1][j][28] = line3[30]
            arr1[i1][j][29] = line3[31]
            arr1[i1][j][30] = line3[32]
            arr1[i1][j][31] = line3[33]
            arr1[i1][j][32] = line3[34]
            arr1[i1][j][33] = line3[35]
            arr1[i1][j][34] = line3[36]
            arr1[i1][j][35] = line3[37]
            arr1[i1][j][36] = line3[38]
            arr1[i1][j][37] = line3[39]
            arr1[i1][j][38] = line3[40]
            actual_time = line3[41]
    y1.append(actual_time)
y1 = np.array(y1)
x1 = np.array(arr1)
print(x1.shape)
for i in range(len(x1)):
    print(x1[i], y1[i])


####################################################  Create Model
def create_model(learn_rate=0.01, momentum=0):  # function to create model
    model = Sequential()
    model.add(LSTM(15, activation='relu', input_shape=(n_steps, n_features)))
    model.add(Dense(10,activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    optimizer = SGD(lr=learn_rate, momentum=momentum)
    model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model

# fix random seed for reproducibility
# seed = 7
# numpy.random.seed(seed)
# create model
model = KerasClassifier(build_fn=create_model, epochs=100, batch_size=10, verbose=0)
# define the grid search parameters
init_mode = ['uniform', 'lecun_uniform', 'normal', 'zero', 'glorot_normal', 'glorot_uniform', 'he_normal', 'he_uniform']
param_grid = dict(init_mode=init_mode)
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3)
grid_result = grid.fit(x_train, y_train)

# summarize results
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))


