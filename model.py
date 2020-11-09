import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv('dataset-dummy.csv')
print(dataset.head())

X = dataset.drop('lable', axis = 1).values
y = dataset['lable'].values

# K Fold
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

print(scores_logistic)


print(lr.predict([[1.0,.0,.0,.0,1.0,.0,.0,1.0,.0,.0,1.0,1.0,.0,1.0,.0,.0,1.0,1.0,.0,1.0,.0,1.0,.0,.0,1.0,.0,.0,.0,.0,.0,.0,1.0,.0,.0]]))
