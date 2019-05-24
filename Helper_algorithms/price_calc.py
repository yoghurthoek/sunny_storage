def price_calc(b, distdict):
    """
    Helper-algorithm that is needed to calculate the price of a configuration.
    """

    price = 0
    for bat in b:
        for house in b[bat].connected:
            price += distdict[house.id][bat] * 9
        price += b[bat].price
    return price
