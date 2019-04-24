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
    depth-first""")
            command = (input("> ")).upper()
            if command == "RANDOM":
                grid.random(grid.batteries, grid.houses)
            elif command == "FIRST-FIT":
                Decreasingfirstfit(grid, grid.batteries, grid.houses)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "AVERAGE-FIT":
                Averagefit(grid, grid.batteries, grid.houses)
                grid.visualize(grid.batteries, grid.houses)
            elif command == "GREEDY-CLIMBER":
                dist, distdict = grid.Distancearr(grid.batteries, grid.houses)
                price = Greedy(dist, grid.batteries, grid.houses)
                print(price)
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
            else:
                print("invalid command")

        else:
            print("neigborhood doesn't exist")
    else:
        print("not correct input")
