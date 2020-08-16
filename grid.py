
import numpy as np
import matplotlib.pyplot as plt



xvalues = np.array([0, 1, 2, 3, 4]);
yvalues = np.array([0, 1, 2, 3, 4]);


xx, yy = np.meshgrid(xvalues, yvalues)

plt.plot(xx, yy, marker='.', color='k', linestyle='none')
circle = plt.Circle( ( 0, 0 ), 1 )

print(xx)
print(yy)
plt.show()
