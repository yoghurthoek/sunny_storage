import random
import copy

def random_alg(distdict, b, h):
    output = 0
    while output == 0:
        keylist = list(range(0, 150))
        price = 0
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
                    price += distdict[key2][key]*9
                    break
            if h[house.id].pluggedin == False:
                output = 0
                for key in b:
                    b[key].connected = []
                    b[key].filled = 0
                for key in h:
                    h[key].pluggedin = False
                break
        print(output)
        print("rerun")
    return price
