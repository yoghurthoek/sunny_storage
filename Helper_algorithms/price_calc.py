def price_calc(b, distdict):

    price = 0
    for bat in b:
        for house in b[bat].connected:
            price += distdict[house.id][house.pluggedin.id] * 9
    return price
