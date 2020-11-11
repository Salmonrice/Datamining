import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression

class Output():

    def __init__(self, friend , price , utilization , exclusive , cheaper , anticheat , problem , longterm , service , spend , gender , year):
        self.lr = LogisticRegression()
        self.friend = friend
        self.price = price
        self.utilization = utilization
        self.exclusive = exclusive
        self.cheaper = cheaper
        self.anticheat = anticheat
        self.problem = problem
        self.longterm = longterm
        self.service = service
        self.spend = spend
        self.gender = gender
        self.year = year
        self.output = ''

    def train(self):
        dataset = pd.read_csv('dataset-dummy.csv')
        print(dataset.head())

        X = dataset.drop('lable', axis=1).values
        y = dataset['lable'].values

        kf = KFold(n_splits=10)
        scores_logistic = []
        for train_index, test_index in kf.split(X, y):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
            self.lr.fit(X_train, y_train)
            scores_logistic.append(self.lr.score(X_test, y_test))

    def pred(self):
        input =[[]]

        if self.friend == 'yes':
            input[0].extend([1,0])
        else:
            input[0].extend([0,1])

        if int(self.price) <= 5000 :
            input[0].extend([0,0,0,1,0])
        elif 5001 <= int(self.price) <= 8000:
            input[0].extend([0,0,0,0,1])
        elif 8001 <= int(self.price) <= 11000:
            input[0].extend([0,1,0,0,0])
        elif 11001 <= int(self.price) <= 14000:
            input[0].extend([0,0,1,0,0])
        elif int(self.price) >= 14001:
            input[0].extend([1,0,0,0,0])

        if self.utilization == 'yes':
            input[0].extend([1,0])
        else:
            input[0].extend([0,1])

        if self.exclusive == 'yes':
            input[0].extend([1,0])
        else:
            input[0].extend([0,1])

        if self.cheaper == 'yes':
            input[0].extend([1,0])
        else:
            input[0].extend([0,1])

        if self.anticheat == 'yes':
            input[0].extend([1,0])
        else:
            input[0].extend([0,1])

        if self.problem == 'yes':
            input[0].extend([1,0])
        else:
            input[0].extend([0,1])

        if self.longterm == 'yes':
            input[0].extend([1,0])
        else:
            input[0].extend([0,1])

        if self.service == 'yes':
            input[0].extend([1,0])
        else:
            input[0].extend([0,1])

        if self.gender == 'male':
            input[0].extend([1,0,0])
        elif self.gender == 'female':
            input[0].extend([0,1,0])
        else:
            input[0].extend([0,0,1])

        if self.year == '1':
            input[0].extend([0,0,0,0,1])
        elif self.year == '2':
            input[0].extend([0,1,0,0,0])
        elif self.year == '3':
            input[0].extend([0,0,1,0,0])
        elif self.year == '4':
            input[0].extend([1,0,0,0,0])
        else:
            input[0].extend([0,0,0,1,0])

        if int(self.spend) <= 500:
            input[0].extend([0,0,0,1,0])
        elif 501 <= int(self.spend) <= 1000:
            input[0].extend([0,0,1,0,0])
        elif 1001 <= int(self.spend) <= 1500:
            input[0].extend([0,1,0,0,0])
        elif 1501 <= int(self.spend) <= 2000:
            input[0].extend([0,0,0,0,1])
        else:
            input[0].extend([1,0,0,0,0])

        self.output = self.lr.predict(input)[0]

        return self.lr.predict(input)

