from CyberSource import *
import samples.tms.coreservices.create_payment_instrument
import json
from data.Configaration import *

def update_payments_identifier():
    try:
        api_payment_response=samples.tms.coreservices.create_payment_instrument.create_payment_instrument()
        request = Body3()

        card_info = PaymentinstrumentsCard()
        card_info.expiration_month = "09"
        card_info.expiration_year = "2022"
        card_info.type = "visa"
        request.card = card_info.__dict__

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
        request.bill_to = bill_to_info.__dict__

        instument_identifier = PaymentinstrumentsInstrumentIdentifier()

        card_info = InstrumentidentifiersCard()
        card_info.number = "4111111111111111"
        instument_identifier.card = card_info.__dict__
        request.instrument_identifier = instument_identifier.__dict__

        message_body = json.dumps(request.__dict__)
        config_obj = Configaration()
        details_dict1 = config_obj.get_configaration()
        payment_instrument_obj = PaymentInstrumentApi(details_dict1)
        return_data, status, body = payment_instrument_obj.paymentinstruments_token_id_patch("93B32398-AD51-4CC2-A682-EA3E93614EB1",api_payment_response.id, message_body)
        print(status)
        print(body)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    update_payments_identifier()
