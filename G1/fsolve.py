#Calculo de una preimagen  a partir de una funcion y su imagen
#ejemplo el costo de la luz esta representada en funcion de los KWh ademas de un cargo fijo de 2000, la funcion seria la siguiente: 120*KWh+2000 = costo luz, pero tenemos la preimagen que seria lo que una persona pago por la luz, que seria $68000, loo que habria que hacer es despejar. 120*e+2000 = 68000
#En este caso se igualara la funcion a 0
import numpy as np
from scipy.optimize import fsolve
#La funcion para calcular el costo de la luz
def calculoLuz(kwh):
    return 120*kwh+2000;

#igualaremos la funcion a 0 para utilizar fsolve
def preimagen(kwh):
    return 120*kwh+2000-68000;

x = np.linspace(0,1000,2);
sol = fsolve(preimagen, x)
print(np.unique(sol))
