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

    def decreasingfirstfit(self, b, h):
        for nr in h:
            for key in b:
                if h[nr].output + b[key].filled < b[key].capacity:
                    b[key].connected.append(h[nr])
                    b[key].filled += h[nr].output
                    h[nr].pluggedin = b[key]
                    break

        for key in self.batteries:
            print(self.batteries[key].filled)
            # for house in self.batteries[key].connected:
            #     print(house)

        for house in self.houses:
            print(self.houses[house].pluggedin)

    def Distancearr(self, b, h):
        """
        Gives manhattan distance for every combination of battery and house
        format: [for every house[(mhdistance, key of battery), ...]]
        """
        dist = []
        for house in h:
            dist.append([])
            for batt in b:
                # manhattan distance calculation |x1 - x2| + |y1 - y2|
                manhat = abs(b[batt].posx - h[house].posx) + \
                         abs(b[batt].posy - h[house].posy)
                dist[house].append((manhat, batt))
            dist[house] = sorted(dist[house])

        return dist

    def visualize(self, b, h):
        fig, ax = plt.subplots()

        # Use different colors depending on battery connection
        colors = ["r", "b", "g", "gold", "m"]
        i = 0
        cmarker = Path([(-0.5, -0.5), (-0.5, 0.5), (0., 1.), (0.5, 0.5),
                        (0.5, -0.5), (-0.5, -0.5), ],
                       [Path.MOVETO, Path.LINETO, Path.LINETO,
                        Path.LINETO, Path.LINETO, Path.CLOSEPOLY, ])

        # Plot battery and connected houses, then go to next battery
        for k in b:
            ax.plot(b[k].posx, b[k].posy, color=colors[i],
                    marker='P', markersize=10, markeredgecolor='k')
            for house in b[k].connected:
                ax.plot(house.posx, house.posy, color=colors[i],
                        marker=cmarker, markersize=10)
                ax.plot([b[k].posx, house.posx], [b[k].posy, house.posy],
                        color=colors[i], linestyle=':', linewidth=1)
            i += 1

        # Plot unconnected houses if they are there
        for k in h:
            if h[k].pluggedin is False:
                ax.plot(h[k].posx, h[k].posy, color='k', marker=cmarker,
                        markersize=15)

        # Set grid limits
        ax.set_xlim((-1, 51))
        ax.set_ylim((-1, 51))

        # Set ticks for minor gridlines
        minorspace = ticker.MultipleLocator()
        ax.xaxis.set_minor_locator(minorspace)
        ax.yaxis.set_minor_locator(minorspace)

        # Set ticks for major gridlines
        majorspace = ticker.MultipleLocator(10)
        ax.xaxis.set_major_locator(majorspace)
        ax.yaxis.set_major_locator(majorspace)

        # Draw in gridlines
        ax.grid(b=True, which='major', linewidth=1.5)
        ax.grid(b=True, which='minor', linewidth=0.5)

        plt.show()
