def distancearr(b, h):
    """
    Gives manhattan distance for every combination of battery and house
    format: [for every house[(mhdistance, key of battery)]]
    """

    dist = []
    lowbprice = 0
    for house in h:
        dist.append([])
        for batt in b:
            manhat = abs(b[batt].posx - h[house].posx) + \
                     abs(b[batt].posy - h[house].posy)
            dist[house].append((manhat, batt))
        dist[house] = sorted(dist[house])
        lowbprice += dist[house][0][0] * 9

    distdict = {}
    for nr in h:
        distdict[nr] = {}
        for batt in dist[nr]:
            distdict[nr][batt[1]] = batt[0]
    return dist, distdict, lowbprice
