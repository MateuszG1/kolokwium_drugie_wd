#zestaw A, grupa I/2



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_csv("cars.csv", header=0, sep=";")
df = pd.DataFrame(a)
df_weight = df[df.Weight < 2200]
grouped = df_weight.groupby(["Model year"])
avg = grouped["Horsepower"].mean()

wykres = avg.plot.bar()
wykres.set_ylabel("Średnia moc silnika")
wykres.set_xlabel("Rok produkcji")
plt.title("Średnia moc silnika w latach produkcji")
plt.savefig("wykres.png")
plt.show()

