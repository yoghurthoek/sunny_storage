"""
Thanks to:
https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
https://gist.github.com/jamiees2/5531924
http://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

"""

# start en goal maar even gedefinieerd, dist is afstand tussen alle
# huizen en batteries

def astar(start, goal, grid):

    # create start and end node
    start_node = Noot(None, start)
    goal_node = Node(None, goal)
    start_node.g, start_node.h, start_node.f = 0
    end_node.g, end_node.h, end_node.f = 0
    # hoe de fack loopen over huisjes?
    # ideetjes: huizen in de openlist gooien en batts als goals
    # alsnog dan check inbouwen of het mogelijk is om deze huizen te koppelen
        # dat gaat echt oneindig lang duren en fakking veel geheugen kosten
    # of eerst koppelen en daarna snelste pad berekenen
        # maar dan wil je optimale sort functie
    # h is al gegeven in dist

    # Make open and closed list and append start_node to open
    open_list = []
    closed_list = []
    open_list.append(start_node)

    # Loop until you find the goal
    while len(open_list) > 0:

        # get current node
        current_node = open_list[0]

        # find the node with the least f in open list, call it "q"
        for noot in open_list:
            if noot.f < current_node.f:
                current_node = noot
                # nu gewoon aangepast -> ik wil iets anders

        # pop q off the open list
        # generate q's 8 successors and set their parents to q
        # for each successor:
            # if successor is goal -> break
            if current_node == end_node:
                break
                # maar ik wil hier nog wel de lengte van het pad?
            # if a node with the same position as successor is
                # open list, which has a lower f, skip this successor
            # if a node with same position as successor is in closed
                # list + lower f, skip this successor, add to open list
                open_list.append(successor)
        # end for loop

        # push q on the closed list
        open_list.pop(current_node)
        closed_list.append(current_node)

    # end while loop
