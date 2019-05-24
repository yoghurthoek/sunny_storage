class Node(object):

    def __init__(self):
        # to access battery 1 self.batts[0].append()
        self.batts = [[], [], [], [], []]
        self.fill = [[0], [0], [0], [0], [0]]
        self.price = 0

        # bnb only
        self.level = 0
        self.lowbound = 0

    def fillnode(self, b, h, price):
        for battery in b:
            self.fill[battery][0] = b[battery].filled
        for nr in h:
            self.batts[h[nr].pluggedin.id].append(h[nr].id)
        self.price = price

    def __str__(self):
        return f"price: {self.price}"
