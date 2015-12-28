"""preprocess.py: Perform some proprocessing on the imported data"""
import numpy as np
import pandas as pd
from sklearn import preprocessing

#Remove NaN values
def replaceMissing(data):
	data = data.fillna(data.mean())
	return data

def fixZeroGPSHeight(data):
	mean = data[data.gps_height != 0].gps_height.mean().round(0)
	data.ix[data.gps_height == 0, 'gps_height'] = mean
	return data

def fixZeroPopulation(data):
	mean = data[data.population > 0].population.mean().round(0)
	data.ix[data.population == 0, 'population'] = mean
	return data

def fixZeroLatitude(data):
	mean = data[data.latitude > 0].latitude.mean()
	data.ix[data.latitude == 0, 'latitude'] = mean
	return data

def fixZeroLongitude(data):
	mean = data[data.longitude != -0.00000002].longitude.mean()
	data.ix[data.latitude == -0.00000002, 'longitude'] = mean
	return data

def fixZeroTSH(data):
	mean = data[data.amount_tsh > 0].amount_tsh.mean()
	data.ix[data.amount_tsh == 0, 'amount_tsh'] = mean
	return data

def normaliseData(data):
	newdata = pd.DataFrame(data).astype(float)
	df_norm = (newdata - newdata.min()) / (newdata.max() - newdata.min())
	return df_norm

def fixUnknownStrings(data):
	data = data.replace('','unknown')
	data = data.replace('Other','unknown')
	data = data.replace('other','unknown')
	return data

def fixZeroConstructionYear(data):
	mean = data[data.construction_year > 0].construction_year.mean().round(0)
	data.ix[data.construction_year == 0, 'construction_year'] = mean
	return data



# def fixExtractionGroup(data):
# 	extraction_dict = {
# 		"ksb": "submersible",
# 		2: "B"
# 	}
# 	data = data.replace({"extraction_type_group": extraction_dict})

def tidyData(data):
	data = data.drop('recorded_by', 1)
	data = data.drop('payment_type', 1)
	data = data.drop('extraction_type_class',1)
	data = data.drop('extraction_type_group',1)
	data = data.drop('quality_group',1)
	data = data.drop('quantity_group',1)
	data = data.drop('source_type',1)
	data = data.drop('waterpoint_type_group',1)
	data = data.drop('region',1)
	data = replaceMissing(data)
	data = fixZeroPopulation(data)
	data = fixZeroTSH(data)
	data = fixZeroGPSHeight(data)
	data = fixZeroLatitude(data)
	data = fixZeroLongitude(data)
	data = fixZeroConstructionYear(data)
	data = normaliseData(data)
	return data


