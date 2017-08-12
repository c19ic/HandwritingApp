"""
Convolutional Neural Net EMNIST
ORIG: RUNS 100 SECONDS PER EPOCH
"""
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
import NISTparser


X_train, X_test, y_train, y_test = NISTparser.X_train, NISTparser.X_test, NISTparser.y_train, NISTparser.y_test
num_classes = 62
# ~~~~~~~~~~~~~~~~ Create the Convo Neural Net Model ~~~~~~~~~~~~~~~~ 
def cnn_model():
	# create model
	model = Sequential()
	model.add(Conv2D(30, (5, 5), input_shape=(1, 28, 28), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Conv2D(15, (3, 3), activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dense(50, activation='relu'))
	model.add(Dense(num_classes, activation='softmax'))
	
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model
	

# build the model
print("Building model...")
model = cnn_model()

# fit the model
print("Fitting model...")
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=200)

# Save model and datasets
model.save('character_recognition_cnn.h5')
print("Model saved in character_recognition_cnn.h5")

"""
np.save('x_train_data.npy', X_train)
print("X_train dataset saved in x_train_data.npy")

np.save('y_train_data.npy', y_train)
print("y_train dataset saved in y_train_data.npy")

np.save('x_test_data.npy', X_test)
print("X_test dataset saved in x_test_data.npy")

np.save('y_test_data.npy', y_test)
print("y_test dataset saved in y_test_data.npy")
"""
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
