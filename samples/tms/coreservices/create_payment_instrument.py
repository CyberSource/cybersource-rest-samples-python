from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_payment_instrument():
    try:
        # Setting the json message body
        request = CreatePaymentInstrumentRequest()
        card_info = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedCard("09","2022","visa")
        request.card = card_info.__dict__

        bill_to_info = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBillTo()
        bill_to_info.first_name = "John"
        bill_to_info.last_name = "Deo"
        bill_to_info.company = "CyberSource"
        bill_to_info.address1 = "12 Main Street"
        bill_to_info.address2 = "20 My Street"
        bill_to_info.locality = "Foster City"
        bill_to_info.administrative_area = "CA"
        bill_to_info.postal_code = "90200"
        bill_to_info.country = "US"
        bill_to_info.email = "john.smith@example.com"
        bill_to_info.phone_number = "555123456"
        request.bill_to = bill_to_info.__dict__

        instument_identifier = Tmsv1paymentinstrumentsInstrumentIdentifier()
        card_info = TmsV1InstrumentIdentifiersPost200ResponseCard()
        card_info.number = "4111111111111111"
        instument_identifier.card = card_info.__dict__
        request.instrument_identifier = instument_identifier.__dict__
        message_body = del_none(request.__dict__)
        message_body = json.dumps(message_body)

        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        payment_instrument_obj = PaymentInstrumentApi(details_dict1)
        return_data, status, body = payment_instrument_obj.create_payment_instrument(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        return return_data
    except Exception as e:
        print("Exception when calling PaymentInstrumentApi->create_payment_instrument: %s\n" % e)


# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


if __name__ == "__main__":
    create_payment_instrument()
