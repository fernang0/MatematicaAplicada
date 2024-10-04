from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def s(x):
    return -1.6*x**2+1.3*x+141.3;

def r(x):
    return 1.4*x**2-5.6*x+12.6;

def zero(x):
    return s(x)-r(x);

def u(x):
    return 150*x+100;

def d(t):
    return 50*np.exp(0.3*t);
def zerod(x):
    return d(x)-551;


def m(x):
    return x**3-4*x**2+5*x

def c(x):
    return (50*x+200);

def s(n):
    return 2*n**2+3*n+5;
def zeros(n):
    return s(n)-500


horas = np.array([5,10,15,20]);
productividad = np.array([50,80,110,140]);

pendiente, intercepto = np.polyfit(horas, productividad, 1)
def produc(x):
    return 6*x+20;

def i(x):
    return 50*x+0.5*x**2;
def c(x):
    return 10*x+450;
def zeroic(x):
    return i(x)-c(x);
print(fsolve(zeroic, 0))

x = np.arange(0, 15, 1)
plt.plot(x, i(x), label="i(x)")
plt.plot(x, c(x), label="c(x)", color="red")
plt.grid()
plt.legend()
plt.show()