class Half:
    def __init__(self, color, dot):
        self.color = color
        self.dot = dot
        self.position = None
        self.coordinate = None

    def name(self):
        return self.color + self.dot
