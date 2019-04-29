"""
Simpelere dfs
"""

from collections import deque
import copy
import time
import operator


def dfs(startnode, b, h, distdict, best):
    """
    Implements a depth first search
    because it takes long
    """
    start = time.time()
    max = len(h)
    # Create a queue / or stack
    stack = deque([startnode])
    # while queue is not empty
    while stack:
        try:
            # if want to try depth first use pop for breadth use popleft
            curnode = stack.pop()
            # When you've reached a possible solution checks if better
            if curnode.level == max:
                if curnode.price < best.price:
                    best = curnode
                    print(best)
                    end = time.time()
                    print(end - start)
                continue
            # Short version of branch and bound to maybe improve performance
            if curnode.price > best.price:
                continue
            stack.extend(children(curnode, b, h, distdict, max))
        except KeyboardInterrupt:
            break
    end = time.time()
    print(end - start)
    print(f"place ended : {curnode.level}")
    print(best.price)
    for bat in b:
        b[bat].connected = best.batts[bat]


def children(node, b, h, distdict, max):
    """
    Creates nodes for every battery
    """
    nodes = []
    for battery in b:
        # Prunes unallowed options
        if node.fill[battery][0] + h[node.level].output <= b[battery].capacity:
            # Makes copy of parent node and adds the house for every batt
            cnode = copy.deepcopy(node)
            cnode.batts[battery].append(h[cnode.level])
            cnode.fill[battery][0] += h[cnode.level].output
            cnode.price += distdict[cnode.level][battery] * 9
            cnode.level += 1
            nodes.append(cnode)
    # Sorts nodes in reverse so the lowest price gets explored first
    nodes = sorted(nodes, key=operator.attrgetter('price'), reverse=True)
    return nodes
