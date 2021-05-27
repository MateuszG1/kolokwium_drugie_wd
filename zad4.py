#zestaw A, grupa I/2



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a = pd.read_csv("cars.csv", header=0, sep=";")
df = pd.DataFrame(a)
