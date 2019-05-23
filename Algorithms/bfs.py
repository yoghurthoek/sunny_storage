from collections import deque
import pickle
import time


def bfs(startnode, b, h, distdict, best):
    """
    Implements a breadth first search/branch n bound, but should only try wijk5
    because it takes long
    """
    start = time.time()
    max = len(h)
    nrofnodes = 0
    # Create a queue / or stack
    queue = deque([startnode])
    # while queue is not empty
    while queue:
        try:
            # Takes first out of queue
            curnode = queue.popleft()
            nrofnodes += 1
            # When you've reached a possible solution checks if better
            if curnode.level == max:
                if curnode.price < best.price:
                    best = curnode
                    print(best)
                    end = time.time()
                    print(end - start)
            # branch and bound??
            if curnode.price > best.price:
                continue
            for node in children(curnode, b, h, distdict, max):
                queue.append(node)
        except KeyboardInterrupt:
            break
    end = time.time()
    print(end - start)
    print(f"Nodes visited: {nrofnodes}")
    print(f"Depth ended: {curnode.level}")
    print(best.price)

    return best


def children(node, b, h, distdict, max):
    """
    Creates nodes for every battery
    """
    if node.level < max:
        for battery in b:
            # Prunes unallowed options
            if node.fill[battery][0] + \
                    h[node.level].output <= b[battery].capacity:
                # Makes copy of parent node and adds the house for every batt
                cnode = pickle.loads(pickle.dumps(node, -1))
                cnode.batts[battery].append(cnode.level)
                cnode.fill[battery][0] += h[cnode.level].output
                cnode.price += distdict[cnode.level][battery] * 9
                cnode.level += 1
                yield cnode
