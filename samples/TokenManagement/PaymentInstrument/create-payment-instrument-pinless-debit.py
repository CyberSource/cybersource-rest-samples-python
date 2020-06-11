from CyberSource import *
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

def create_payment_instrument_pinless_debit():
    profileid = "93B32398-AD51-4CC2-A682-EA3E93614EB1"

    cardExpirationMonth = "09"
    cardExpirationYear = "2017"
    cardType = "visa"
    cardIssueNumber = "01"
    cardStartMonth = "01"
    cardStartYear = "2016"
    cardUseAs = "pinless debit"
    card = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedCard(
        expiration_month = cardExpirationMonth,
        expiration_year = cardExpirationYear,
        type = cardType,
        issue_number = cardIssueNumber,
        start_month = cardStartMonth,
        start_year = cardStartYear,
        use_as = cardUseAs
    )

    buyerInformationCompanyTaxID = "12345"
    buyerInformationCurrency = "USD"
    buyerInformation = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBuyerInformation(
        company_tax_id = buyerInformationCompanyTaxID,
        currency = buyerInformationCurrency
    )

    billToFirstName = "John"
    billToLastName = "Smith"
    billToCompany = "Cybersource"
    billToAddress1 = "8310 Capital of Texas Highwas North"
    billToAddress2 = "Bluffstone Drive"
    billToLocality = "Austin"
    billToAdministrativeArea = "TX"
    billToPostalCode = "78731"
    billToCountry = "US"
    billToEmail = "john.smith@test.com"
    billToPhoneNumber = "+44 2890447951"
    billTo = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedBillTo(
        first_name = billToFirstName,
        last_name = billToLastName,
        company = billToCompany,
        address1 = billToAddress1,
        address2 = billToAddress2,
        locality = billToLocality,
        administrative_area = billToAdministrativeArea,
        postal_code = billToPostalCode,
        country = billToCountry,
        email = billToEmail,
        phone_number = billToPhoneNumber
    )

    processingInformationBillPaymentProgramEnabled = True
    processingInformation = TmsV1InstrumentIdentifiersPaymentInstrumentsGet200ResponseEmbeddedProcessingInformation(
        bill_payment_program_enabled = processingInformationBillPaymentProgramEnabled
    )

    instrumentIdentifierCardNumber = "411111111111111"
    instrumentIdentifierCard = TmsV1InstrumentIdentifiersPost200ResponseCard(
        number = instrumentIdentifierCardNumber
    )

    instrumentIdentifier = Tmsv1paymentinstrumentsInstrumentIdentifier(
        card = instrumentIdentifierCard.__dict__
    )

    requestObj = CreatePaymentInstrumentRequest(
        card = card.__dict__,
        buyer_information = buyerInformation.__dict__,
        bill_to = billTo.__dict__,
        processing_information = processingInformation.__dict__,
        instrument_identifier = instrumentIdentifier.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentInstrumentApi(client_config)
        return_data, status, body = api_instance.create_payment_instrument(profileid, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentInstrumentApi->create_payment_instrument: %s\n" % e)

if __name__ == "__main__":
    create_payment_instrument_pinless_debit()
