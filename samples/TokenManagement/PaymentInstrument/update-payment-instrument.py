from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def update_payment_instrument():
    profileid = "93B32398-AD51-4CC2-A682-EA3E93614EB1"
    paymentInstrumentTokenId = "888454C31FB6150CE05340588D0AA9BE"

    cardExpirationMonth = "12"
    cardExpirationYear = "2031"
    cardType = "visa"
    card = Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentCard(
        expiration_month = cardExpirationMonth,
        expiration_year = cardExpirationYear,
        type = cardType
    )

    billToFirstName = "Jack"
    billToLastName = "Smith"
    billToCompany = "CyberSource"
    billToAddress1 = "1 Market St"
    billToLocality = "San Francisco"
    billToAdministrativeArea = "CA"
    billToPostalCode = "94105"
    billToCountry = "US"
    billToEmail = "updatedemail@cybs.com"
    billToPhoneNumber = "4158888674"
    billTo = Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentBillTo(
        first_name = billToFirstName,
        last_name = billToLastName,
        company = billToCompany,
        address1 = billToAddress1,
        locality = billToLocality,
        administrative_area = billToAdministrativeArea,
        postal_code = billToPostalCode,
        country = billToCountry,
        email = billToEmail,
        phone_number = billToPhoneNumber
    )

    instrumentIdentifierId = "7010000000016241111"
    instrumentIdentifier = Tmsv2tokenizeTokenInformationCustomerEmbeddedDefaultPaymentInstrumentInstrumentIdentifier(
        id = instrumentIdentifierId
    )

    requestObj = PatchPaymentInstrumentRequest(
        card = card.__dict__,
        bill_to = billTo.__dict__,
        instrument_identifier = instrumentIdentifier.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentInstrumentApi(client_config)
        return_data, status, body = api_instance.patch_payment_instrument(paymentInstrumentTokenId, requestObj, profile_id=profileid)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling PaymentInstrumentApi->patch_payment_instrument: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    update_payment_instrument()
