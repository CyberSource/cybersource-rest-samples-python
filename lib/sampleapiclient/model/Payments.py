class Payments:
    def __init__(self):
        self.clientReferenceInformation = None

        self.processingInformation = None
        self.aggregatorInformation = None
        self.orderInformation = None
        self.paymentInformation = None

    def set_client_reference_information(self, value):
        self.clientReferenceInformation = value

    def set_processing_information(self, value):
        self.processingInformation = value

    def set_aggregator_information(self, value):
        self.aggregatorInformation = value

    def set_order_information(self, value):
        self.orderInformation = value

    def set_payment_information(self, value):
        self.paymentInformation = value
