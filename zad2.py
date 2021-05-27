#zestaw A, grupa I/2



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = np.arange(0, 100, 0.05)
y1 = x1**2-4*x1+2
x2 = np.arange(0, 100, 0.2)
y2 = x2**3-2**x2-4*x2

plt.subplot(1, 3, 1)
plt.xlim([0, 10])
plt.xticks([0, 5, 10])
plt.ylim([-10, 50])
plt.plot(x1, y1, "-", label="x^2-4x+2")
plt.title("Pierwszy wykres")
plt.legend(loc="lower left")
plt.grid()

plt.subplot(1, 3, 2)
plt.xlim([0, 10])
plt.xticks([0, 2, 4, 6, 8, 10])
plt.ylim([-99, 249])
plt.plot(x2, y2, "g.", label="x^3-2^x-4x")
plt.title("Drugi wykres")
plt.legend(loc="lower center")
plt.grid()

plt.subplot(1, 3, 3)
plt.xlim([0, 10])
plt.xticks([0, 2, 4, 6, 8, 10])
plt.ylim([-10, 50])
plt.plot(x1, y1, "-", label="x^2-4x+2")
plt.plot(x2, y2, "g.", label="x^3-2^x-4x")
plt.title("Trzeci wykres")
plt.legend(loc="upper center")
plt.grid()

plt.show()