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
from Algorithms.KmeansClusterbatteries import KmeansClusterbatteries


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
    savefig = bestplot(argv[1], command, best.price)
    print(best.price)
    nodetoclasses(batteries, houses, best)
    if savefig is True:
        visualize(batteries, houses, argv[1], command)


def input_firstfit(batteries, houses, command, repeats=1):
    decreasingfirstfit(grid, batteries, houses)
    visualize(batteries, houses, argv[1], command)


def input_averagefit(batteries, houses, command, repeats=1):
    averagefit(grid, batteries, houses)
    visualize(batteries, houses, argv[1], command)


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
    savefig = bestplot(argv[1], command, best.price)
    print(best.price)
    if savefig is True:
        nodetoclasses(batteries, houses, best)
        visualize(batteries, houses, argv[1], command)


def input_bfs(batteries, houses, command, repeats=1):
    node = Node()
    best = Node()
    dist, distdict, lowbprice = distancearr(batteries, houses)
    best.price = 100000
    bfs(node, batteries, houses, distdict, best)
    visualize(batteries, houses, argv[1], command)


def input_branchnbound(batteries, houses, command, repeats=1):
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


def input_hillclimber(batteries, houses, command, base, repeats=1):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    command = base + "_" + command
    if repeats == 1:
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


def input_randclimber(batteries, houses, command, base, repeats=1):
    dist, distdict, lowbprice = distancearr(batteries, houses)
    print("repeat until no change for how many times?")
    repetitions = int(input("> "))
    command = base + "_" + command + str(repetitions)
    if repeats == 1:
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


def input_kmeans(batteries, houses, command, repeats=1):
    print("how many clusters?")
    k = int(input("> "))
    clusters, connectedhomes = KmeansClusterdistance(houses, batteries, k)
<<<<<<< HEAD
    # print(clusters, connectedhomes)
    b, h = clustertoclasses(batteries, houses, clusters, connectedhomes)
    batteries = b
    houses = h
    for bat in batteries:
        print(batteries[bat].posx)
        print(batteries[bat].posy)
=======
    clustertoclasses(batteries, houses, clusters, connectedhomes)
>>>>>>> 6634557e79eeee9ca21a3ccff9590d9176e5bc27
    visualize(batteries, houses, argv[1], command)


def input_batoptimize(batteries, houses, command, base, repeats=1):
    command = base + "-->" + "hillclimber" + "-->" + "optimize"
    output = input_hillclimber(batteries, houses, "hillclimber", base)
    battery_optimization(batteries)
    dist, distdict, lowbprice = distancearr(batteries, houses)
    price = price_calc(batteries, distdict)
    write_to_csv(argv[1], command, price)
    print(price)
    # alleen visualize werkt nog niet
    visualize(batteries, houses, argv[1], command)


def battery_Kmeans(batteries, houses, command, repeats):
    a, b = KmeansClusterbatteries(batteries, houses)
    # print(a)
    # print(b)


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
    "kmeansclusterbatteries": battery_Kmeans,
    "optimize": input_batoptimize
}

if __name__ == "__main__":
    if int(argv[1]) > 0 and int(argv[1]) < 6:
        if len(argv) == 4:
            grid = Grid(argv[1])
            command = argv[2].lower()
            try:
                repeats = int(argv[3])
            except ValueError:
                print("input a positive int")
                repeats = 1
            if command == "hillclimber" or command == "randclimber" or command == "optimize":
                print("base: greedy or random")
                base = (input("> ")).lower()
                functions[command](grid.batteries, grid.houses, command, base, repeats)
            else:
                functions[command](grid.batteries, grid.houses, command, repeats)
        elif len(argv) == 3:
            grid = Grid(argv[1])
            command = argv[2].lower()
            repeats = 1
            if command == "hillclimber" or command == "randclimber" or command == "optimize":
                print("base: greedy or random")
                base = (input("> ")).lower()
                functions[command](grid.batteries, grid.houses, command, base, repeats)
            else:
                functions[command](grid.batteries, grid.houses, command, repeats)
        elif len(argv) == 2:
            grid = Grid(argv[1])
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
    Kmeansclusterdistance
    Kmeansclusterbatteries
    optimize""")
            command = (input("> ")).lower()
            repeats = 1
            if command == "hillclimber" or command == "randclimber" or command == "optimize":
                print("base: greedy or random")
                base = (input("> ")).lower()
                functions[command](grid.batteries, grid.houses, command, base, repeats)
            else:
                functions[command](grid.batteries, grid.houses, command, repeats)
