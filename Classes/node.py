class Node(object):

    def __init__(self):
        # to access battery 1 self.batts[0].append()
        self.batts = [[], [], [], [], []]
        self.level = 0
        self.fill = [[0], [0], [0], [0], [0]]
        self.price = 0
