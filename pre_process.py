"""preprocess.py: Perform some proprocessing on the imported data"""
import numpy as np


#Remove NaN values
def replaceMissing(data):
	data = data.fillna(data.mean())
	return data

def fixZeroPopulation(data):
	meanpopulation = data[data.population > 0].population.mean()
	data.ix[data.population == 0, 'population'] = meanpopulation
	return data


def tidyData(data):
	data = fixZeroPopulation(data)
	data = replaceMissing(data)
	return data

