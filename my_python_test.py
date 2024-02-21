import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,200)
y = x**3 + x**2 + 5 

plt.figure()
plt.plot(x,y)
plt.show()