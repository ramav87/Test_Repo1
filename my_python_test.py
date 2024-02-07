import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
y = x**2 + x*3 +5

plt.figure()
plt.plot(x,y)
