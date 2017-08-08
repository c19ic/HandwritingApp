# Convolutional Neural Network Model
As of August 8, program uses MNIST dataset as test dataset to train model.
X datasets were not uploaded because they were too large.

## Usage
0. Open new terminal
1. Copy folder to local directory
2. cd into model folder

## To rebuild model:
run `$python build_model.py`

### Model Inputs
Image of a number (0-9) as a matrix with 1s and 0s.

### Model Output
Classification of image as a number (0-9).
Each test and train datasets are saved as .npy files.
Model is saved as .npy file.
Accuracy is printed in terminal.

## To test predictions of model:
run `$python predict_results.py`

### File inputs
Test dataset that was saved from running `$python build_model.py`

### File outputs
Predictions are printed in terminal and saved into predications.npy.
