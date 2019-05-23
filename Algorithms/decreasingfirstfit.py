def decreasingfirstfit(grid, b, h):
    """
    Connects houses to batteries by trying to fit into first battery and
    if not possible try the next
    """
    for nr in h:
        for key in b:
            if h[nr].output + b[key].filled < b[key].capacity:
                b[key].connected.append(h[nr])
                b[key].filled += h[nr].output
                h[nr].pluggedin = b[key]
                break

    for key in b:
        print(b[key].filled)
    for house in h:
        print(h[house].pluggedin)
