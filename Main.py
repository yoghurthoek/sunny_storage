from sys import argv
from Algorithms.averagefit import Averagefit
from Algorithms.decreasingfirstfit import Decreasingfirstfit
from Algorithms.greedyclimber import Greedy
from Algorithms.bfs import bfs
from Algorithms.astar import astar
from Algorithms.dfs import dfs
from Classes.thegrid import Grid
from Classes.node import Node
from Classes.node2 import Noot
from Algorithms.hillclimber import hillclimber
from Algorithms.random import random_alg


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
    greedy-climber
    breadth-first
    A-star
    depth-first
    hillclimber""")
            command = (input("> ")).upper()
            if command == "RANDOM":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                output = random_alg(grid, distdict, grid.batteries, grid.houses)
                if output == 0:
                    for key in grid.batteries:
                        grid.batteries[key].connected = []
                    for key in grid.houses:
                        grid.houses[key].pluggedin = False
                    print(output)
                    print(grid.batteries)
                    print(grid.houses)
                    output = random_alg(grid, distdict, grid.batteries, grid.houses)
                    print("second time")
                print(output)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "FIRST-FIT":
                Decreasingfirstfit(grid, grid.batteries, grid.houses)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "AVERAGE-FIT":
                Averagefit(grid, grid.batteries, grid.houses)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "GREEDY-CLIMBER":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                greedy = Greedy(dist, grid.batteries, grid.houses)
                print(greedy[0])
                grid.visualize(grid.batteries, grid.houses)
            elif command == "BREADTH-FIRST":
                node = Node()
                best = Node()
                best.price = 999999
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
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
            elif command == "DEPTH_FIRST":
                print("not available at the moment!")
            elif command == "HILLCLIMBER":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                print("""what is the base?
    choices:
        random
        greedy-climber
        """)
                command = (input("> ")).upper()
                if command == "RANDOM":
                    random = random_alg(grid, distdict, grid.batteries, grid.houses)
                    print(random)
                    price = hillclimber(dist, distdict, random[0], random[1], random[2])
                elif command == "GREEDY-CLIMBER":
                    greedy = Greedy(dist, grid.batteries, grid.houses)
                    price = hillclimber(dist, distdict, greedy[0], greedy[1], greedy[2])
                else:
                    print("invalid command")
                print(price)
                grid.visualize(grid.batteries, grid.houses)
            else:
                print("invalid command")

        else:
            print("neigborhood doesn't exist")
    else:
        print("not correct input")
