import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
y = x**2 + 2*x + 5 + np.random.normal(0,1,100)

#fit poynomial
p =np.polyfit(x,y,2)
pfit = np.polyval(p,x)

plt.figure()
plt.plot(x,y,'ro', label = 'Raw Data')
plt.plot(x,pfit, 'b', label = 'Polynomial Fit')
plt.legend(loc='best')


