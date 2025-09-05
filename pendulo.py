import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,2*np.pi,200, endpoint=True)
w=1
x_1 = np.sin(w*t)
x_2 = np.sin(2*w*t)
x_3 = x_1 + x_2

plt.plot(t,x_1, color = "red")
plt.plot(t,x_2, color = "green")
plt.plot(t,x_3, color = "blue")
plt.grid()

plt.show()