class Card:
    def __init__(self, id, half1, half2):
        self.id = id
        self.half1 = half1
        self.half2 = half2

    def name(self):
        return self.half1.name() + ' ' + self.half2.name()
