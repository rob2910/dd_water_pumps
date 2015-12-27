"""read_data.py: Helper script to read data from csv files."""

import config
import pandas as pd
import numpy as np

""" readTestLabels : 
	Load test set labels into data structure """
def readTrainingLabels():
	data = pd.read_csv(config.TRAINING_SET_LABELS, sep=',',dtype=config.LABEL_DTYPE,index_col=0,encoding='utf8')
	return data

""" readData : 
	Load test or training set values into data structure """
def readData(file_name):
	data = pd.read_csv(file_name, sep=',',dtype=config.VALUE_DTYPE,index_col=0, parse_dates=[2],encoding='utf8')
	data["funder"] = pd.Categorical.from_array(data.funder).codes
	return data