from collections import deque
import copy


def bfs(startnode, b, h, distdict, best):
    """
    Implements a depth first search, but should only try wijk5
    because it takes long
    """
    max = len(h)
    # Create an archive(maybe a set)
    archive = []
    # Create a queue
    queue = deque([startnode])
    # while queue is not empty
    while queue:
        try:
            curnode = queue.popleft()
            archive.append(curnode)
            if curnode.level == max:
                if curnode.price < best.price:
                    best = curnode
                    print(best)
            for node in children(curnode, b, h, distdict, max):
                queue.append(node)
        except KeyboardInterrupt:
            break
    print(f"place ended : {curnode.level}")
    print(len(archive))
    print(best.price)
    for bat in b:
        b[bat].connected = best.batts[bat]


def children(node, b, h, distdict, max):
    # Don't set allowed node.level too high unless you have the time and memory
    if node.level < max:
        for battery in b:
            if node.fill[battery][0] + h[node.level].output <= b[battery].capacity:
                cnode = copy.deepcopy(node)
                cnode.batts[battery].append(h[cnode.level])
                cnode.fill[battery][0] += h[cnode.level].output
                cnode.price += distdict[cnode.level][battery] * 9
                cnode.level += 1
                yield cnode
