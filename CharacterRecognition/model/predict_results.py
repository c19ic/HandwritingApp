import numpy as np
from keras.models import load_model

save_filename = 'test_run_digits1'

# load data - for testing
X_test = np.load('x_test_data.npy')
y_test = np.load('y_test_data.npy')

# normalize data
# input: array of imgs [arr]
# for i in arr: read img, reshape, normalize


# load model
print("Loading model......................")
model_path = "character_recognition_cnn.h5"
model = load_model(model_path)

# ~~~~~~~~~~~~~~~~ Predictions ~~~~~~~~~~~~~~~~
# calculate predictions
predictions = model.predict_classes(X_test)

print("\n")
print(predictions)
predictions.dtype = np.uint8
 
# save predictions as npy file
#np.save('predictions.npy', predictions)

np.save(save_filename + '.npy', predictions)
# save predictions as txt file
np.savetxt(save_filename + '.txt', predictions)

'''
# save predictions as txt file
with open('my_predictions.txt', 'w') as outfile:
	for i in predictions:
		outfile.write(i)
		outfile.write("\n")
	
	print type(predictions[0])
	print outfile
'''
print('Done')