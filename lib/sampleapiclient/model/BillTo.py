class BillTo:
    def __init__(self):
        self.country = None
        self.lastName = None
        self.address2 = None
        self.address1 = None
        self.postalCode = None
        self.locality = None
        self.administrativeArea = None
        self.firstName = None
        self.phoneNumber = None
        self.district = None
        self.buildingNumber = None
        self.company = None
        self.email = None

    def set_country(self, value):
        self.country = value

    def set_last_name(self, value):
        self.lastName = value

    def set_address2(self, value):
        self.address2 = value

    def set_address1(self, value):
        self.address1 = value

    def set_postal_code(self, value):
        self.postalCode = value

    def set_locality(self, value):
        self.locality = value

    def set_administrative_area(self, value):
        self.administrativeArea = value

    def set_first_name(self, value):
        self.firstName = value

    def set_phone_number(self, value):
        self.phoneNumber = value

    def set_district(self, value):
        self.district = value

    def set_building_number(self, value):
        self.buildingNumber = value

    def set_company(self, value):
        self.company = value

    def set_email(self, value):
        self.email = value
