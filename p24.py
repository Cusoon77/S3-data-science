import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([12,14,16,18,20,22,24])
ypoints = np.array([100,200,250,400,300,450,500])

plt.plot(xpoints,ypoints,marker='o',color='red',mec='g',mfc='g',linestyle='dotted')
plt.show()