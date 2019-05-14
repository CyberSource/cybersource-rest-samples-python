class Card:
    def __init__(self):
        self.expirationYear = None
        self.number = None
        self.securityCode = None
        self.expirationMonth = None
        self.type = None

    def set_espiration_year(self, value):
        self.expirationYear = value

    def set_number(self, value):
        self.number = value

    def set_security_code(self, value):
        self.securityCode = value

    def set_expiration_month(self, value):
        self.expirationMonth = value

    def set_type(self, value):
        self.type = value
