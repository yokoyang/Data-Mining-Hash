from __future__ import print_function
from lshash import LSHash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lsh = LSHash(6, 8)
lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
lsh.index([3, 4, 5, 6, 7, 8, 9, 10])

lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
print (lsh.query([1, 2, 3, 4, 5, 6, 7, 7]))

print (len(lsh.query([1, 2, 3, 4, 5, 6, 7, 7])))
