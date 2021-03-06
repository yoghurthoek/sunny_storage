"""
Implements a branch 'n bound algorithm, but should only try neighbourhood 4
because the state space of the others is too big.
"""

from collections import deque
import pickle
import time
import operator


def branchnbound(startnode, b, h, distdict, dist, best):
    """
    Uses children to go in a depth-first manner through the state space.
    Returns the best price possible with this algorithm.
    """
    start = time.time()
    nrofnodes = 0
    timestoend = 0
    max = len(h)

    stack = deque([startnode])

    while stack:
        try:
            curnode = stack.pop()
            nrofnodes += 1

            if curnode.level == max:
                timestoend += 1
                if curnode.price < best.price:
                    best = curnode
                    print(best)
                    end = time.time()
                    print(end - start)
                continue

            if curnode.price + curnode.lowbound >= best.price:
                continue
            for node in children(curnode, b, h, distdict, dist, max):
                stack.append(node)
        except KeyboardInterrupt:
            break
    end = time.time()
    print(end - start)
    print(f"Nodes visited : {nrofnodes}")
    print(f"Times reached max depth : {timestoend}")

    return best


def children(node, b, h, distdict, dist, max):
    """
    Creates nodes for every battery
    """
    nodes = []
    for battery in b:
        if node.fill[battery][0] + h[node.level].output <= b[battery].capacity:
            cnode = pickle.loads(pickle.dumps(node, -1))
            cnode.batts[battery].append(cnode.level)
            cnode.fill[battery][0] += h[cnode.level].output
            cnode.price += distdict[cnode.level][battery] * 9
            cnode.lowbound -= dist[cnode.level][0][0] * 9
            cnode.level += 1
            nodes.append(cnode)
    nodes = sorted(nodes, key=operator.attrgetter('price'), reverse=True)
    return nodes
