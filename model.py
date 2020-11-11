import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

dataset = pd.read_csv('dataset-dummy.csv')
print(dataset.head())

X = dataset.drop('lable', axis = 1).values
y = dataset['lable'].values

# 10 Fold cross validation
def get_score(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)

lr = LogisticRegression()

kf = KFold(n_splits=10)
scores_logistic = []
for train_index, test_index in kf.split(X,y):
    X_train, X_test, y_train, y_test = X[train_index] , X[test_index] , y[train_index] , y[test_index]
    lr.fit(X_train,y_train)
    scores_logistic.append(lr.score(X_test,y_test))

print('10 Fold Acc Score')
print(scores_logistic)

y_pred = lr.predict(X_test)
print(classification_report(y_test,y_pred))

input = [[]]
input[0].extend([1.0,.0,.0,.0,1.0,.0,.0,1.0,.0,.0,1.0,1.0,.0,1.0,.0,.0,1.0,1.0,.0,1.0,.0,1.0,.0,.0,1.0,.0,.0,.0,.0,.0,.0,1.0,.0,.0])
print(lr.predict(input))
