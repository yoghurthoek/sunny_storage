from collections import deque
import pickle
import time
import operator


def branchnbound(startnode, b, h, distdict, dist, best):
    """
    This algorithm creates a stack with all possible configurations. It is also
    an exhaustive algorithm with a (very) long runtime. We tried to prune the
    stack, making it a branch 'n bound algorithm. Should only try wijk 5.
    """
    start = time.time()
    nrofnodes = 0
    timestoend = 0
    max = len(h)

    # Create a queue / or stack
    stack = deque([startnode])

    # while stack is not empty
    while stack:
        try:
            # if want to try depth first use pop for breadth use popleft
            curnode = stack.pop()
            nrofnodes += 1

            # When you've reached a possible solution checks if better
            if curnode.level == max:
                timestoend += 1
                if curnode.price < best.price:
                    best = curnode
                    print(best)
                    end = time.time()
                    print(end - start)
                continue
            if curnode.level == 0:
                print("back to the start")

            # Short version of branch and bound to maybe improve performance
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
    print(best.price)

    return best


def children(node, b, h, distdict, dist, max):
    """
    Creates nodes for every battery
    """
    nodes = []
    for battery in b:
        # Prunes unallowed options
        if node.fill[battery][0] + h[node.level].output <= b[battery].capacity:
            # Makes copy of parent node and adds the house for every batt
            cnode = pickle.loads(pickle.dumps(node, -1))
            cnode.batts[battery].append(cnode.level)
            cnode.fill[battery][0] += h[cnode.level].output
            cnode.price += distdict[cnode.level][battery] * 9
            cnode.lowbound -= dist[cnode.level][0][0] * 9
            cnode.level += 1
            nodes.append(cnode)
    # Sorts nodes in reverse so the lowest price gets explored first
    nodes = sorted(nodes, key=operator.attrgetter('price'), reverse=True)
    return nodes
