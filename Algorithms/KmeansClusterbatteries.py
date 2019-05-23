import random
from copy import deepcopy


def KmeansClusterbatteries(b, h):
    """This function implements Kmeansclustering etc..."""

    batteryamount = 5
    totalcaphouse = 0
    housecoordinates = {}
    keylist = list(range(0, 50))
    for house in h:
        totalcaphouse += h[house].output
    batterylist_pos = {0: ["Powerstar", 450, 900, 0, 0, 0], 1: ["Imerse-II", 900, 1350, 0, 0, 0], 2: ["Imerse-III", 1800, 1800, 0, 0, 0]}

<<<<<<< HEAD
    for batteryamount in range(5, 18):
=======
    while batteryamount < 18:
>>>>>>> 6634557e79eeee9ca21a3ccff9590d9176e5bc27
        used_batteries = {}
        batteryamountlist = range(batteryamount)
        bestfit = 10000
        housecapleft = totalcaphouse

        #package met alle permutaties van een lijst
        for battery in batterylist_pos:
            fit = totalcaphouse/batteryamount - batterylist_pos[battery][1]
            if fit > 0 and fit < bestfit:
                fit = bestfit
                bestbattery = batterylist_pos[battery]
        for instance in batteryamountlist:
            used_batteries[instance] = []
            if bestbattery[1] < housecapleft:
                used_batteries[instance].append(bestbattery)
                housecapleft -= bestbattery[1]
            elif batterylist_pos[0][1] < housecapleft:
                used_batteries[instance].append(batterylist_pos[0][1])
            elif batterylist_pos[1][1] < housecapleft:
                used_batteries[instance].append(batterylist_pos[1][1])
        # print(used_batteries)

        startover = 0
        while startover < batteryamount:
            for number in batteryamountlist:
                housecoordinates[number] = []
                used_batteries[number][0][3] = random.choice(keylist)
                used_batteries[number][0][4] = random.choice(keylist)
                used_batteries[number][0][5] = used_batteries[number][0][1]
                # print(used_batteries)
            for house in h:
                manhatbest = 1000
                for key in used_batteries:
                    manhat = abs(used_batteries[key][0][3] - h[house].posx) + \
                             abs(used_batteries[key][0][4] - h[house].posy)
                    if used_batteries[key][0][5] > h[house].output:
                        if manhat < manhatbest:
                            manhatbest = manhat
                            bestbattery = key
                            housecoordinates[bestbattery].append(h[house].id)
                            used_batteries[bestbattery][0][5] -= h[house].output
            # print(housecoordinates)

            startover = 0
            old_used_batteries = deepcopy(used_batteries)
            for i in batteryamountlist:
                totaly = 0
                totalx = 0
                totalh = 0
                if len(housecoordinates[i]) != 0:
                    for houseID in housecoordinates[i]:
                        house = h[houseID]
                        totalx += house.posx
                        totaly += house.posy
                        totalh += 1
                    used_batteries[i][0][1] = round(totalx/totalh)
                    used_batteries[i][0][2] = round(totaly/totalh)
                if old_used_batteries[i][0][1] == used_batteries[i][0][1] and old_used_batteries[i][0][2] == used_batteries[i][0][2]:
                    startover += 1
                    print(used_batteries, end="\r")
    return used_batteries, housecoordinates
