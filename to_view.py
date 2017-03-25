from __future__ import print_function
from lshash import LSHash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors


class MapWriter(object):
    def __init__(self, indexes, input_filename, output_filename):
        self.indexes = indexes
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.rgb_table = ['#EEB422', '#9B30FF', '#A0522D', '#7CFC00', '#3A5FCD', '#218868']

    def write_more(self):
        df = (pd.read_csv(self.input_filename))
        temp = df.groupby(df['Tid'])
        f2 = open(self.output_filename, 'w')
        f2.write(
            'function initMap() {var map = new google.maps.Map(document.getElementById(\'map\'), {zoom: 13,center: {lat: 31.2283979866, lng: 121.462497501},mapTypeId: google.maps.MapTypeId.TERRAIN});')
        f2.write('\n')
        for c, p in enumerate(self.indexes):
            for q in p:
                self.write_number(q, f2, temp, self.rgb_table[c])

        f2.write('}')
        f2.close()

    def write_2(self):
        df = (pd.read_csv(self.input_filename))
        temp = df.groupby(df['Tid'])
        f2 = open(self.output_filename, 'w')
        f2.write(
            'function initMap() {var map = new google.maps.Map(document.getElementById(\'map\'), {zoom: 13,center: {lat: 31.2283979866, lng: 121.462497501},mapTypeId: google.maps.MapTypeId.TERRAIN});')
        f2.write('\n')
        colour = self.rgb_table[-1]
        for p in self.indexes:
            self.write_number(p, f2, temp, colour)

        f2.write('}')
        f2.close()

    def write_number(self, number, f2, temp, colour):
        f2.write('var flightPlanCoordinates')
        f2.write(str(number))
        f2.write(' = [')
        for i, j in temp:
            if i == number:
                latitude = j['Latitude'].values[:]
                longitude = j['Longitude'].values[:]
                for la, lo in zip(latitude, longitude):
                    f2.write("{lat: ")
                    f2.write(str(la))
                    f2.write(", lng: ")
                    f2.write(str(lo))
                    f2.write("},\n")
                break
        f2.write('];\n')
        f2.write('var flightPath')
        f2.write(str(number))
        f2.write(' =  new google.maps.Polyline({ path: flightPlanCoordinates')
        f2.write(str(number))
        f2.write(',geodesic: true,strokeColor: \'' + str(colour) + '\',strokeOpacity: 1.0,strokeWeight: 5});')
        f2.write('flightPath' + str(number) + '.setMap(map);')


# hash size = 10
# w = MapWriter([[15, 33, 904, 371], [250, 559, 895, 78, 928, ],
#                [480, 916, 845, 219, 834, 320],
#                [690, 834, 52, 154, 845, 699, 670, 615],
#                [900, 580, 60, 1, 206, 664]],
#               'transfer.csv', 'LSHash_Result_2.js')

# hash size = 11
# w = MapWriter([[15, 946, 597, 544, 115, 51], [250, 128, 351, 194, 93],
#                [480, 316, 299, 31, 261, 2, 722, 358],
#                [690, 446, 615, 488, 927, 479, 998, 872, 481, 772],
#                [900, 203, 189, 847, 154, 756, 670]],
#               'transfer.csv', 'LSHash_Result_2.js')
# w = MapWriter([333, 937, 369, 987],
#               'transfer.csv', 'LSHash_Result_2.js')
# w = MapWriter([15, 33, 904, 371, 525, 603, 714],
#               'transfer.csv', 'LSHash_Result_2.js')
w = MapWriter([[15], [250],
               [480],[690],[900]],
              'transfer.csv', 'LSHash_Result_2.js')

# un pca 10
# w = MapWriter([[15, 730, 564, 114, 196], [250, 604, 459, 647, 7],
#                [480, 953, 786, 45, 51, 138],
#                [690, 369, 914, 230, 491, 118, 88],
#                [900, 707, 707, 155, 789, 457, 321]],
#               'transfer.csv', 'LSHash_Result_2.js')

# un pca 11
# w = MapWriter([[15, 567, 911, 162, 717], [250, 40, 145, 810, 230],
#                [480, 707, 92, 331, 368, 152],
#                [690, 968, 45, 954, 611, 918],
#                [900, 301, 464, 281, 698]],
#               'transfer.csv', 'LSHash_Result_2.js')
# knn
# w = MapWriter([[15, 206, 949, 624, 987], [250, 243, 742, 88, 841],
#                [480, 551, 95, 963, 60],
#                [690, 67, 446, 653, 980],
#                [900, 580, 60, 1, 688]],
#               'transfer.csv', 'LSHash_Result_2.js')
w.write_more()
# w.write_2()
