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
def vessel_model(neurons=1):  # function to create model
    model = Sequential()
    model.add(LSTM(neurons, activation= 'softsign', kernel_initializer='he_normal', kernel_constraint=maxnorm(4), input_shape=(n_steps, n_features)))
    model.add(Dropout(0.1))
    model.add(Dense(10, kernel_initializer='he_normal', activation='softsign', kernel_constraint=maxnorm(4)))
    model.add(Dropout(0.1))
    model.add(Dense(1, kernel_initializer='he_normal', activation='softsign', kernel_constraint=maxnorm(4)))
    optimizer = 'Adadelta'
    model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model

# fix random seed for reproducibility
# seed = 7
# numpy.random.seed(seed)
# create model
x_train, y_train=()

model = KerasClassifier(build_fn=vessel_model, epochs=200, batch_size=20, verbose=1)
neurons = [15,20,25]
weight_constraint = [1, 2, 3, 4, 5, 6]
learn_rate = [0.001, 0.01, 0.1, 0.2, 0.3]
momentum = [0.0, 0.2, 0.4, 0.6, 0.8, 0.9]
dropout_rate = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
optimizer = ['SGD', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam']
activation = ['softmax', 'softplus', 'softsign', 'relu', 'tanh', 'sigmoid', 'hard_sigmoid', 'linear']
init_mode = ['uniform', 'lecun_uniform', 'normal', 'zero', 'glorot_normal', 'glorot_uniform', 'he_normal', 'he_uniform']
param_grid = dict(neurons=neurons, momentum=momentum, init_mode=init_mode, activation=activation,
                  dropout_rate=dropout_rate, weight_constraint=weight_constraint)
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)
grid_result = grid.fit(x_train, y_train)
print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))


