from __future__ import print_function
from lshash import LSHash
import pandas as pd
import numpy as np
import time

time_type = "%Y-%m-%d %H:%M:%S"
timeMe = time.strptime('2015-04-01 14:04:50', time_type)
print(time.mktime(timeMe))
