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
from Helper_algorithms.clusterbatplacement import clusterbatplacement
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
    print(f"Best price found: {best.price}")
    nodetoclasses(batteries, houses, best)
    if savefig is True:
        visualize(batteries, houses, argv[1], command, best.price)


def input_firstfit(batteries, houses, command):
    print("use sorted list y/n")
    sorted = input("> ").lower()
    if sorted == "y" or sorted == "yes":
        grid.houses = grid.load_houses(
            f"Data/wijk{argv[1]}_huizensortedhigh-low.csv")
        houses = grid.houses
    decreasingfirstfit(batteries, houses)
    visualize(batteries, houses, argv[1], command)


def input_averagefit(batteries, houses, command):
    grid.houses = grid.load_houses(
        f"Data/wijk{argv[1]}_huizensortedhigh-low.csv")
    houses = grid.houses
    averagefit(batteries, houses)
    visualize(batteries, houses, argv[1], command)


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
    print(f"Best price found: {best.price}")
    if savefig is True:
        nodetoclasses(batteries, houses, best)
        visualize(batteries, houses, argv[1], command, best.price)


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
    print(f"Best price found: {price}")
    visualize(batteries, houses, argv[1], command, best.price)


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
        write_to_csv(argv[1], command, price)
        reset(batteries, houses)
    savefig = bestplot(argv[1], command, best.price)
    print(f"Best price found: {best.price}")
    nodetoclasses(batteries, houses, best)
    if savefig is True:
        visualize(batteries, houses, argv[1], command, best.price)
        battery_optimization(batteries)
        dist, distdict, lowbprice = distancearr(batteries, houses)
        price = price_calc(batteries, distdict)
        print(f"Best price found with optimize: {price}")
        visualize(batteries, houses, argv[1], command, price)


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
        visualize(batteries, houses, argv[1], command, best.price)


def input_kmeansbat(batteries, houses, command):
    k = len(batteries)
    clusters, connectedhomes = KmeansClusterdistance(houses, batteries, k)
    clusterbatplacement(batteries, houses, clusters, connectedhomes)
    command = "hillclimber_" + command
    input_hillclimber(batteries, houses, command)


def input_kmeans(batteries, houses, command):
    bestprice = 100000
    for k in range(5, 17):
        clusters, connectedhomes = KmeansClusterdistance(houses, batteries, k)
        b, h = clustertoclasses(batteries, houses, clusters, connectedhomes)
        if b is False:
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
    visualize(batteries, houses, argv[1], command, bestprice)


def funcdict():
    functions = {
        "1": (input_random, "random"),
        "2": (input_firstfit, "first-fit"),
        "3": (input_averagefit, "average-fit"),
        "4": (input_greedy, "greedy"),
        "5": (input_bfs, "breadth-first"),
        "6": (input_branchnbound, "branchnbound"),
        "7": (input_hillclimber, "hillclimber"),
        "8": (input_randclimber, "randclimber"),
        "9": (input_kmeansbat, "kmeansbatplacement"),
        "10": (input_kmeans, "kmeansdistance")
    }
    return functions


if __name__ == "__main__":
    if int(argv[1]) > 0 and int(argv[1]) < 6:
        grid = Grid(argv[1])
        if len(argv) == 2:
            print("""which algorithm to execute, please type the number:
choices:
1. random
2. first-fit
3. average-fit
4. greedy
5. breadth-first (only with wijk 4)
6. branchnbound (might not finish in this lifetime)
7. hillclimber
8. randclimber
9. kmeansbattplacement
10. kmeansclusterdistance
""")
            command = (input("> ")).lower()
            functions = funcdict()
            functions[command][0](
                grid.batteries, grid.houses, functions[command][1])
