class Card:
    def __init__(self, card_type, half1, half2, card_id):
        self.card_type = card_type
        self.half1 = half1
        self.half2 = half2
        self.card_id = card_id

    def name(self):
        return self.half1.name() + ' ' + self.half2.name()
