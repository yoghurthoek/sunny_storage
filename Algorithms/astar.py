"""
Thanks to:
https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
https://gist.github.com/jamiees2/5531924
http://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2


Werkt nog van geen kant :D, want problems:
    # hoe de fack loopen over huisjes?
    # ideetjes: huizen in de openlist gooien en batts als goals
    # alsnog dan check inbouwen of het mogelijk is om deze huizen te koppelen
        # dat gaat echt oneindig lang duren en fakking veel geheugen kosten
    # of eerst koppelen en daarna snelste pad berekenen
        # maar dan wil je optimale sort functie

open list: huis connecten met batt (kies beste optie)?

"""

# start en goal maar even gedefinieerd, dist is afstand tussen alle
# huizen en batteries

def astar(start, grid):
    hellepies
