#zestaw A, grupa I/2



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {"a": np.random.randint(0, 100, 100),
        "b": np.random.randint(0, 100, 100),
        "c": np.random.randint(0, 8, 100)}
data["d"] = np.abs(data["a"]-data["b"])
df = pd.DataFrame(data)
wykres = sns.relplot(data=df, x="a", y="b", hue="c", palette="Set2", size="d", legend=True)
wykres.fig.set_size_inches(10, 10)
wykres.set(title = " Wykres punktowy")
plt.show()
