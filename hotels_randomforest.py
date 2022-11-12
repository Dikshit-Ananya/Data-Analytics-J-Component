# -*- coding: utf-8 -*-
"""hotels_randomforest

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PcgRtpAC2ZaQ-kaX6rCSQqmFDqQUwKnQ
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report, confusion_matrix
import pickle
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv("HOTELS.csv")
# print(data1.head())
#C = 'City'
#city = input('Enter a location (Mumbai, Goa, Delhi or Bangalore):')
#data = data1.loc[data1['Location'] == C]

data['Location'].replace(['Bengaluru', 'Delhi', 'Goa', 'Mumbai'], [1, 2, 3, 4], inplace = True)

X = data[['Location','Room category','Price','Rating']]
y = data[['Hotel Name']]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

c = RandomForestClassifier(n_estimators = 20, criterion = 'gini', random_state = 1, max_depth = 3)
c.fit(X_train, y_train)
pickle.dump(c,open("hp.pkl","wb"))
# y_pred = c.predict(X_test)
# print("Prediction: ",y_pred)

'''
y_pred1 = c.predict([[2,12972,8.9]])
print(y_pred1)

accuracy = round(accuracy_score(y_test,y_pred)*100, 2)
precision = round(precision_score(y_test,y_pred,average='micro')*100,2)
recall = round(recall_score(y_test,y_pred,average='micro')*100,2)
f1 = round(f1_score(y_test,y_pred,average='micro')*100,2)

print("\nAccuracy = ",accuracy)
print("Precision = ",precision)
print("Recall = ",recall)
print("F1 Score = ",f1)'''

