from CyberSource import *
import retrieve_payment_instrument
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def update_payments_identifier():
    try:
        api_payment_response=retrieve_payment_instrument.retrieve_payment_instrument()
        request = Body3()

        card_info = Tmsv1paymentinstrumentsCard()
        card_info.expiration_month = "09"
        card_info.expiration_year = "2022"
        card_info.type = "visa"
        request.card = card_info.__dict__

        bill_to_info = Tmsv1paymentinstrumentsBillTo()
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

        card_info = Tmsv1instrumentidentifiersCard()
        card_info.number = "4111111111111111"
        instument_identifier.card = card_info.__dict__
        request.instrument_identifier = instument_identifier.__dict__
        message_body = del_none(request.__dict__)
        message_body = json.dumps(message_body)
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()

        payment_instrument_obj = PaymentInstrumentsApi(details_dict1)
        return_data, status, body = payment_instrument_obj.tms_v1_paymentinstruments_token_id_patch("93B32398-AD51-4CC2-A682-EA3E93614EB1",api_payment_response.id, message_body)
        print(status)
        print(body)

    except Exception as e:
        print(e)


def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d
if __name__ == "__main__":
    update_payments_identifier()
