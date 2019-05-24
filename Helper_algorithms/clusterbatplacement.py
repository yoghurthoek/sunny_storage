def clusterbatplacement(b, h, cluster, connectedhomes):
    for batt in b:
        b[batt].posx = cluster[batt][0]
        b[batt].posy = cluster[batt][1]
        for house in connectedhomes[batt]:
            b[batt].connected.append(h[house])

    for c in connectedhomes:
        for house in connectedhomes[c]:
            h[house].pluggedin = b[c]
