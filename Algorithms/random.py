import random
import copy

def random_alg(grid, distdict, b, h):
    #h2 = copy.deepcopy(h)
    keylist = list(range(0, 150))
    price = 0
    for nr in h:
        key2 = random.choice(keylist)
        keylist.remove(key2)
        house = h[key2]
        #house = random.choice(h2)
        for key in b:
            if house.output + b[key].filled < b[key].capacity:
                b[key].connected.append(house)
                b[key].filled += house.output
                h[house.id].pluggedin = b[key]
                price += distdict[key2][key]*9
                break
        if h[house.id].pluggedin == False:
            return 0
    return price, b, h
