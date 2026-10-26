import numpy as np
import matplotlib.pyplot as plt

y1 = [22,30,35,35,26]
y2 = [25,32,30,35,29]

x_labels = ['g1','g2','g3','g4','g5']
x1 = np.arange(5)
width = 0.40

plt.bar(x1-0.2,y1,color="green",width=width,label='men')
plt.bar(x1-0.2,y2,color="red",width=width,label='women')

plt.xticks(x1,x_labels)

plt.xlabel("person")
plt.ylabel("scores")
plt.legend()

plt.title("scores by group and gender")
plt.show()