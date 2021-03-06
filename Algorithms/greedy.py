import random


def greedy(dist, b, h):
    """
    This algorithm chooses randomly a house and connects it to a battery based
    on best (shortest) distance.
    """
    output = 0
    while output == 0:
        output = 1
        keylist = list(range(0, len(h)))
        for nr in h:
            key = random.choice(keylist)
            keylist.remove(key)

            for cell in dist[key]:
                if b[cell[1]].filled + h[key].output < b[cell[1]].capacity:
                    b[cell[1]].connected.append(h[key])
                    b[cell[1]].filled += h[nr].output
                    h[key].pluggedin = b[cell[1]]
                    break

            if h[h[key].id].pluggedin is False:
                output = 0
                for key in b:
                    b[key].connected = []
                    b[key].filled = 0
                for key in h:
                    h[key].pluggedin = False
                break
