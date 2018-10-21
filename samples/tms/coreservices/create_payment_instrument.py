from cybersource_rest_client_python import *
import json


def create_payment_instrument():
    try:
        request = Body2()
    
        card_info = PaymentinstrumentsCard()
        card_info.expiration_month = "09"
        card_info.expiration_year = "2022"
        card_info.type = "visa"
        request.card=card_info.__dict__
    
        bill_to_info = PaymentinstrumentsBillTo()
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
        request.bill_to=bill_to_info.__dict__
    
        instument_identifier = PaymentinstrumentsInstrumentIdentifier()
    
        card_info = InstrumentidentifiersCard()
        card_info.number = "4111111111111111"
        instument_identifier.card = card_info.__dict__
        request.instrument_identifier=instument_identifier.__dict__
        message_body = del_none(request.__dict__)
        message_body = json.dumps(message_body)
        payment_instrument_obj = PaymentInstrumentApi()
        return payment_instrument_obj.paymentinstruments_post("93B32398-AD51-4CC2-A682-EA3E93614EB1", message_body)
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
    create_payment_instrument()
