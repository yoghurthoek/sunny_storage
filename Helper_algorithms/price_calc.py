def price_calc(b, distdict):

    price = 0
    for bat in b:
        for house in b[bat].connected:
            price += distdict[house.id][bat] * 9
        price += b[bat].price
    return price
