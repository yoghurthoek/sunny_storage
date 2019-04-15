from sys import argv
from Algorithms.averagefit import Averagefit
import csv
from Classes.thegrid import Grid

if __name__ == "__main__":
    if len(argv) == 2:
        if argv[1] == '1' or argv[1] == '2' or argv[1] == '3':
            grid = Grid(argv[1])
            print("""which algorithm to execute:
choices:
    random
    first-fit
    average-fit""")
            command = (input("> ")).upper()
            if command == "RANDOM":
                grid.random(grid.batteries, grid.houses)
            elif command == "FIRST-FIT":
                # grid.connect()
                grid.decreasingfirstfit(grid.batteries, grid.houses)
            elif command == "AVERAGE-FIT":
                Averagefit.averagefit(grid)
            else:
                print("invalid command")

        else:
            print("neigborhood doesn't exist")
    else:
        print("not correct input")

    # hier nog prompten voor welk algoritme je wilt kiezen
