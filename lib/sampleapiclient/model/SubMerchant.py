class SubMerchant:
    def __init__(self):
        self.cardAcceptorID = None
        self.country = None
        self.phoneNumber = None
        self.address1 = None
        self.postalCode = None
        self.locality = None
        self.name = None
        self.administrativeArea = None
        self.region = None
        self.email = None

    def set_card_acceptor_id(self, value):
        self.cardAcceptorID = value

    def set_country(self, value):
        self.country = value

    def set_phone_number(self, value):
        self.phoneNumber = value

    def set_address1(self, value):
        self.address1 = value

    def set_postal_code(self, value):
        self.postalCode = value

    def set_locality(self, value):
        self.locality = value

    def set_name(self, value):
        self.name = value

    def set_administrative_area(self, value):
        self.administrativeArea = value

    def set_region(self, value):
        self.region = value

    def set_email(self, value):
        self.email = value
