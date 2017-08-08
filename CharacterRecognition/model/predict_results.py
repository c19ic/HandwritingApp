import numpy as np
from keras.models import load_model

# load data
X_test = np.load('x_test_data.npy')
y_test = np.load('y_test_data.npy')

# load model
print("Loading model")
model_path = "character_recognition_cnn.h5"
model = load_model(model_path)

# ~~~~~~~~~~~~~~~~ Predictions ~~~~~~~~~~~~~~~~
# calculate predictions
predictions = model.predict(X_test)

print(predictions)

# save predictions as npy file
np.save('predictions.npy', predictions)


print('Done')