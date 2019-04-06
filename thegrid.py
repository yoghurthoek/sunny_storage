from sys import argv
import csv
from house import House
from battery import Battery

class grid():
    """Class governing batteries and houses"""

    def __init__(self, nr):
        self.grid = self.create_grid(51,51)
        self.houses =self.load_houses(f"Huizen&Batterijen/wijk{nr}_huizen.csv")
        self.batteries =self.load_batteries(f"Huizen&Batterijen/wijk{nr}_batterijen.txt")

    def create_grid(self, x, y):
        """create a grid to put objects"""
        grid = [[[] for x in range(0,51)] for y in range (0, 51)]
        return grid

    def load_houses(self, file):
        """Loads in houses from csv"""
        # create dictionary
        houses = {}
        with open("Huizen&Batterijen/wijk1_huizen.csv", "r") as f:
            reader = csv.reader(f, delimiter=',')
            for row in enumerate(reader, 1):
                id = row[0]
                posx = int(row[1][0])
                posy = int(row[1][1])
                output = row[1][2]

                #Make house object with id as key
                house = House(id, posx, posy, output)
                houses[id] = house

                # Add house to grid
                grid[posy][posx] = houses[id]

        # voorbeeld voor indexen. Eerst y daarna x. Zou huis nr 0 moeten geven.
        print(grid[47][34])


    def load_batteries(self, file):
        """Loads in batteries from txt"""
        batteries = {}
        with open("Huizen&Batterijen/wijk2_batterijen.csv", "r") as f:
                reader = csv.reader(f, delimiter=',')
                for row in enumerate(reader, 1):
                    id = row[0]
                    posx = int(row[1][0])
                    posy = int(row[1][1])
                    capacity = row[1][2]

                    # Make battery object with id as key
                    battery = Battery(id, posx, posy, capacity)
                    batteries[id] = battery

                    # Add battery to the grid
                    grid[posy][posx] = batteries[id]

        print(batteries[0])

if __name__ == "__main__":
        if len(argv) == 2:
            if argv[1] == 1 or argv[1] == 2 or argv[1] == 3:
                grid = grid(argv[1])
