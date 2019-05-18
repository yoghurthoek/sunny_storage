def nodetoclasses(b, h, node):
    # Set best configuration into the battery class to visualize
    for bat in b:
        for housekey in node.batts[bat]:
            b[bat].connected.append(h[housekey])

    # Set house connections to true, so does not get blacked out in visualize
    for bat in b:
        for house in b[bat].connected:
            house.pluggedin = b[bat]
