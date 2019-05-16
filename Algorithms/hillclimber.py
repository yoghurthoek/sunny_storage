def hillclimber(dist, distdict, b, h):

    for nr1 in h:
        for nr2 in h:
            # Checkt of huizen niet al bij zelfde batterij zitten
            if not h[nr1].pluggedin == h[nr2].pluggedin:
                if (b[h[nr1].pluggedin.id].filled - h[nr1].output + h[nr2].output < b[h[nr1].pluggedin.id].capacity) and (b[h[nr2].pluggedin.id].filled - h[nr2].output + h[nr1].output < b[h[nr2].pluggedin.id].capacity):
                    if distdict[nr1][h[nr1].pluggedin.id] + distdict[nr2][h[nr2].pluggedin.id] > distdict[nr1][h[nr2].pluggedin.id] + distdict[nr2][h[nr1].pluggedin.id]:

                        b[h[nr1].pluggedin.id].filled += h[nr2].output - h[nr1].output
                        b[h[nr2].pluggedin.id].filled += h[nr1].output - h[nr2].output

                        b[h[nr2].pluggedin.id].connected.remove(h[nr2])
                        b[h[nr2].pluggedin.id].connected.append(h[nr1])

                        b[h[nr1].pluggedin.id].connected.remove(h[nr1])
                        b[h[nr1].pluggedin.id].connected.append(h[nr2])

                        temporary = h[nr2].pluggedin
                        h[nr2].pluggedin = h[nr1].pluggedin
                        h[nr1].pluggedin = temporary
