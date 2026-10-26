import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
data = pd.read_csv('Iris.csv')
print("first few rows of the dataset:")
print(data.head())

x=data.iloc[:,:4]
y=data.iloc[:,-1]
print("\nfeatures data(first 5 rows):")
print(x.head())
print("\ntesting features(first 5 rows):")
print(y.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)

print("\ntesting features(first 5 rows):")
print(x_train.head())
print("\ntesting features(first 5 rows):")
print(x_test.head())

sc = StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
classifier=KNeighborsClassifier(n_neighbors=5)
print(classifier.fit(x_train,y_train))

y_pred=classifier.predict(x_test)
print("\n array" ,y_pred)
print("\n actual label:" ,y_test)

cm=confusion_matrix(y_test,y_pred)
ac=accuracy_score(y_test,y_pred)
print("\n confusion matrix:",cm)
print("\n accuracy:",ac)