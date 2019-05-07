from sys import argv
from Algorithms.averagefit import Averagefit
from Algorithms.decreasingfirstfit import Decreasingfirstfit
from Algorithms.greedy import Greedy
from Algorithms.bfs import bfs
from Algorithms.astar import astar
from Algorithms.dfs import dfs
from Algorithms.randclimber import Randclimber
from Classes.thegrid import Grid
from Classes.node import Node
from Classes.node2 import Noot
from Algorithms.hillclimber import hillclimber
from Algorithms.random import random_alg
from Algorithms.battery_optimization import battery_optimization
from Helper_algorithms.price_calc import price_calc
from Helper_algorithms.visualize import visualize
from Helper_algorithms.write_to_csv import write_to_csv


if __name__ == "__main__":
    if len(argv) == 2:
        if argv[1] == '1' or argv[1] == '2' or argv[1] == '3' or \
                argv[1] == '4' or argv[1] == '5':
            grid = Grid(argv[1])
            print("""which algorithm to execute:
choices:
    random
    first-fit
    average-fit
    greedy
    breadth-first
    A-star
    depth-first
    hillclimber
    randclimber""")
            command = (input("> ")).upper()
            command2 = "no"
            command3 = "no"
            if command == "RANDOM":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                random_alg(distdict, grid.batteries, grid.houses)
                price = price_calc(grid.batteries, distdict)
                print(price)
                visualize(grid.batteries, grid.houses)
            elif command == "FIRST-FIT":
                Decreasingfirstfit(grid, grid.batteries, grid.houses)
                visualize(grid.batteries, grid.houses)
            elif command == "AVERAGE-FIT":
                Averagefit(grid, grid.batteries, grid.houses)
                visualize(grid.batteries, grid.houses)
            elif command == "GREEDY":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                Greedy(dist, grid.batteries, grid.houses)
                price = price_calc(grid.batteries, distdict)
                print(price)
                visualize(grid.batteries, grid.houses)
                # grid.savefig('hallo.png') # plus 1 voor elke run?
            elif command == "BREADTH-FIRST":
                node = Node()
                best = Node()
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                # Only use this if greedy gives a allowed solution
                best.price = Greedy(dist, grid.batteries, grid.houses)
                bfs(node, grid.batteries, grid.houses, distdict, best)
                visualize(grid.batteries, grid.houses)
            elif command == "A-STAR":
                # node = Noot()
                # dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                # start = (3,4) # huis randomly gepakt
                # goal = (18,34) # batt randomly gepakt
                # astar(start, goal, dist)
                # visualize(grid.batteries, grid.houses)
                print("not available at the moment!")
            elif command == "DEPTH-FIRST":
                node = Node()
                best = Node()
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                best.price = 700000
                dfs(node, grid.batteries, grid.houses, distdict, best)
                visualize(grid.batteries, grid.houses)
            elif command == "HILLCLIMBER":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                print("""what is the base?
    choices:
        random
        greedy
        """)
                command2 = (input("> ")).upper()
                if command2 == "RANDOM":
                    random_alg(distdict, grid.batteries, grid.houses)
                    hillclimber(dist, distdict, grid.batteries, grid.houses)
                    price = price_calc(grid.batteries, distdict)
                    print(price)
                    visualize(grid.batteries, grid.houses)
                elif command2 == "GREEDY":
                    Greedy(dist, grid.batteries, grid.houses)
                    hillclimber(dist, distdict, grid.batteries, grid.houses)
                    price = price_calc(grid.batteries, distdict)
                    print(price)
                    visualize(grid.batteries, grid.houses)
                else:
                    print("invalid command")
                print("""Do you want to optimize the location of the batteries with hillclimber?
            Optimize
            no optimize
            """)
                command3 = (input("> ")).upper()
                if command3 == "OPTIMIZE":
                    dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                    battery_optimization(grid.batteries)
                    dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                    price = price_calc(grid.batteries, distdict)
                    print(price)
                    visualize(grid.batteries, grid.houses)
                elif command == "NO OPTIMIZE":
                    print("nothing")
            elif command == "RANDCLIMBER":
                print("Choose number of repetitions")
                repetitions = int(input("> "))
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                price = Greedy(dist, grid.batteries, grid.houses)
                initial = Node()
                initial.fillnode(grid.batteries, grid.houses, price)
                price = Randclimber(initial, price, repetitions, distdict, grid.batteries, grid.houses)
            else:
                print("invalid command")

            print("""do you want to save your run?
            Options:
            Yes
            No
            """)
            if (input("> ")).upper() == "YES":
                algorithm = (command + " --> " + command2 + " --> " + command3)
                write_to_csv(argv[1], algorithm, price, grid.batteries, grid.houses)

        else:
            print("neigborhood doesn't exist")
    else:
        print("not correct input")
