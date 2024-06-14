import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Defino la función a ajustar
def fun(x,a,b):
    return ( b * 2 * np.sqrt(abs(a) * x) / ( abs(a) + x ) ) 
    #return ( b * 2 * np.sqrt(a * x) / ( a + x ) ) 

# Cargar los datos a ajustar
local = np.loadtxt('local.dat', usecols = (0,1) )

# Graficar los datos
plt.plot(local[:,0], local[:,1], "-", label = "Datos")

# Ajuste
popt, pcov = curve_fit(fun, local[:,0], local[:,1])

print("popt", popt)
print("pcov", pcov)

# Graficar ajuste
x = np.arange(0.001, 0.5,0.001)
plt.plot(x, fun(x, *popt), "-", label = "función")

# Etiquetas y leyendas
plt.xlabel("Energy [MeV]")
plt.ylabel("L(E)")
plt.legend()

# Muestra de información
plt.savefig("fit.pdf",format="pdf")
plt.show()
