import pandas as pd

from sklearn.cluster import KMeans

data = pd.read_csv("Iris.csv")

print(data.head())

print()

x = data.iloc[:,:4]

print(x.head())

print()

km = KMeans(n_clusters=3,n_init=10,random_state=42)

print(km.fit(x))

print()

y=km.predict(x)

print(y)

print()

centroid = km.cluster_centers_

print(centroid)