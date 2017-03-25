from __future__ import print_function
from lshash import LSHash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold

t_cell = 44107
t_trace = 1000
hash_size = [10, 11, 12, 13, 14, 15]
trade = [15, 250, 480, 690, 900]
df = (pd.read_csv('transfer.csv'))
sort_grid = df['Grid'].drop_duplicates().tolist()
sort_grid.sort()
sort_grid = np.array(sort_grid)
temp = df.groupby(df['Tid'])

dimension = 200
f = open('pca_LSHash_Result.txt', 'w')
pca = PCA(n_components=dimension)
sel = VarianceThreshold(threshold=0.001)


def findByRow(mat, row):
    return np.where((mat == row).all(1))[0]


big_metric = np.zeros([t_trace, t_cell])
for i, j in temp:
    grid_t = j['Grid'].values[:]
    for k in grid_t:
        my_index = (np.argwhere(sort_grid == k))
        if my_index > 0:
            big_metric[i - 1][my_index] = 1

f.write("Distance Func Hamming")
f.write('\n')
f.write('\n')
f.write('############################')
f.write('\n')

select_metric = sel.fit_transform(big_metric)
metric = pca.fit_transform(select_metric)

for u in range(6):
    lsh = LSHash(int(hash_size[u]), dimension)
    for i in range(1000):
        lsh.index(metric[i])
    for v in trade:
        f.write("Hash_size: ")
        f.write(str(int(hash_size[u])))
        f.write('\n')
        f.write("As for Tid ")
        f.write(str(v))
        f.write('\n')
        f.write('--------------------------------')
        f.write('\n')

        row = lsh.query(metric[v - 1], distance_func="hamming")
        for g in row:
            f.write("Index ")
            f.write(str(1 + (findByRow(metric, list(g[0])))[0]))
            f.write(" Distance is :")
            f.write(str(g[1]))
            f.write('\n')

f.write("Distance Func Euclidean")
f.write('\n')
f.write('\n')
f.write('############################')
f.write('\n')

for u in range(6):

    lsh = LSHash(int(hash_size[u]), dimension)
    for i in range(1000):
        lsh.index(metric[i])
    for v in trade:
        f.write("Hash_size: ")
        f.write(str(int(hash_size[u])))
        f.write('\n')
        f.write("As for Tid ")
        f.write(str(v))
        f.write('\n')
        f.write('--------------------------------')
        f.write('\n')

        row = lsh.query(metric[v - 1], distance_func="euclidean")
        for g in row:
            f.write("Index ")
            f.write(str(1 + (findByRow(metric, list(g[0])))[0]))
            f.write(" Distance is :")
            f.write(str(g[1]))
            f.write('\n')

f.close()
