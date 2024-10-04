import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,6,0.01);
y = 120*x+2000;

plt.plot(x,y)
plt.grid(True)
plt.axis([0,6,0,2800])
plt.show();
