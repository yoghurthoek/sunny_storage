def Decreasingfirstfit(grid, b, h):
    for nr in h:
        for key in b:
            if h[nr].output + b[key].filled < b[key].capacity:
                b[key].connected.append(h[nr])
                b[key].filled += h[nr].output
                h[nr].pluggedin = b[key]
                break

    # Checks
    for key in b:
        print(b[key].filled)
    for house in h:
        print(h[house].pluggedin)
