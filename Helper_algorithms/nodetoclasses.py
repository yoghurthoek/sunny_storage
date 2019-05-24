def nodetoclasses(b, h, node):
    """
    Helper-algorithm that is needed to transfer the information in the nodes
    to the grid.
    """

    for bat in b:
        for housekey in node.batts[bat]:
            b[bat].connected.append(h[housekey])

    for bat in b:
        for house in b[bat].connected:
            house.pluggedin = b[bat]
