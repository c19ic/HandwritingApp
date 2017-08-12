# Convolutional Neural Network Model
As of August 12, program uses EMNIST dataset as test dataset to train model.
## Issue: build model raises ValueError: Negative dimension size caused by subtracting 5 from 1 for 'conv2d_1/convolution' (op: 'Conv2D') with input shapes: [?,1,28,28], [5,5,28,30].

## To rebuild model:
run `$python build_model.py`

## To test predictions of model:
1. In terminal run `$open predict_results.py`
2. At end of file, change function args (npy array to be loaded, save filename)
3. run `$python predict_results.py`


