import csv
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.ticker as ticker
# import numpy as np
"""classes"""
from Classes.house import House
from Classes.battery import Battery
import os


class Grid():
    """Class governing batteries and houses"""

    def __init__(self, nr):
        """initializes grid"""

        batteryload = os.path.dirname(os.getcwd())+f"\\sunny_storage\\Data\\wijk{nr}_batterijen.csv"
        housesload = os.path.dirname(os.getcwd())+f"\\sunny_storage\\Data\\wijk{nr}_huizen.csv"

        self.grid = self.create_grid(51, 51)
        self.houses = self.load_houses(housesload)
        self.batteries = self.load_batteries(batteryload)

    def create_grid(self, x, y):
        """create a grid to put objects"""

        grid = [[[] for x in range(0, x)] for y in range(0, y)]
        return grid

    def load_houses(self, file):
        """Loads in houses from csv"""

        # create dictionary
        houses = {}
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=',')
            for row in enumerate(reader):
                id = row[0]
                posx = int(row[1][0])
                posy = int(row[1][1])
                output = float(row[1][2])

                # Make house object with id as key
                house = House(id, posx, posy, output)
                houses[id] = house

                # Add house to grid
                self.grid[posy][posx] = houses[id]

        return houses

    def load_batteries(self, file):
        """Loads in batteries from csv"""

        batteries = {}
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=',')
            for row in enumerate(reader):
                id = row[0]
                posx = int(row[1][0])
                posy = int(row[1][1])
                capacity = float(row[1][2])

                # Make battery object with id as key
                battery = Battery(id, posx, posy, capacity)
                batteries[id] = battery

                # Add battery to the grid
                self.grid[posy][posx] = batteries[id]

        return batteries

    def Distancearr(self, b, h):
        """
        Gives manhattan distance for every combination of battery and house
        format: [for every house[(mhdistance, key of battery), ...]]
        """
        dist = []
        # lowbprice = 0
        for house in h:
            dist.append([])
            for batt in b:
                # manhattan distance calculation |x1 - x2| + |y1 - y2|
                manhat = abs(b[batt].posx - h[house].posx) + \
                         abs(b[batt].posy - h[house].posy)
                dist[house].append((manhat, batt))
            dist[house] = sorted(dist[house])
            # lowbprice += dist[house][0][0] * 9
        distdict = {}
        for nr in h:
            distdict[nr] = {}
            for batt in dist[nr]:
                distdict[nr][batt[1]] = batt[0]
        return dist, distdict
