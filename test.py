import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data.csv')


print(dataset.head())

X = dataset.drop('class', axis = 1).values
y = dataset['class'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,random_state=101)

print(X_test[1])

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(C=1.0, random_state=1)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

print(classifier.predict([[6,148,72,35,0,33.6,0.627,50]]))

print(confusion_matrix(y_test, lr_pred))
print(classification_report(y_test, lr_pred))