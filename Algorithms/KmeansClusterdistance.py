import random

def KmeansClusterdistance(h, b, k):

    clustercenters = []
    keylist = list(range(0, 150))
    housecoordinates = {}
    k = list(range(0, k))
    for number in k:
        clustercenters.append([0,0,0])
        clustercenters[number][0] = random.choice(keylist)
        clustercenters[number][1] = random.choice(keylist)
        clustercenters[number][2] = number
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

    print(housecoordinates[0])
    print(housecoordinates[1])
    print(clustercenters)

    # for ps in housecoordinates:
    #
    #     if ps[3] == 1:
    #         manhattancum1 = manhattancum1 + abs(p[0] - housepos[1]) + \
    #                  abs(p[1] - housepos[2])
    # for h in b[bat].connected:
    #     positions[bat][0] += b[bat].connected[i].posx
    #     positions[bat][1] += b[bat].connected[i].posy
    #     i += 1
    # positions[bat][0] = round(positions[bat][0]/len(b[bat].connected))
    # positions[bat][1] = round(positions[bat][1]/len(b[bat].connected))
    # b[bat].posx = positions[bat][0]
    # b[bat].posy = positions[bat][1]
