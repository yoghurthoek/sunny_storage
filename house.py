class House(object):
        """House object housing house things"""

        def __init__(self, id, x, y, output):
            self.id = id
            self.posx = x
            self.posy = y
            self.output = output

        def __str__(self):
            return f"house nr.{self.id}"
