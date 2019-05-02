def hillclimber(dist, distdict, price, b, h):
    # price = 0
    # for nr in h:
    #     for cell in dist[nr]:
    #         if b[cell[1]].filled + h[nr].output < b[cell[1]].capacity:
    #             b[cell[1]].connected.append(h[nr])
    #             b[cell[1]].filled += h[nr].output
    #             h[nr].pluggedin = b[cell[1]]
    #             price += cell[0] * 9
    #             break
    #averagefit
    print(distdict)
    for nr1 in h:
            for nr2 in h:
                if not h[nr1].pluggedin == h[nr2].pluggedin:
                    if (b[h[nr1].pluggedin.id].filled - h[nr1].output + h[nr2].output < b[h[nr1].pluggedin.id].capacity) and (b[h[nr2].pluggedin.id].filled - h[nr2].output + h[nr1].output < b[h[nr2].pluggedin.id].capacity):
                        if distdict[nr1][h[nr1].pluggedin.id] + distdict[nr2][h[nr2].pluggedin.id] > distdict[nr1][h[nr2].pluggedin.id] + distdict[nr2][h[nr1].pluggedin.id]:

                            # a = b[h[nr1].pluggedin.id].connected
                            # c = b[h[nr2].pluggedin.id].connected
                            # print(a)
                            #
                            # a[h[nr1]], c[h[nr2]] = c[h[nr1]], a[h[nr2]]

                            b[h[nr2].pluggedin.id].connected.remove(h[nr2])
                            b[h[nr2].pluggedin.id].connected.append(h[nr1])

                            b[h[nr1].pluggedin.id].connected.remove(h[nr1])
                            b[h[nr1].pluggedin.id].connected.append(h[nr2])

                            price = price - (dist[nr1][h[nr1].pluggedin.id][0] + dist[nr2][h[nr2].pluggedin.id][0]) * 9 + (dist[nr1][h[nr2].pluggedin.id][0] + dist[nr2][h[nr1].pluggedin.id][0]) * 9

                            temporary = h[nr2].pluggedin
                            h[nr2].pluggedin = h[nr1].pluggedin
                            h[nr1].pluggedin = temporary
    return price
