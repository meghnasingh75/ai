# ALGORITHM: 
# The steps to cover in this are as follows: 
# 1. Load Data. 
# 2. Define Keras Model. 
# 3. Compile Keras Model. 
# 4. Fit Keras Model. 
# 5. Evaluate Keras Model. 
# 6. Tie It All Together. 
# 7. Make Predictions 



# DEFINE THE MODEL
# first neural network with keras tutorial 
from numpy import loadtxt 
from keras.models import Sequential 
from keras.layers import Dense 
# load the dataset 
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',') 
# split into input (X) and output (y) variables 
X = dataset[:,0:8] 
y = dataset[:,8] 
# define the keras model 
model = Sequential() 
model.add(Dense(12, input_dim=8, activation='relu')) 
model.add(Dense(8, activation='relu')) 
model.add(Dense(1, activation='sigmoid')) 
# compile the keras model 
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy']) 
# fit the keras model on the dataset 
model.fit(X, y, epochs=150, batch_size=10,verbose=0) 
# evaluate the keras model 
_, accuracy = model.evaluate(X, y, verbose=0) 
print('Accuracy: %.2f' % (accuracy*100))




# PREDICTING FROM MODEL
# first neural network with keras make predictions 
from numpy import loadtxt 
from keras.models import Sequential 
from keras.layers import Dense 
# load the dataset 
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',') 
# split into input (X) and output (y) variables 
X = dataset[:,0:8] 
y = dataset[:,8] 
# define the keras model 
model = Sequential() 
model.add(Dense(12, input_dim=8, activation='relu')) 
model.add(Dense(8, activation='relu')) 
model.add(Dense(1, activation='sigmoid')) 
# compile the keras model 
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])
 
# fit the keras model on the dataset 
model.fit(X, y, epochs=150, batch_size=10, verbose=0) 
# make class predictions with the model 
predictions = model.predict_classes(X) 
# summarize the first 5 cases 
for i in range(5): 
    print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))