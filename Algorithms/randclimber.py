import random
import copy


def Randclimber(initial, price, repetitions, distdict, b, h):
    """
    A version of hillclimber which switches random houses iteratively
    """
#     bestconf = initial
# # Set a while loop which changes random houses and keeps if the price is lower
#     for i in range(repetitions):
#         # Select random house
#         h1 = random.choice(random.choice(bestconf.batts))
#         h2 = random.choice(random.choice(bestconf.batts))
#         if not h1.pluggedin == h2.pluggedin:
#             if h1.output + b[h2.pluggedin.id].filled - h2.output < \
#                     b[h2.pluggedin.id].capacity and \
#                     h2.output + b[h1.pluggedin.id].filled - h1.output < \
#                     b[h1.pluggedin.id].capacity:
#                 curprice = distdict[h1][h1.pluggedin.id] + distdict[h2][h2.pluggedin.id]
#                 swapprice = distdict[h1][h2.pluggedin.id] + distdict[h2][h1.pluggedin.id]
#                 if curprice > swapprice:
#                     bestconf = change(h1, h2, b, bestconf)

    return


# def change(h1, h2, b, conf):
#
