import random

def Greedy(dist, b, h):
    price = 0
    keylist = list(range(0, 150))
    for nr in h:
        key = random.choice(keylist)
        keylist.remove(key)
        for cell in dist[key]:
            if b[cell[1]].filled + h[key].output < b[cell[1]].capacity:
                b[cell[1]].connected.append(h[key])
                b[cell[1]].filled += h[nr].output
                h[key].pluggedin = b[cell[1]]
                price += cell[0] * 9
                break
    return price, b, h
