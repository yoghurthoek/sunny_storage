class Noot(object):
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.h = 0
        self.g = 0
        self.f = 0

    def move_cost(self, other):
        return self.position == other.position
