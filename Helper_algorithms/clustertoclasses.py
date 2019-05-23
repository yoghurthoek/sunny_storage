from Classes.battery import Battery
from Classes.thegrid import Grid

def clustertoclasses(b, h, cluster, connectedhomes):

    b = {}
    print(cluster)
    print(connectedhomes)
    for key in connectedhomes:
        outputcluster = 0
        for houseID in connectedhomes[key]:
            outputcluster += h[houseID].output
        cluster[key].append(outputcluster)
    print(cluster)

    index = 0
    for row in cluster:
        posx = row[0]
        posy = row[1]
        id = row[2]
        if row[3] < 450:
            capacity = 450
        elif row[3] < 900:
            capacity = 900
        elif row[3] < 1800:
            capacity = 1800
        filled = row[3]

        # Make battery object with id as key
        battery = Battery(id, posx, posy, capacity)
        b[id] = battery
        b[id].filled = filled
        for house in connectedhomes[index]:
            b[id].connected.append(h[house])
        index += 1

    for c in connectedhomes:
        for house in connectedhomes[c]:
            h[house].pluggedin = b[c]

    return b, h
