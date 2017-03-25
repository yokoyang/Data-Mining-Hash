from __future__ import print_function
from lshash import LSHash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# const value here!
rectangle_x1 = 346000
rectangle_x2 = 362800
rectangle_y1 = 3448600
rectangle_y2 = 3463800
t_col = 840
t_row = 760


################################

def which_map(x, y):
    my_list = list()
    for i1, i2 in zip(x, y):
        diff_x = int((i1 - rectangle_x1) / 20)
        diff_y = int((i2 - rectangle_y1) / 20)
        pos = (t_row - 1 - diff_y) * t_col + diff_x
        my_list.append(pos)
    return my_list


##################################
df = (pd.read_csv('Traj_1000_SH_UTM'))
x_list = df['X'].values
y_list = df['Y'].values
my_list = which_map(x_list, y_list)
grid = list()
df['Grid'] = my_list
new_list = list(set(my_list))
print (len(new_list))
df.to_csv('grid_data.csv', index=False, header=True)
