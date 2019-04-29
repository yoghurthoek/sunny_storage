def Hillclimber(dist, b, h):
    price = 0
    for nr in h:
        for cell in dist[nr]:
            if b[cell[1]].filled + h[nr].output < b[cell[1]].capacity:
                b[cell[1]].connected.append(h[nr])
                b[cell[1]].filled += h[nr].output
                h[nr].pluggedin = b[cell[1]]
                price += cell[0] * 9
                break

    for nr1 in h:
            for nr2 in h:
                # Checkt of huizen niet al bij zelfde batterij zitten
                if not h[nr1].pluggedin == h[nr2].pluggedin:
                    for cell1 in dist[nr1]:
                        for cell2 in dist[nr2]:
                            if (b[cell2[1]].filled - h[nr1].output + h[nr2].output < b[cell2[1]].capacity) and (b[cell1[1]].filled - h[nr2].output + h[nr1].output < b[cell1[1]].capacity):
                                if dist[nr1][cell1[1]][0] + dist[nr2][cell2[1]][0] > dist[nr1][cell2[1]][0] + dist[nr2][cell1[1]][0]:
                                    temporary = h[nr2].pluggedin
                                    h[nr2].pluggedin = h[nr1].pluggedin
                                    h[nr1].pluggedin = temporary
                                    print(dist[nr1][cell1[1]][0])
                                    #b[cell1[1]].connected.remove(h[nr1])
                                    #b[cell2[1]].connected.remove(h[nr2])

                                    # better insert I think
                                    b[cell2[1]].connected.append(h[nr1])
                                    b[cell1[1]].connected.append(h[nr2])

                                    price = price - (dist[nr1][cell1[1]][0] + dist[nr2][cell2[1]][0] - (dist[nr1][cell2[1]][0] + dist[nr2][cell1[1]][0])) * 9
    return price
