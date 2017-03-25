from __future__ import print_function
import utm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lat_list = list()
lon_list = list()


def type_trans(x, y):
    for i1, i2 in zip(x, y):
        lat_list.append((utm.to_latlon(i1, i2, 51, northern=True))[0])
        lon_list.append((utm.to_latlon(i1, i2, 51, northern=True))[1])


# latitude
print((utm.to_latlon(358313.5884571367, 3454101.94532791, 51, northern=True))[0])
# longitude
print((utm.to_latlon(358313.5884571367, 3454101.94532791, 51, northern=True))[1])

df = (pd.read_csv('grid_data.csv'))

x_list = df['X'].values
y_list = df['Y'].values
type_trans(x_list, y_list)
df['Latitude'] = lat_list
df['Longitude'] = lon_list

df.to_csv('transfer.csv', index=False, header=True)
