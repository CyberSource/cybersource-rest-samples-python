class AggregatorInformation:
    def __init__(self):
        self.subMerchant = None
        self.name = None
        self.aggregatorID = None

    def set_submerchant(self, value):
        self.subMerchant = value

    def set_name(self, value):
        self.name = value

    def set_aggregator_id(self, value):
        self.aggregatorID = value
