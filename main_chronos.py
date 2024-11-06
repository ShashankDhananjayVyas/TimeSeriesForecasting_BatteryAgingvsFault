import argparse

import numpy as np
import scipy.io as sio
import pandas as pd
import torch

from chronos import ChronosPipeline

import matplotlib.pyplot as plt

# Command line argument for model selection
# 'tiny' has 8M parameters
# 'mini' has 20M parameters
# 'small' has 46M parameters
# 'base' has 200M parameters
# 'large' has 710M parameters
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='tiny')
args = parser.parse_args()

# Set model name
model = 'amazon/chronos-t5-' + args.model

# Use 'mps' for Apple Silicon, 'cpu' for CPU inference or 'cuda' if GPU is available
device = 'mps'
# device = 'cpu'
if torch.cuda.is_available():
  device = 'cuda'

# Define model
pipeline = ChronosPipeline.from_pretrained(model, device_map=device, torch_dtype=torch.bfloat16)

# Load the data
data_mat = sio.loadmat('data.mat')
dataR = pd.DataFrame(data_mat['Resistance']) # convert the data to pandas dataframe

# Make predictions
context = torch.tensor(data['Resistance']) # context must be either a 1D tensor, a list of 1D tensors or
                                           # a left-padded 2D tensor with batch as the first dimension
prediction_length = 12
forecast = pipeline.predict(context, prediction_length)  # shape [num_series, num_samples, prediction_length]

# Visualize the results
plt.figure()
plt.plot(data['Resistance'], color='blue', label='Resistance From Data')
plt.plot(R_pred, color='red', label='Predicted Resistance')
plt.legend()
plt.grid()
plt.show()
