import random


def randclimber(repetitions, distdict, b, h):
    """
    A version of hillclimber which switches 2 random houses until no
    improvements are made for the set number of times
    """
    startover = 0
    while startover < repetitions:
        # Select 2 random houses
        h1 = random.choice(h)
        h2 = random.choice(h)
        if not h1.pluggedin == h2.pluggedin:
            if h1.output + b[h2.pluggedin.id].filled - h2.output < \
                    b[h2.pluggedin.id].capacity and \
                    h2.output + b[h1.pluggedin.id].filled - h1.output < \
                    b[h1.pluggedin.id].capacity:
                curprice = distdict[h1.id][h1.pluggedin.id] + distdict[h2.id][h2.pluggedin.id]
                swapprice = distdict[h1.id][h2.pluggedin.id] + distdict[h2.id][h1.pluggedin.id]
                if curprice > swapprice:
                    b[h1.pluggedin.id].filled += h2.output - h1.output
                    b[h2.pluggedin.id].filled += h1.output - h2.output
                    b[h2.pluggedin.id].connected.remove(h2)
                    b[h2.pluggedin.id].connected.append(h1)
                    b[h1.pluggedin.id].connected.remove(h1)
                    b[h1.pluggedin.id].connected.append(h2)
                    temporary = h2.pluggedin
                    h2.pluggedin = h1.pluggedin
                    h1.pluggedin = temporary

                    startover = 0
        startover += 1
