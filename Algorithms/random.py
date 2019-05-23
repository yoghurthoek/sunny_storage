import random


def random_alg(distdict, b, h):
    """
    This algorithm connects houses and batteries randomly
    """
    output = 0
    while output == 0:
        keylist = list(range(0, 150))
        output = 1
        for nr in h:
            key2 = random.choice(keylist)
            keylist.remove(key2)
            house = h[key2]
            for key in b:
                if house.output + b[key].filled < b[key].capacity:
                    b[key].connected.append(house)
                    b[key].filled += house.output
                    h[house.id].pluggedin = b[key]
                    break
            if h[house.id].pluggedin is False:
                output = 0
                for key in b:
                    b[key].connected = []
                    b[key].filled = 0
                for key in h:
                    h[key].pluggedin = False
                break
