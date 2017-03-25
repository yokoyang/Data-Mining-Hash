from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = (pd.read_csv('transfer.csv'))
temp = df.groupby(df['Tid'])
for i, j in temp:
    latitude = j['Latitude'].values
    longitude = j['Longitude'].values
    plt.plot(latitude, longitude)

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()
