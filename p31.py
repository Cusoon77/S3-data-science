from random import gauss

import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('Iris.csv')
print(data.head())
print()

x=data.iloc[:,:4]
print(x.head())
print()

y=data.iloc[:,-1]
print(y.head())
print()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
print(x_train.head())
print()
print(x_test.head())
print()

sc = StandardScaler()
sc.fit(x_train)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
classifier=GaussianNB()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print("array" ,y_pred)
print()
print(y_test)

cm=confusion_matrix(y_test,y_pred)
ac=accuracy_score(y_test,y_pred)
print("\n Confusion matrix:\n",cm)
print("\n Accuracy Score:",ac)