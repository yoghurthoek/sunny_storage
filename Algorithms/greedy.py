import random


def greedy(dist, b, h):
    """

    """
    # Keeps repeating until all houses are placed
    output = 0
    while output == 0:
        output = 1
        keylist = list(range(0, len(h)))
        for nr in h:

            # Chooses a random key for house dictionary
            key = random.choice(keylist)
            keylist.remove(key)

            # Adds house to nearest battery unless capacity is exceeded
            for cell in dist[key]:
                if b[cell[1]].filled + h[key].output < b[cell[1]].capacity:
                    b[cell[1]].connected.append(h[key])
                    b[cell[1]].filled += h[nr].output
                    h[key].pluggedin = b[cell[1]]
                    break

            # Checks if a house has not been connected
            if h[h[key].id].pluggedin is False:
                output = 0
                for key in b:
                    b[key].connected = []
                    b[key].filled = 0
                for key in h:
                    h[key].pluggedin = False
                break
