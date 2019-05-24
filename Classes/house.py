class House(object):
    """House object"""

    def __init__(self, id, x, y, output):
        self.id = id
        self.posx = x
        self.posy = y
        self.output = output
        self.pluggedin = False

    def __str__(self):
        return f"house nr.{self.id}"
