from collections import deque
import copy
import time


def bfs(startnode, b, h, distdict, best):
    """
    Implements a breadth first search, but should only try wijk5
    because it takes long
    """
    start = time.time()
    max = len(h)
    # Create a queue / or stack
    queue = deque([startnode])
    # while queue is not empty
    while queue:
        try:
            # Takes first out of queue
            curnode = queue.popleft()
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
    print(f"place ended : {curnode.level}")
    print(best.price)
    for bat in b:
        b[bat].connected = best.batts[bat]


def children(node, b, h, distdict, max):
    """
    Creates nodes for every battery
    """
    if node.level < max:
        for battery in b:
            # Prunes unallowed options
            if node.fill[battery][0] + h[node.level].output <= b[battery].capacity:
                # Makes copy of parent node and adds the house for every batt
                cnode = copy.deepcopy(node)
                cnode.batts[battery].append(h[cnode.level])
                cnode.fill[battery][0] += h[cnode.level].output
                cnode.price += distdict[cnode.level][battery] * 9
                cnode.level += 1
                yield cnode
