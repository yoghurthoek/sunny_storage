import csv

"""Classes"""
from Classes.house import House
from Classes.battery import Battery
import os


class Grid():
    """Class governing batteries and houses"""

    def __init__(self, nr):
        """initializes grid"""

        batteryload = os.path.dirname(os.getcwd()) + f"\\sunny_storage\\Data\\wijk{nr}_batterijen.csv"
        housesload = os.path.dirname(os.getcwd()) + f"\\sunny_storage\\Data\\wijk{nr}_huizen.csv"

        self.grid = self.create_grid(51, 51)
        self.houses = self.load_houses(housesload)
        self.batteries = self.load_batteries(batteryload)


    def create_grid(self, x, y):
        """create a grid to put objects"""

        grid = [[[] for x in range(0, x)] for y in range(0, y)]
        return grid


    def load_houses(self, file):
        """Loads in houses from csv"""

        houses = {}
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter=',')
            for row in enumerate(reader):
                id = row[0]
                posx = int(row[1][0])
                posy = int(row[1][1])
                output = float(row[1][2])

                house = House(id, posx, posy, output)
                houses[id] = house

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

                battery = Battery(id, posx, posy, capacity)
                batteries[id] = battery

                self.grid[posy][posx] = batteries[id]

        return batteries
