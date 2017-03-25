from __future__ import print_function
from lshash import LSHash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold

sel = VarianceThreshold(threshold=0.002)
df = (pd.read_csv('grid_data.csv'))
sort_grid = df['Grid'].drop_duplicates().tolist()
sort_grid.sort()
sort_grid = np.array(sort_grid)
temp = df.groupby(df['Tid'])
t_cell = 44107
t_trace = 1000
f = open('KNN_Result.txt', 'w')

big_metric = np.zeros([t_trace, t_cell])
for i, j in temp:
    grid_t = j['Grid'].values[:]
    for k in grid_t:
        my_index = (np.argwhere(sort_grid == k))
        if my_index > 0:
            big_metric[i - 1][my_index] = 1

pca = PCA(n_components=500)
select_metric = sel.fit_transform(big_metric)
metric = pca.fit_transform(select_metric)
ks = [1, 2, 3, 4, 5]
for k in ks:
    nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(metric)
    distances, indices = nbrs.kneighbors(metric)
    trade = [15, 250, 480, 690, 900]
    f.write('n_neighbors=' + str(k) + '\n')
    f.write('-------------------------- ' + '\n')

    for t in trade:
        for i in indices[t - 1]:
            f.write(str(i + 1) + ', ')
        f.write('\n')
        f.write('Distances:\n')
        f.write('[')
        for d1 in distances[t - 1]:
            f.write(str(d1) + ', ')
        f.write(']')
        f.write('\n')
    f.write('\n')
f.close()
