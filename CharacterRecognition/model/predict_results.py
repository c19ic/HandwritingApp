import numpy as np
import os
from keras.models import load_model

def predict_results (abs_path, save_filename):
	''' Loads numpy array specified by 
	   	Input: abs_path to numpy array to be loaded
	   		   save_filename to save predictions in data folder
	   	Output:saved numpy and text files of predictions in data folder
	   	---> ? always save predictions in predictions.txt and predictions.npy
	'''
	path = "./data/"
	save_filename = save_filename.split('.')[0]
	save_filename = os.path.join(path, save_filename)
	print(save_filename)

	# load data for testing
	try:
		X_test = np.load(abs_path)
	except OSError, e:
			sys.exit()

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
	np.save(save_filename + '.npy', predictions)
	# save predictions as txt file
	np.savetxt(save_filename + '.txt', predictions)

	print('Done')

## For testing	
#predict_results("./data/digit_pics.npy", "predictions")