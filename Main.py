from sys import argv
from Algorithms.averagefit import Averagefit
from Algorithms.bfs import bfs
from Algorithms.decreasingfirstfit import Decreasingfirstfit
from Algorithms.dfs import dfs
from Algorithms.greedy import Greedy
# from Algorithms.multiplehillclimber import multhillclimber
from Algorithms.randclimber import Randclimber
from Classes.thegrid import Grid
from Classes.node import Node
from Algorithms.hillclimber import hillclimber
from Algorithms.random import random_alg
from Algorithms.battery_optimization import battery_optimization
from Helper_algorithms.distancearr import distancearr
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
    depth-first
    hillclimber
    randclimber
    multiplehillclimber""")
            command = (input("> ")).upper()
            command2 = "no"
            command3 = "no"
            if command == "RANDOM":
                dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
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
                dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
                Greedy(dist, grid.batteries, grid.houses)
                price = price_calc(grid.batteries, distdict)
                print(price)
                visualize(grid.batteries, grid.houses)
                # grid.savefig('hallo.png') # plus 1 voor elke run?
            elif command == "BREADTH-FIRST":
                node = Node()
                best = Node()
                dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
                # Only use this if greedy gives a allowed solution
                best.price = Greedy(dist, grid.batteries, grid.houses)
                bfs(node, grid.batteries, grid.houses, distdict, best)
                visualize(grid.batteries, grid.houses)
            elif command == "DEPTH-FIRST":
                node = Node()
                best = Node()
                dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
                best.price = 700000
                node.lowbound = lowbprice
                dfs(node, grid.batteries, grid.houses, distdict, dist, best)
                price = price_calc(grid.batteries, distdict)
                visualize(grid.batteries, grid.houses)
            elif command == "HILLCLIMBER":
                dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
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
                    dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
                    battery_optimization(grid.batteries)
                    dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
                    price = price_calc(grid.batteries, distdict)
                    print(price)
                    visualize(grid.batteries, grid.houses)
                elif command == "NO OPTIMIZE":
                    print("nothing")
            elif command == "RANDCLIMBER":
                print("repeat until no change for how many times?")
                repetitions = int(input("> "))
                dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
                Greedy(dist, grid.batteries, grid.houses)
                price = price_calc(grid.batteries, distdict)
                print(f"Price of greedy: {price}")
                Randclimber(repetitions, distdict, grid.batteries, grid.houses)
                price = price_calc(grid.batteries, distdict)
                print(f"Price after climbing: {price}")
                visualize(grid.batteries, grid.houses)
            # elif command == "MULTIPLEHILLCLIMBER":
            #     print("repeat until no change for how many times?")
            #     repetitions = int(input("> "))
            #     dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
            #     Greedy(dist, grid.batteries, grid.houses)
            #     price = price_calc(grid.batteries, distdict)
            #     node = Node()
            #     node.fillnode(grid.batteries, grid.houses, price)
            #     print(f"Price of greedy: {price}")
            #     multhillclimber(node, repetitions, distdict, grid.batteries, grid.houses)
            #     price = price_calc(grid.batteries, distdict)
            #     print(f"Price after climbing: {price}")
            #     visualize(grid.batteries, grid.houses)
            # else:
            #     print("invalid command")

            print("""do you want to save your run?
            Options:
            Yes
            No
            """)
            if (input("> ")).upper() == "YES":
                algorithm = (command + " --> " + command2 + " --> " + command3)
                write_to_csv(argv[1], algorithm, price, grid.batteries, grid.houses)
                # save fig
        else:
            print("neigborhood doesn't exist")
    else:
        print("not correct input")
