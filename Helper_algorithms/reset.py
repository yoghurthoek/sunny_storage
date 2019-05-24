def reset(b, h):\
    """
    Helper-algorithm that resets the grid configuration to unplugged.
    """
    for key in h:
        h[key].pluggedin = False
    for key in b:
        b[key].filled = 0
        b[key].connected = []
