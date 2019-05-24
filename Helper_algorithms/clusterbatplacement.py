def clusterbatplacement(b, h, cluster, connectedhomes):
    """
    Helper-algorithm that modifies batteries to the coordinates found with
    k-means
    """
    for batt in b:
        b[batt].posx = cluster[batt][0]
        b[batt].posy = cluster[batt][1]
        for house in connectedhomes[batt]:
            b[batt].connected.append(h[house])
