from sys import argv
import csv
from house import House
from battery import Battery


class grid():
    """Class governing batteries and houses"""

    def __init__(self, nr):
        """initializes grid"""
        self.grid = self.create_grid(51, 51)
        self.houses = self.load_houses(
            f"Huizen&Batterijen/wijk{nr}_huizensortedhigh-low.csv")
        self.batteries = self.load_batteries(
            f"Huizen&Batterijen/wijk{nr}_batterijen.csv")

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

    def connect(self):
        for key in self.batteries:
            count = 1
            backcount = 150
            while self.batteries[key].filled < self.batteries[key].capacity:
                if count > 150 or backcount < 1:
                    break
                if self.houses[count].output + self.houses[backcount].output + self.batteries[key].filled < self.batteries[key].capacity:
                    if self.houses[count].pluggedin is not False:
                        count += 1
                    elif self.houses[backcount].pluggedin is not False:
                        backcount -= 1
                    else:
                        self.batteries[key].connected.append(self.houses[count])
                        self.batteries[key].connected.append(self.houses[backcount])
                        self.batteries[key].filled += self.houses[count].output + self.houses[backcount].output
                        self.houses[count].pluggedin = self.batteries[key]
                        self.houses[backcount].pluggedin = self.batteries[key]
                        count += 1
                        backcount -= 1
                else:
                    count += 1

                # if self.batteries[key].capacity - self.batteries[key].filled < self.houses[150].output:
                #     break
                # if self.houses[count].output + self.batteries[key].filled < self.batteries[key].capacity and self.houses[count].pluggedin is False:
                #     self.batteries[key].connected.append(self.houses[count])
                #     self.batteries[key].filled += self.houses[count].output
                #     self.houses[count].pluggedin = self.batteries[key]

        for key in self.batteries:
            print(self.batteries[key].filled)
            for house in self.batteries[key].connected:
                print(house)

        for house in self.houses:
            print(self.houses[house].pluggedin)


if __name__ == "__main__":
    if len(argv) == 2:
        if argv[1] == '1' or argv[1] == '2' or argv[1] == '3':
            grid = grid(argv[1])
            grid.connect()
    else:
        print("not correct input")
