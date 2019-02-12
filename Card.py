class Card:
    def __init__(self, index_in_cardtype, half1, half2, card_id):
        self.index_in_cardtype = index_in_cardtype
        self.half1 = half1
        self.half2 = half2
        self.card_id = card_id

    def name(self):
        return self.half1.name() + ' ' + self.half2.name()
