import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv('US_Population.csv')
plt.plot(dataset.Year, dataset.Population)

plt.title("US Population")
plt.xlabel("Year")
plt.ylabel("Population")

plt.show()