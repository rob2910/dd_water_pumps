# dd_water_pumps
Project for my submission of the DataDriven.org Pump It Up competition - http://www.drivendata.org/competitions/7/

## Methods

### Random Forest

I made use of scikit-learn's RandomForestClassifier model.

## Requirements

Please sign up for the competition and download necessary .csv data files from http://www.drivendata.org/competitions/7/data/ and place the files under the following names in the data directory.

```
./data/test_test_values.csv
./data/training_set_values.csv
./data/training_set_labels.csv
```

You will also need the following python modules which can be installed via pip.

* pandas
* numpy
* scikit-learn
* matplotlib (optional for graphs)

## Documentation

### predict.py

This is the main invocation script for the predictor.

Usage : 
```
python predict.py
```

### config.py

Holds constants and configuration data.

### data_helper.py

Helper module for reading and processing data.

### pre_process.py #

Helper module for pre-processing data.

## Current Score

77.9