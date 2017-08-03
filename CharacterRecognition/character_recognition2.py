#################
# Aug 2
# Do the one hot encoding for characters
#################
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

# ~~~~~~~~~~~~~~~~ Fix Random Seed for Reproducibility ~~~~~~~~~~~~~~~~
seed = 7
numpy.random.seed(seed)

# ~~~~~~~~~~~~~~~~ Load Letter Recognition Dataset ~~~~~~~~~~~~~~~~
dataset = numpy.genfromtxt("letter-recognition.txt", delimiter=",", dtype=None)

# ~~~~~~~~~~~~~~~~ Split into Input and Output Variables ~~~~~~~~~~~~~~~~
# Features list (20000 X 16)
input = []
for row in dataset:
	data = []
	for i in range(1,17):
		data.append(row[i])
	input.append(data)
#input = numpy.asarray(input)
#### print input
# Character char list
output = []
for row in dataset:
	output.append(row[0])
#### print output

# ~~~~~~~~~~~~~~~~ One Hot Encode Class Variables ~~~~~~~~~~~~~~~~
encoder = LabelEncoder()
encoder.fit(output)
encoded_output = encoder.transform(output)

# convert integers to binary variables (i.e. one hot encoded) (20000 X 26)
# Ex. A = [1. 0. ... 0. 0.]
# 	  B = [0. 1. ... 0. 0.]
bin_output = np_utils.to_categorical(encoded_output)
#### print bin_output

# ~~~~~~~~~~~~~~~~  Create Model ~~~~~~~~~~~~~~~~ 
input_dim_val = len(input)*len(input[0])

# 16 inputs --> [ # hidden nodes ] --> 26 outputs (26 [A-Z] )
model = Sequential()
model.add(Dense(100, input_dim=17, input_shape=(20000, 16), activation='relu'))
model.add(Dense(80, activation='relu'))
model.add(Dense(input_dim_val, activation='softmax')) ## softmax makes sure outputs are 0 or 1

# ~~~~~~~~~~~~~~~~  Compile Model ~~~~~~~~~~~~~~~~ 
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# ~~~~~~~~~~~~~~~~ Fit Model ~~~~~~~~~~~~~~~~ 
model.fit(input, output, epochs=30, batch_size=10)

# ~~~~~~~~~~~~~~~~ Evaluate the Model ~~~~~~~~~~~~~~~~ 
scores = model.evaluate(input, output)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

