import matplotlib.pyplot as plt;
import numpy as np;

x = np.arange(0,2, 0.0001);

plt.plot(x, x**3,label="Cubo", color='red');
plt.legend()
plt.show();
