# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:22:06 2022

@author: alexc
"""

import pandas as pd
import pickle
import os
from sklearn.metrics import precision_recall_fscore_support

#carreguem el test
os.getcwd()
test_data = pd.read_csv('test_data.csv', names=['n', 'url', 'class'], delimiter=',', na_filter=False)
#test_data = pd.read_csv('url_classification.csv', names=['n', 'url', 'class'], delimiter=',', na_filter=False)
X_test=test_data['url']
y_test=test_data['class']

filename = 'multinomialNB_trained.sav'
model = pickle.load(open(filename, 'rb'))
y_pred=model.predict(X_test)
result = precision_recall_fscore_support(y_test, y_pred, average='weighted')
print("Precision: "+str(result[0]))
print(result)





