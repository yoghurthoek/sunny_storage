from sys import argv
from Algorithms.averagefit import Averagefit
from Algorithms.bfs import bfs
from Algorithms.decreasingfirstfit import Decreasingfirstfit
from Algorithms.dfs import dfs
from Algorithms.greedy import greedy
#from Algorithms.multiplehillclimber import multhillclimber
from Algorithms.randclimber import Randclimber
from Classes.thegrid import Grid
from Classes.node import Node
from Algorithms.hillclimber import hillclimber
from Algorithms.random import random_alg
from Algorithms.battery_optimization import battery_optimization
from Helper_algorithms.distancearr import distancearr
from Helper_algorithms.nodetoclasses import nodetoclasses
from Helper_algorithms.price_calc import price_calc
from Helper_algorithms.reset import reset
from Helper_algorithms.visualize import visualize
from Helper_algorithms.write_to_csv import write_to_csv
from Algorithms.KmeansClusterdistance import KmeansClusterdistance

def input_random(batteries, houses, command):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    print(lowbprice)
    print("run how many times?")
    repeats = int(input("> "))
    best = Node()
    best.price = 70000
    for i in range(0, repeats):
        random_alg(distdict, batteries, houses)
        price = price_calc(batteries, distdict)
        if price < best.price:
            best.batts = [[], [], [], [], []]
            best.fillnode(batteries, houses, price)
        write_to_csv(argv[1], command, price)
        reset(batteries, houses)
    print(best.price)
    nodetoclasses(batteries, houses, best)
    visualize(batteries, houses)


def input_firstfit(batteries, houses, command):
    Decreasingfirstfit(grid, batteries, houses)
    visualize(batteries, houses)


def input_averagefit(batteries, houses, command):
    Averagefit(grid, batteries, houses)
    visualize(batteries, houses)


def input_greedy(batteries, houses, command):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    print("run how many times?")
    repeats = int(input("> "))
    best = Node()
    best.price = 70000
    for i in range(0, repeats):
        greedy(dist, batteries, houses)
        price = price_calc(batteries, distdict)
        if price < best.price:
            best.batts = [[], [], [], [], []]
            best.fillnode(batteries, houses, price)
        write_to_csv(argv[1], command, price)
        reset(batteries, houses)
    print(best.price)
    nodetoclasses(batteries, houses, best)
    visualize(batteries, houses)


def input_bfs(batteries, houses, command):
    node = Node()
    best = Node()
    dist, distdict, lowbprice = distancearr(batteries, houses)
    best.price = greedy(dist, batteries, houses)
    bfs(node, batteries, houses, distdict, best)
    visualize(batteries, houses)


def input_dfs(batteries, houses, command):
    node = Node()
    best = Node()
    dist, distdict, lowbprice = distancearr(batteries, houses)
    best.price = 700000
    node.lowbound = lowbprice
    dfs(node, batteries, houses, distdict, dist, best)
    price = price_calc(batteries, distdict)
    print(price)
    visualize(batteries, houses)


def input_hillclimber(batteries, houses, command, base):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    command = base + "-->" + command
    print("run how many times?")
    repeats = int(input("> "))
    best = Node()
    best.price = 70000
    for i in range(0, repeats):
        if base == "GREEDY":
            greedy(dist, batteries, houses)
        elif base == "RANDOM":
            random_alg(distdict, batteries, houses)
        hillclimber(dist, distdict, batteries, houses)
        price = price_calc(batteries, distdict)
        if price < best.price:
            best.batts = [[], [], [], [], []]
            best.fillnode(batteries, houses, price)
        write_to_csv(argv[1], command, price)
        reset(batteries, houses)
    print(best.price)
    nodetoclasses(batteries, houses, best)
    visualize(batteries, houses)


def input_randclimber(batteries, houses, command, base):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    print("repeat until no change for how many times?")
    repetitions = int(input("> "))
    print("run how many times?")
    repeats = int(input("> "))
    best = Node()
    best.price = 70000
    for i in range(0, repeats):
        if base == "GREEDY":
            greedy(dist, batteries, houses)
        elif base == "RANDOM":
            random_alg(distdict, batteries, houses)
        Randclimber(repetitions, distdict, batteries, houses)
        price = price_calc(batteries, distdict)
        if price < best.price:
            best.batts = [[], [], [], [], []]
            best.fillnode(batteries, houses, price)
        write_to_csv(argv[1], command, price)
        reset(batteries, houses)
    print(best.price)
    nodetoclasses(batteries, houses, best)
    visualize(batteries, houses)


def input_multclimber(batteries, houses, command, base):
    # print("repeat until no change for how many times?")
    # repetitions = int(input("> "))
    # dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    # Greedy(dist, grid.batteries, grid.houses)
    # price = price_calc(grid.batteries, distdict)
    # node = Node()
    # node.fillnode(grid.batteries, grid.houses, price)
    # print(f"Price of greedy: {price}")
    # multhillclimber(node, repetitions, distdict, grid.batteries, grid.houses)
    # price = price_calc(grid.batteries, distdict)
    # print(f"Price after climbing: {price}")
    # visualize(grid.batteries, grid.houses)
    pass


def input_kmeans(batteries, houses):
    print("how many clusters?")
    k = int(input("> "))
    KmeansClusterdistance(houses, batteries, k)


if __name__ == "__main__":
    if len(argv) == 2:
        if argv[1] == '1' or argv[1] == '2' or argv[1] == '3' or \
                argv[1] == '4' or argv[1] == '5':
            grid = Grid(argv[1])
            print("""which algorithm to execute:
choices:
    random
    first_fit
    average-fit
    greedy
    breadth-first
    depth-first
    hillclimber
    randclimber
    multiplehillclimber""")
    functions = {
        "RANDOM": input_random,
        "FIRST-FIT": input_firstfit,
        "AVERAGE_FIT": input_averagefit,
        "GREEDY": input_greedy,
        "BREADTH-FIRST": input_bfs,
        "DEPTH-FIRST": input_dfs,
        "HILLCLIMBER": input_hillclimber,
        "RANDCLIMBER": input_randclimber,
        "MULTIPLEHILLCLIMBER": input_multclimber,
        "KMEANSCLUSTERDISTANCE": input_kmeans
    }
    command = (input("> ")).upper()
    try:
        functions[command](grid.batteries, grid.houses, command)
    except TypeError:
        print("base: greedy or random")
        base = (input("> ")).upper()
        functions[command](grid.batteries, grid.houses, command, base)

    #         if command == "RANDOM":
    #             dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    #             random_alg(distdict, grid.batteries, grid.houses)
    #             price = price_calc(grid.batteries, distdict)
    #             print(price)
    #             visualize(grid.batteries, grid.houses)
    #         elif command == "FIRST_FIT":
    #             Decreasingfirstfit(grid, grid.batteries, grid.houses)
    #             visualize(grid.batteries, grid.houses)
    #         elif command == "AVERAGE-FIT":
    #             Averagefit(grid, grid.batteries, grid.houses)
    #             visualize(grid.batteries, grid.houses)
    #         elif command == "GREEDY":
    #             dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    #             Greedy(dist, grid.batteries, grid.houses)
    #             price = price_calc(grid.batteries, distdict)
    #             print(price)
    #             visualize(grid.batteries, grid.houses)
    #             # grid.savefig('hallo.png') # plus 1 voor elke run?
    #         elif command == "BREADTH-FIRST":
    #             node = Node()
    #             best = Node()
    #             dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    #             best.price = Greedy(dist, grid.batteries, grid.houses)
    #             bfs(node, grid.batteries, grid.houses, distdict, best)
    #             visualize(grid.batteries, grid.houses)
    #         elif command == "DEPTH-FIRST":
    #             node = Node()
    #             best = Node()
    #             dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    #             best.price = 700000
    #             node.lowbound = lowbprice
    #             dfs(node, grid.batteries, grid.houses, distdict, dist, best)
    #             price = price_calc(grid.batteries, distdict)
    #             visualize(grid.batteries, grid.houses)
    #         elif command == "HILLCLIMBER":
    #             dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    #             print("""what is the base?
    #                         choices:
    #                         random
    #                         greedy
    #                         """)
    #             command2 = (input("> ")).upper()
    #             if command2 == "RANDOM":
    #                 random_alg(distdict, grid.batteries, grid.houses)
    #                 hillclimber(dist, distdict, grid.batteries, grid.houses)
    #                 price = price_calc(grid.batteries, distdict)
    #                 print(price)
    #                 visualize(grid.batteries, grid.houses)
    #             elif command2 == "GREEDY":
    #                 Greedy(dist, grid.batteries, grid.houses)
    #                 hillclimber(dist, distdict, grid.batteries, grid.houses)
    #                 price = price_calc(grid.batteries, distdict)
    #                 print(price)
    #                 visualize(grid.batteries, grid.houses)
    #             else:
    #                 print("invalid command")
    #             print("""Do you want to optimize the location of the batteries with hillclimber?
    #         Optimize
    #         no optimize
    #         """)
    #             command3 = (input("> ")).upper()
    #             if command3 == "OPTIMIZE":
    #                 dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    #                 battery_optimization(grid.batteries)
    #                 dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    #                 price = price_calc(grid.batteries, distdict)
    #                 print(price)
    #                 visualize(grid.batteries, grid.houses)
    #             elif command == "NO OPTIMIZE":
    #                 print("nothing")
    #         elif command == "RANDCLIMBER":
    #             print("repeat until no change for how many times?")
    #             repetitions = int(input("> "))
    #             dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    #             Greedy(dist, grid.batteries, grid.houses)
    #             price = price_calc(grid.batteries, distdict)
    #             print(f"Price of greedy: {price}")
    #             Randclimber(repetitions, distdict, grid.batteries, grid.houses)
    #             price = price_calc(grid.batteries, distdict)
    #             print(f"Price after climbing: {price}")
    #             visualize(grid.batteries, grid.houses)
    #         # elif command == "MULTIPLEHILLCLIMBER":
    #         #     print("repeat until no change for how many times?")
    #         #     repetitions = int(input("> "))
    #         #     dist, distdict, lowbprice = distancearr(grid.batteries, grid.houses)
    #         #     Greedy(dist, grid.batteries, grid.houses)
    #         #     price = price_calc(grid.batteries, distdict)
    #         #     node = Node()
    #         #     node.fillnode(grid.batteries, grid.houses, price)
    #         #     print(f"Price of greedy: {price}")
    #         #     multhillclimber(node, repetitions, distdict, grid.batteries, grid.houses)
    #         #     price = price_calc(grid.batteries, distdict)
    #         #     print(f"Price after climbing: {price}")
    #         #     visualize(grid.batteries, grid.houses)
    #         else:
    #             print("invalid command")
    #
    #         print("""do you want to save your run?
    #         Options:
    #         Yes
    #         No
    #         """)
    #         if (input("> ")).upper() == "YES":
    #             algorithm = (command + " --> " + command2 + " --> " + command3)
    #             write_to_csv(argv[1], algorithm, price)
    #             # save fig
    #     else:
    #         print("neigborhood doesn't exist")
    # else:
    #     print("not correct input")
