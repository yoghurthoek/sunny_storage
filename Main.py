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
from Algorithms.hillclimber_batteries import hillclimber_batteries
from Helper_algorithms.price_calc import price_calc


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
            if command == "RANDOM":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                random_alg(distdict, grid.batteries, grid.houses)
                price = price_calc(grid.batteries, distdict)
                print(price)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "FIRST-FIT":
                Decreasingfirstfit(grid, grid.batteries, grid.houses)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "AVERAGE-FIT":
                Averagefit(grid, grid.batteries, grid.houses)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "GREEDY":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                Greedy(dist, grid.batteries, grid.houses)
                price = price_calc(grid.batteries, distdict)
                print(price)
                grid.visualize(grid.batteries, grid.houses)
                grid.savefig('hallo.png') # plus 1 voor elke run?
            elif command == "BREADTH-FIRST":
                node = Node()
                best = Node()
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                # Only use this if greedy gives a allowed solution
                best.price = Greedy(dist, grid.batteries, grid.houses)
                bfs(node, grid.batteries, grid.houses, distdict, best)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "A-STAR":
                # node = Noot()
                # dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                # start = (3,4) # huis randomly gepakt
                # goal = (18,34) # batt randomly gepakt
                # astar(start, goal, dist)
                # grid.visualize(grid.batteries, grid.houses)
                print("not available at the moment!")
            elif command == "DEPTH-FIRST":
                node = Node()
                best = Node()
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                best.price = 700000
                dfs(node, grid.batteries, grid.houses, distdict, best)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "HILLCLIMBER":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                print("""what is the base?
    choices:
        random
        greedy
        """)
                command = (input("> ")).upper()
                if command == "RANDOM":
                    random_alg(distdict, grid.batteries, grid.houses)
                    hillclimber(dist, distdict, grid.batteries, grid.houses)
                    price = price_calc(grid.batteries, distdict)
                    print(price)
                    grid.visualize(grid.batteries, grid.houses)
                elif command == "GREEDY":
                    Greedy(dist, grid.batteries, grid.houses)
                    hillclimber(dist, distdict, grid.batteries, grid.houses)
                    price = price_calc(grid.batteries, distdict)
                    print(price)
                    grid.visualize(grid.batteries, grid.houses)
                else:
                    print("invalid command")
                print("""Do you want to optimize the location of the batteries with hillclimber?
            Yes
            No
            """)
                command = (input("> ")).upper()
                if command == "YES":
                    dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                    hillclimber_batteries(grid.batteries)
                    dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                    price = price_calc(grid.batteries, distdict)
                    print(price)
                    grid.visualize(grid.batteries, grid.houses)
                elif command == "NO":
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
        else:
            print("neigborhood doesn't exist")
    else:
        print("not correct input")
