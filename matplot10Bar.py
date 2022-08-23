import numpy as np 
import matplotlib.pyplot  as plt

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y,color = 'red',width = 0.1)

plt.show()

#horizontal bar 
plt.barh(x,y,height = 0.5)

plt.show()
