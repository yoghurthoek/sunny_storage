from sys import argv
from Algorithms.averagefit import Averagefit
from Algorithms.bfs import bfs
from Algorithms.decreasingfirstfit import Decreasingfirstfit
from Algorithms.branchnbound import branchnbound
from Algorithms.greedy import greedy
#from Algorithms.multiplehillclimber import multhillclimber
from Algorithms.randclimber import Randclimber
from Classes.thegrid import Grid
from Classes.node import Node
from Algorithms.hillclimber import hillclimber
from Algorithms.random import random_alg
from Algorithms.battery_optimization import battery_optimization
from Helper_algorithms.clustertoclasses import clustertoclasses
from Helper_algorithms.distancearr import distancearr
from Helper_algorithms.nodetoclasses import nodetoclasses
from Helper_algorithms.price_calc import price_calc
from Helper_algorithms.reset import reset
from Helper_algorithms.visualize import visualize
from Helper_algorithms.write_to_csv import write_to_csv
from Algorithms.KmeansClusterdistance import KmeansClusterdistance


def input_random(batteries, houses, command, repeats=1):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    if repeats == 1:
        print("run how many times?")
        repeats = int(input("> "))
    best = Node()
    best.price = 100000
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


def input_firstfit(batteries, houses, command, repeats=1):
    Decreasingfirstfit(grid, batteries, houses)
    visualize(batteries, houses)


def input_averagefit(batteries, houses, command, repeats=1):
    Averagefit(grid, batteries, houses)
    visualize(batteries, houses)


def input_greedy(batteries, houses, command, repeats=1):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    if repeats == 1:
        print("run how many times?")
        repeats = int(input("> "))
    best = Node()
    best.price = 100000
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


def input_bfs(batteries, houses, command, repeats=1):
    node = Node()
    best = Node()
    dist, distdict, lowbprice = distancearr(batteries, houses)
    best.price = greedy(dist, batteries, houses)
    bfs(node, batteries, houses, distdict, best)
    visualize(batteries, houses)


def input_branchnbound(batteries, houses, command, repeats=1):
    node = Node()
    best = Node()
    dist, distdict, lowbprice = distancearr(batteries, houses)
    best.price = 100000
    node.lowbound = lowbprice
    branchnbound(node, batteries, houses, distdict, dist, best)
    price = price_calc(batteries, distdict)
    print(price)
    visualize(batteries, houses)


def input_hillclimber(batteries, houses, command, base, repeats=1):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    command = base + "-->" + command
    if repeats == 1:
        print("run how many times?")
        repeats = int(input("> "))
    best = Node()
    best.price = 100000
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


def input_randclimber(batteries, houses, command, base, repeats=1):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    command = base + "-->" + command
    print("repeat until no change for how many times?")
    repetitions = int(input("> "))
    if repeats == 1:
        print("run how many times?")
        repeats = int(input("> "))
    best = Node()
    best.price = 100000
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


def input_kmeans(batteries, houses, command, repeats=1):
    print("how many clusters?")
    k = int(input("> "))
    clusters, connectedhomes = KmeansClusterdistance(houses, batteries, k)
    # print(clusters, connectedhomes)
    clustertoclasses(batteries, houses, clusters, connectedhomes)
    visualize(batteries, houses)


def input_batoptimize(batteries, houses, command, base, repeats=1):
    command = base + "-->" + "HILLCLIMBER" + "-->" + "OPTIMIZE"
    input_hillclimber(batteries, houses, "HILLCLIMBER", base)
    battery_optimization(batteries)
    dist, distdict, lowbprice = distancearr(batteries, houses)
    price = price_calc(batteries, distdict)
    write_to_csv(argv[1], command, price)
    print(price)
    visualize(batteries, houses)


functions = {
    "RANDOM": input_random,
    "FIRST-FIT": input_firstfit,
    "AVERAGE-FIT": input_averagefit,
    "GREEDY": input_greedy,
    "BREADTH-FIRST": input_bfs,
    "BRANCHNBOUND": input_branchnbound,
    "HILLCLIMBER": input_hillclimber,
    "RANDCLIMBER": input_randclimber,
    "MULTIPLEHILLCLIMBER": input_multclimber,
    "KMEANSCLUSTERDISTANCE": input_kmeans,
    "OPTIMIZE": input_batoptimize
}

if __name__ == "__main__":
    if int(argv[1]) > 0 and int(argv[1]) < 6:
        if len(argv) == 4:
            grid = Grid(argv[1])
            command = argv[2].upper()
            try:
                repeats = int(argv[3])
            except ValueError:
                print("input a positive int")
                repeats = 1
            try:
                functions[command](grid.batteries, grid.houses, command, repeats)
            except TypeError:
                print("base: greedy or random")
                base = (input("> ")).upper()
                functions[command](grid.batteries, grid.houses, command, base, repeats)
            except KeyError:
                print("invalid command")
        elif len(argv) == 3:
            grid = Grid(argv[1])
            command = argv[2].upper()
            try:
                functions[command](grid.batteries, grid.houses, command)
            except TypeError:
                print("base: greedy or random")
                base = (input("> ")).upper()
                functions[command](grid.batteries, grid.houses, command, base)
            except KeyError:
                print("invalid command")
        elif len(argv) == 2:
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
    multiplehillclimber
    Kmeansclusterdistance
    optimize""")
            command = (input("> ")).upper()
            try:
                functions[command](grid.batteries, grid.houses, command)
            except TypeError:
                print("base: greedy or random")
                base = (input("> ")).upper()
                functions[command](grid.batteries, grid.houses, command, base)
            except KeyError:
                print("invalid command")
