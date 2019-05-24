from sys import argv
from Algorithms.averagefit import averagefit
from Algorithms.bfs import bfs
from Algorithms.decreasingfirstfit import decreasingfirstfit
from Algorithms.branchnbound import branchnbound
from Algorithms.greedy import greedy
from Algorithms.randclimber import randclimber
from Classes.thegrid import Grid
from Classes.node import Node
from Algorithms.hillclimber import hillclimber
from Algorithms.random import random_alg
from Algorithms.battery_optimization import battery_optimization
from Helper_algorithms.bestplot import bestplot
from Helper_algorithms.clustertoclasses import clustertoclasses
from Helper_algorithms.distancearr import distancearr
from Helper_algorithms.nodetoclasses import nodetoclasses
from Helper_algorithms.price_calc import price_calc
from Helper_algorithms.reset import reset
from Helper_algorithms.visualize import visualize
from Helper_algorithms.write_to_csv import write_to_csv
from Algorithms.KmeansClusterdistance import KmeansClusterdistance


def input_random(batteries, houses, command):
    dist, distdict, lowbprice = distancearr(batteries, houses)
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
    savefig = bestplot(argv[1], command, best.price)
    print(best.price)
    nodetoclasses(batteries, houses, best)
    if savefig is True:
        visualize(batteries, houses, argv[1], command)


def input_firstfit(grid, command):
#     decreasingfirstfit(grid, batteries, houses)
#     visualize(batteries, houses, argv[1], command)
    pass
#
def input_averagefit(grid, command):
#     averagefit(grid, batteries, houses)
#     visualize(batteries, houses, argv[1], command)
    pass

def input_greedy(batteries, houses, command):
    dist, distdict, lowbprice = distancearr(batteries, houses)
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
    savefig = bestplot(argv[1], command, best.price)
    print(best.price)
    if savefig is True:
        nodetoclasses(batteries, houses, best)
        visualize(batteries, houses, argv[1], command)


def input_bfs(batteries, houses, command):
    node = Node()
    best = Node()
    dist, distdict, lowbprice = distancearr(batteries, houses)
    best.price = 100000
    best = bfs(node, batteries, houses, distdict, best)
    nodetoclasses(batteries, houses, best)
    visualize(batteries, houses, argv[1], command)


def input_branchnbound(batteries, houses, command):
    node = Node()
    best = Node()
    dist, distdict, lowbprice = distancearr(batteries, houses)
    best.price = 100000
    node.lowbound = lowbprice
    best = branchnbound(node, batteries, houses, distdict, dist, best)
    nodetoclasses(batteries, houses, best)
    price = price_calc(batteries, distdict)
    print(price)
    visualize(batteries, houses, argv[1], command)


def input_hillclimber(batteries, houses, command):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    print("base: greedy or random")
    base = (input("> ")).lower()
    command = base + "_" + command
    print("run how many times?")
    repeats = int(input("> "))
    best = Node()
    best.price = 100000
    for i in range(0, repeats):
        if base == "greedy":
            greedy(dist, batteries, houses)
        elif base == "random":
            random_alg(distdict, batteries, houses)
        hillclimber(dist, distdict, batteries, houses)
        price = price_calc(batteries, distdict)
        if price < best.price:
            best.batts = [[], [], [], [], []]
            best.fillnode(batteries, houses, price)
            bat_op = batteries
            houses_op = houses
        write_to_csv(argv[1], command, price)
        reset(batteries, houses)
    savefig = bestplot(argv[1], command, best.price)
    print(best.price)
    nodetoclasses(batteries, houses, best)
    if savefig is True:
        visualize(batteries, houses, argv[1], command)


def input_randclimber(batteries, houses, command):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    print("base: greedy or random")
    base = (input("> ")).lower()
    print("repeat until no change for how many times?")
    repetitions = int(input("> "))
    command = base + "_" + command + str(repetitions)
    print("run how many times?")
    repeats = int(input("> "))
    best = Node()
    best.price = 100000
    for i in range(0, repeats):
        if base == "greedy":
            greedy(dist, batteries, houses)
        elif base == "random":
            random_alg(distdict, batteries, houses)
        randclimber(repetitions, distdict, batteries, houses)
        price = price_calc(batteries, distdict)
        if price < best.price:
            best.batts = [[], [], [], [], []]
            best.fillnode(batteries, houses, price)
        write_to_csv(argv[1], command, price)
        reset(batteries, houses)
    savefig = bestplot(argv[1], command, best.price)
    print(best.price)
    if savefig is True:
        nodetoclasses(batteries, houses, best)
        visualize(batteries, houses, argv[1], command)

def input_kmeans(batteries, houses, command):
    bestprice = 100000
    for k in range(5, 12):
        clusters, connectedhomes = KmeansClusterdistance(houses, batteries, k)
        # print(clusters, connectedhomes)
        b, h = clustertoclasses(batteries, houses, clusters, connectedhomes)
        if b == False:
            k -= 1
            continue
        batteries = b
        houses = h
        dist, distdict, lowbprice = distancearr(batteries, houses)
        price = price_calc(batteries, distdict)
        if price < bestprice:
            print(price)
            print(k)
            bestprice = price
            bestbat = batteries
    batteries = bestbat
    visualize(batteries, houses, argv[1], command)


def input_batoptimize(batteries, houses, command):
    output = input_hillclimber(batteries, houses, "hillclimber")
    # command = base + "_" + "hillclimber" + "_" + "optimize"
    battery_optimization(batteries)
    dist, distdict, lowbprice = distancearr(batteries, houses)
    price = price_calc(batteries, distdict)
    write_to_csv(argv[1], command, price)
    print(price)
    visualize(batteries, houses, argv[1], command)

def funcdict():
    functions = {
        "random": input_random,
        "first-fit": input_firstfit,
        "average-fit": input_averagefit,
        "greedy": input_greedy,
        "breadth-first": input_bfs,
        "branchnbound": input_branchnbound,
        "hillclimber": input_hillclimber,
        "randclimber": input_randclimber,
        "kmeansclusterdistance": input_kmeans,
        "optimize": input_batoptimize
    }
    return functions


if __name__ == "__main__":
    if int(argv[1]) > 0 and int(argv[1]) < 6:
        grid = Grid(argv[1])
        if len(argv) == 2:
            print("""which algorithm to execute:
choices:
random
first-fit
average-fit
greedy
breadth-first (only with wijk 5)
branchnbound (might not finish in this lifetime)
hillclimber
randclimber
kmeansclusterdistance
optimize""")
            command = (input("> ")).lower()
            functions = funcdict()
            functions[command](grid.batteries, grid.houses, command)
