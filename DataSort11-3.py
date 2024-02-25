import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('data11-3.xlsx')

arr_df = df.to_numpy()

plt.plot(df.Count, df.AttitudePitch)
plt.xlabel("Time")
plt.ylabel("AttitudePitch")
plt.title("Alitutde Pitch vs. Count")
plt.show()