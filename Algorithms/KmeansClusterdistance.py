import random
from copy import deepcopy

def KmeansClusterdistance(h, b, k):

        clustercenters = []
        keylist = list(range(0, 50))
        housecoordinates = {}
        k_list = list(range(0, k))
        for number in k_list:
            clustercenters.append([0,0,0])
            clustercenters[number][0] = random.choice(keylist)
            clustercenters[number][1] = random.choice(keylist)
            clustercenters[number][2] = number
            housecoordinates[number] = []

        startover = 0
        while startover < k:
            for number in k_list:
                housecoordinates[number] = []
            for house in h:
                manhatbest = 1000
                for p in clustercenters:
                    manhat = abs(p[0] - h[house].posx) + \
                             abs(p[1] - h[house].posy)
                    if manhat < manhatbest:
                        manhatbest = manhat
                        bestp = p[2]
                housecoordinates[bestp].append(h[house].id)
            print(clustercenters, housecoordinates)

            startover = 0
            oldclustercenters = deepcopy(clustercenters)
            for i in k_list:
                totaly = 0
                totalx = 0
                totalh = 0
                if len(housecoordinates[i]) != 0:
                    for houseID in housecoordinates[i]:
                        house = h[houseID]
                        totalx += house.posx
                        totaly += house.posy
                        totalh += 1
                    clustercenters[i][0] = round(totalx/totalh)
                    clustercenters[i][1] = round(totaly/totalh)

                if oldclustercenters[i][0] == clustercenters[i][0] and oldclustercenters[i][1] == clustercenters[i][1]:
                    startover += 1
        return clustercenters, housecoordinates
