from random import choice
import itertools
import pickle


def multhillclimber(best, repetitions, distdict, b, h):
    """
    A version of hillclimber which switches random houses iteratively
    """
# Set a while loop which changes random houses and keeps if the price is lower
    options = [0, 1, 2, 3, 4]
    startover = 0
    while startover < repetitions:
        breaker = False
        batteries = [choice(options) for i in range(0, 4)]
        # houses = set(choice(best.batts[battery]) for battery in batteries)
        housescheck = set()
        houses = []
        for battery in batteries:
            temp = choice(best.batts[battery])
            houses.append(temp)
            housescheck.add(temp)
        if len(housescheck) == 4:
            both = list(zip(batteries, houses))
            combi = []
            for combination in itertools.combinations(both, 2):
                combi.append(combination)
            for i in range(0, 3):
                cnode = pickle.loads(pickle.dumps(best, -1))
                # calculate new filled values
                cnode.fill[combi[i][0][0]][0] += h[combi[i][1][1]].output - h[combi[i][0][1]].output
                cnode.fill[combi[i][1][0]][0] += h[combi[i][0][1]].output - h[combi[i][1][1]].output
                cnode.fill[combi[5-i][0][0]][0] += h[combi[5-i][1][1]].output - h[combi[5-i][0][1]].output
                cnode.fill[combi[5-i][1][0]][0] += h[combi[5-i][0][1]].output - h[combi[5-i][1][1]].output
                for batt in cnode.fill:
                    if batt[0] > b[0].capacity:
                        breaker = True
                if breaker is True:
                    break
                # calculate new price
                cnode.price += distdict[combi[i][0][1]][combi[i][1][0]] + distdict[combi[i][1][1]][combi[i][0][0]] + distdict[combi[5-i][0][1]][combi[5-i][1][0]] + distdict[combi[5-i][1][1]][combi[5-i][0][0]] \
                    - distdict[combi[i][0][1]][combi[i][0][0]] - distdict[combi[i][1][1]][combi[i][1][0]] - distdict[combi[5-i][0][1]][combi[5-i][0][0]] - distdict[combi[5-i][1][1]][combi[5-i][1][0]]

                # if filled is possible and price is better. swap it.
                if best.price > cnode.price:
                    cnode.batts[combi[i][0][0]].remove(combi[i][0][1])
                    cnode.batts[combi[i][1][0]].append(combi[i][0][1])
                    cnode.batts[combi[i][1][0]].remove(combi[i][1][1])
                    cnode.batts[combi[i][0][0]].append(combi[i][1][1])

                    cnode.batts[combi[5-i][0][0]].remove(combi[5-i][0][1])
                    cnode.batts[combi[5-i][1][0]].append(combi[5-i][0][1])
                    cnode.batts[combi[5-i][1][0]].remove(combi[5-i][1][1])
                    cnode.batts[combi[5-i][0][0]].append(combi[5-i][1][1])

                    best = cnode
                    startover = 0
                    break

        startover += 1

    # Set best configuration into the battery class to visualize
    for bat in b:
        for housekey in best.batts[bat]:
            b[bat].connected.append(h[housekey])

    # Set house connections to true, so does not get blacked out in visualize
    for bat in b:
        for house in b[bat].connected:
            house.pluggedin = b[bat]
