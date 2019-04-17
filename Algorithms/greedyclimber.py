def Greedy(dist, b, h):
    price = 0
    for nr in h:
        for cell in dist[nr]:
            if b[cell[1]].filled + h[nr].output < b[cell[1]].capacity:
                b[cell[1]].connected.append(h[nr])
                b[cell[1]].filled += h[nr].output
                h[nr].pluggedin = b[cell[1]]
                price += cell[0] * 9
                break

    return price

    # Checks
    for key in b:
        print(b[key].filled)
    for house in h:
        print(h[house].pluggedin)

# def Hillclimber():
#
