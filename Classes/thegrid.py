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
        housesload = os.path.dirname(os.getcwd())+f"\\sunny_storage\\Data\\wijk{nr}_huizensortedhigh-low.csv"

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
            for row in enumerate(reader, 1):
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
            for row in enumerate(reader, 1):
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

    def visualize(self, b):
        fig, ax = plt.subplots()

        # Use different colors depending on battery connection
        colors = ["r", "b", "g", "c", "m"]
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
            i += 1

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
