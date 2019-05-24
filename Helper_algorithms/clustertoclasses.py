from Classes.battery import Battery


def clustertoclasses(b, h, cluster, connectedhomes, movebat = False):
    """
    Helper-algorithm that is used to transfer the Kmeanscluster output to
    the grid.
    """

    b = {}
    for key in connectedhomes:
        outputcluster = 0
        for houseID in connectedhomes[key]:
            outputcluster += h[houseID].output
        cluster[key].append(outputcluster)

    index = 0
    for row in cluster:
        posx = row[0]
        posy = row[1]
        id = row[2]
        if row[3] < 450:
            capacity = 450
            price = 900
        elif row[3] < 900:
            capacity = 900
            price = 1350
        elif row[3] < 1800:
            capacity = 1800
            price = 1800
        elif row[3] > 1800:
            print("Not possible")
            return False, False
        filled = row[3]

        battery = Battery(id, posx, posy, capacity)
        b[id] = battery
        b[id].filled = filled
        b[id].price = price
        for house in connectedhomes[index]:
            b[id].connected.append(h[house])
        index += 1

    for c in connectedhomes:
        for house in connectedhomes[c]:
            h[house].pluggedin = b[c]

    return b, h
