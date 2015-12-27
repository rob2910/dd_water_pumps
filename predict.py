"""predict.py: Main script for prediction initiation."""

import numpy as np
import read_data
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
import config

labels = read_data.readTrainingLabels()

train_data = read_data.readData(config.TRAINING_SET_VALUES)

X_train, X_test, y_train, y_test = train_test_split(train_data, labels, test_size=0.33, random_state=42)

# test_data = read_data.readData(config.TEST_SET_VALUES)

iris = load_iris()

features = ['amount_tsh','funder','population']
clf = RandomForestClassifier(n_jobs=2)
y, _ = pd.factorize(y_train['status_group'])

y_test, _ = pd.factorize(y_test['status_group'])

clf.fit(X_train[features], y)

preds = clf.predict(X_test[features])

pd.crosstab(y_test, preds, rownames=['actual'], colnames=['preds'])