## This is course material for Introduction to Modern Artificial Intelligence
## Example code: mlp.py
## Author: Allen Y. Yang
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Load dependencies
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

# Create data
linearSeparableFlag = False
x_bias = 6

def toy_2D_samples(x_bias, linearSeparableFlag):
    samples1 = np.random.multivariate_normal([5 + x_bias, 5], [[1, 0], [0, 1]], 50)
    samples2 = np.random.multivariate_normal([-5 + x_bias, -5], [[1, 0], [0, 1]], 50)
    samples3 = np.random.multivariate_normal([-5 + x_bias, 5], [[1, 0], [0, 1]], 50)           
    samples4 = np.random.multivariate_normal([5 + x_bias, -5], [[1, 0], [0, 1]], 50)

    samples = np.concatenate((samples1, samples2, samples3, samples4), axis=0)
    labels1 = np.array([[1, 1]] * 50 + [[-1, -1]] * 50)
    labels2 = np.array([[1, -1]] * 50 + [[-1, 1]] * 50)

    labels = np.concatenate((labels1, labels2), axis=0)
    return samples, labels

samples, labels = toy_2D_samples(x_bias, linearSeparableFlag)

# Split training and testing set
randomOrder = np.random.permutation(200)
trainingX = samples[randomOrder[0:100], :]
trainingY = labels[randomOrder[0:100], :]
testingX = samples[randomOrder[100:200], :]
testingY = labels[randomOrder[100:200], :]

model = Sequential()
model.add(Dense(2, input_shape=(2,), activation='linear', use_bias=True))  # No hidden layers, 2 perceptrons
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
                
model.fit(trainingX, trainingY, epochs=600, batch_size=15, verbose=1, validation_split=0.2)

score = 0
for i in range(100):
    predict_x = model.predict(np.array([testingX[i, :]]))
    estimate = np.sign(predict_x)

    if np.array_equal(testingY[i], estimate[0]):
        score += 1
    

    if estimate[0][0] == 1 and estimate[0][1] == 1:
        plt.plot(testingX[i, 0], testingX[i, 1], 'bo')
    elif estimate[0][0] == -1 and estimate[0][1] == -1:
        plt.plot(testingX[i, 0], testingX[i, 1], 'bo')
    else:
        plt.plot(testingX[i, 0], testingX[i, 1], 'rx')

    # estimate=np.argmax(predict_x)

    # if testingY[i,estimate] == 1:
    #     score = score  + 1

    # if estimate == 0:
    #     plt.plot(testingX[i, 0], testingX[i, 1], 'bo')
    # else: 
    #     plt.plot(testingX[i, 0], testingX[i, 1], 'rx')

print('Test accuracy:', score / 100)
plt.show()