import matplotlib.pyplot as plt
from numpy import cos, arange
t = arange(0, 5.0, 0.01)
x = arange(0, 5.0, 0.01)
plt.plot(t, cos(x**2)/x)
plt.show() 
