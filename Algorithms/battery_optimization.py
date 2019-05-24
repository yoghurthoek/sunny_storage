def battery_optimization(b):
    """
    This program optimizes the location of batteries based on the location of
    all the houses that are connected to it.
    """
    positions = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for bat in b:
        i = 0
        for h in b[bat].connected:
            positions[bat][0] += b[bat].connected[i].posx
            positions[bat][1] += b[bat].connected[i].posy
            i += 1
        positions[bat][0] = round(positions[bat][0]/len(b[bat].connected))
        positions[bat][1] = round(positions[bat][1]/len(b[bat].connected))
        b[bat].posx = positions[bat][0]
        b[bat].posy = positions[bat][1]
