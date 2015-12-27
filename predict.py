"""predict.py: Main script for prediction initiation."""

import numpy as np
import data_helper
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import config

labels = data_helper.readTrainingLabels()

train_data = data_helper.readData(config.TRAINING_SET_VALUES)


X_train, X_cross_validate, y_train, y_cross_validate = train_test_split(train_data, labels, test_size=0.5, random_state=42)

iris = load_iris()

# features = [5, 32, 6, 33, 7, 10, 1, 3, 15]
num_features = X_train.shape[1]

#create the random forest model
forest = RandomForestClassifier(n_estimators = 10)

#fit the RandomForestClassififer on the training data
forest.fit(X_train, y_train)

#predict the labels for the cross validation set
preds = forest.predict(X_cross_validate)

print(pd.crosstab(y_cross_validate, preds, rownames=['actual'], colnames=['preds']))
print("Cross Validation Accuracy : ",accuracy_score(y_cross_validate,preds))



# Run predictor on test data for submission

test_data = data_helper.readData(config.TEST_SET_VALUES)
x = forest.predict(test_data)
test_data['status_group'] = 0
test_data.status_group = x


#save data to csv
data_helper.saveData(test_data,config.OUTPUT_PREDICTIONS,['status_group'])

importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# plt.figure()
# plt.title("Feature importances")
# plt.bar(range(num_features), importances[indices],
#        color="r", yerr=std[indices], align="center")
# plt.xticks(range(num_features), indices)
# plt.xlim([-1, num_features])
# plt.show()