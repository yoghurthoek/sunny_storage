def reset(b, h):
    for key in h:
        h[key].pluggedin = False
    for key in b:
        b[key].filled = 0
        b[key].connected = []
