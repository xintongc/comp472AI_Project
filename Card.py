import copy

class Card:
    def __init__(self, card_type, half1, half2, card_id):
        self.card_type = card_type
        self.half1 = half1
        self.half2 = half2
        self.card_id = card_id

    def name(self):
        return self.half1.name() + ' ' + self.half2.name()

    def set_half_coordinate(self, card_type, coordinate): # [y, x] for each coordinate --> half1
        if card_type == 1:
            self.half1.coordinate = copy.copy(coordinate);
            coordinate[1] = coordinate[1] + 1;
            self.half2.coordinate = coordinate
        if card_type == 2:
            self.half1.coordinate = copy.copy(coordinate);
            coordinate[0] = coordinate[0] - 1;
            self.half2.coordinate = coordinate
        if card_type == 3:
            self.half1.coordinate = copy.copy(coordinate);
            coordinate[1] = coordinate[1] - 1;
            self.half2.coordinate = coordinate
        if card_type == 4:
            self.half1.coordinate = copy.copy(coordinate);
            coordinate[0] = coordinate[0] + 1;
            self.half2.coordinate = coordinate
        if card_type == 5:
            self.half1.coordinate = copy.copy(coordinate);
            coordinate[1] = coordinate[1] + 1;
            self.half2.coordinate = coordinate
        if card_type == 6:
            self.half1.coordinate = copy.copy(coordinate);
            coordinate[0] = coordinate[0] - 1;
            self.half2.coordinate = coordinate
        if card_type == 7:
            self.half1.coordinate = copy.copy(coordinate);
            coordinate[1] = coordinate[1] - 1;
            self.half2.coordinate = coordinate
        if card_type == 8:
            self.half1.coordinate = copy.copy(coordinate);
            coordinate[0] = coordinate[0] + 1;
            self.half2.coordinate = coordinate

        #boundary check, if false, it results an illegal state
        if self.half1.coordinate[0] < 1 or self.half2.coordinate[0] < 1 or self.half1.coordinate[0] > 12 or self.half2.coordinate[0] > 12:
            return False
        elif self.half1.coordinate[1] < 0 or self.half2.coordinate[1] < 0 or self.half1.coordinate[1] > 7 or self.half2.coordinate[1] > 7:
            return False
        else:
            return True