class Half:
    def __init__(self, color, dot):
        self.color = color
        self.dot = dot
        self.position = None
        self.coordinate = None

    def name(self):
        return self.color + self.dot

    def match_with_role_token(self, role_token):
        if role_token == self.color or role_token == self.dot:
            return True
        else:
            return False
