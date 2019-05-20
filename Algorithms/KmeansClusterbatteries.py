import random
from copy import deepcopy

def KmeansClusterbatteries(b, h):

    batteryamount = 5
    totalcaphouse = 0
    housecoordinates = {}
    keylist = list(range(0, 50))
    for house in h:
        totalcaphouse += h[house].output
    batterylist_pos = {0: ["Powerstar", 450, 900, 0, 0, 0], 1: ["Imerse-II", 900, 1350, 0, 0, 0], 2: ["Imerse-III", 1800, 1800, 0, 0, 0]}


    while batteryamount < 18:
        used_batteries = {}
        batteryamountlist = list(range(0, batteryamount))
        bestfit = 10000
        housecapleft = totalcaphouse

        for battery in batterylist_pos:
            batterylist_pos[battery][1]
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
        print(used_batteries)

        startover = 0
        while startover < batteryamount:
            for number in batteryamountlist:
                housecoordinates[number] = []
                used_batteries[number][3] = random.choice(keylist)
                used_batteries[number][4] = random.choice(keylist)
                used_batteries[number][5] = used_batteries[number][2]
            for house in h:
                manhatbest = 1000
                for key in used_batteries:
                    manhat = abs(used_batteries[key][3] - h[house].posx) + \
                             abs(used_batteries[key][4] - h[house].posy)
                    if used_batteries[key][5] > h[house].output:
                        if manhat < manhatbest:
                            manhatbest = manhat
                            bestbattery = key
                        housecoordinates[bestbattery] = h[house].id
                        used_batteries[bestbattery][5] -= h[house].output
            # print(clustercenters, housecoordinates)

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
                    used_batteries[i][1] = round(totalx/totalh)
                    used_batteries[i][2] = round(totaly/totalh)
                if old_used_batteries[i][1] == used_batteries[i][1] and old_used_batteries[i][2] == used_batteries[i][2]:
                    startover += 1
        batteryamount += 1
    return used_batteries, housecoordinates
