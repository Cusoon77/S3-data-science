import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

data = pd.read_csv("Iris.csv")
print(data.head())
print()

x = data.iloc[:,:4]
print(x.head())
print()
y = data.iloc[:,-1]
print(y.head())
print()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

classifier = DecisionTreeClassifier()
print(classifier)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print()

ac = accuracy_score(y_test, y_pred)
print("Accuracy:", ac)

plt.figure(figsize=(12,8))
tree.plot_tree(classifier)
plt.title("Decision Tree for Iris dataset")
plt.show()
