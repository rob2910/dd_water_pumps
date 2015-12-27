"""config.py: Holds constants for dd_water_dumps program."""
import numpy as np
import pandas as pd

TEST_SET_VALUES = "./data/test_set_values.csv"
TRAINING_SET_LABELS = "./data/training_set_labels.csv"
TRAINING_SET_VALUES = "./data/training_set_values.csv"

LABEL_DTYPE={ 'id' : np.float64, 'status_group' : str }

VALUE_DTYPE={
	"id" : np.int32,
	"amount_tsh" : np.float64,
	"date_recorded" : pd.datetime,
	"funder" : str,
	"gps_height" : np.uint32,
	"installer" : str,
	"longitude" : np.float64,
	"latitude" : np.float64,
	"wpt_name" : str,
	"num_private" : np.uint32,
	"basin" : str,
	"subvillage" : str,
	"region" : str,
	"region_code" : np.uint16,
	"district_code" : np.uint16,
	"lga" : str,
	"ward" : str,
	"population" : np.uint32,
	"public_meeting" : np.bool,
	"recorded_by" : str,
	"scheme_management" : str,
	"scheme_name" : str,
	"permit" : np.bool,
	"construction_year" : np.uint16,
	"extraction_type" : str,
	"extraction_type_group" : str,
	"extraction_type_class" : str,
	"management" : str,
	"management_group" : str,
	"payment" : str,
	"payment_type" : str,
	"water_quality" : str,
	"quality_group" : str,
	"quantity" : str,
	"quantity_group" : str,
	"source" : str,
	"source_type" : str,
	"source_class" : str,
	"waterpoint_type" : str,
	"waterpoint_type_group" : str
	}