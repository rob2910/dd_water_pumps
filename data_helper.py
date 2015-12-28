"""read_data.py: Helper script to read data from csv files."""

import config
import pandas as pd
import numpy as np
import datetime as dt
import pre_process

def setCatgories(data,fields):
	for field in fields:
		data[field] = pd.Categorical.from_array(data[field]).codes
	return data 

dataConv = lambda t : (dt.datetime.now()-dt.datetime.strptime(t, "%Y-%m-%d")).days

""" readTestLabels : 
	Load test set labels into data structure """
def readTrainingLabels():
	data = pd.read_csv(config.TRAINING_SET_LABELS, sep=',',dtype=config.LABEL_DTYPE,index_col=0,encoding='utf8')
	return data['status_group']

""" readData : 
	Load test or training set values into data structure """
def readData(file_name):
	data = pd.read_csv(file_name, sep=',',dtype=config.VALUE_DTYPE,index_col=0, parse_dates=[2],encoding='utf8',converters={'date_recorded' : dataConv})
	data = pre_process.fixUnknownStrings(data)
	data = setCatgories(data,["funder","installer","wpt_name","basin","subvillage","region","lga","ward","recorded_by","scheme_management","scheme_name","extraction_type","extraction_type_group","extraction_type_class","management","management_group","payment","payment_type","water_quality","quality_group","quantity","quantity_group","source","source_type","source_class","waterpoint_type","waterpoint_type_group"])
	data = pre_process.tidyData(data)
	return data

def saveData(data,file_name,columns):
	data[columns].to_csv(file_name, sep=',', encoding='utf-8')