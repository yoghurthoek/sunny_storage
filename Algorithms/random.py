import random
import copy

def random_alg(grid, b, h):
    print(h)
    h2 = copy.deepcopy(h)
    for nr in h:
        house = random.choice(h2)
        for key in b:
            if house.output + b[key].filled < b[key].capacity:
                b[key].connected.append(house)
                b[key].filled += house.output
                print(house)
                del h2[house.id]
                print(h2)
                h[house.id].pluggedin = b[key]
                break
