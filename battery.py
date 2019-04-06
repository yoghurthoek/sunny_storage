class Battery(object):
        """Battery object """

        def __init__(self, id, x, y, capacity):
            self.id = id
            self.posx = x
            self.posy = y
            self.capacity = capacity

        def __str__(self):
            return f"Battery nr.{self.id}"
