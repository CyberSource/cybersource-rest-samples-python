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

def AzureIntermediateTesting():
    clientReferenceInformationCode = "12345678"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    paymentInformationCardNumber = "4111111111111111"
    paymentInformationCardExpirationMonth = "03"
    paymentInformationCardExpirationYear = "2031"
    paymentInformationCardType = "001"
    paymentInformationCard = Ptsv2paymentsidrefundsPaymentInformationCard(
        number = paymentInformationCardNumber,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear,
        type = paymentInformationCardType
    )

    paymentInformation = Ptsv2paymentsidrefundsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "200"
    orderInformationAmountDetailsCurrency = "usd"
    orderInformationAmountDetails = Ptsv2paymentsidcapturesOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Deo"
    orderInformationBillToAddress1 = "900 Metro Center Blvd"
    orderInformationBillToLocality = "Foster City"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToPostalCode = "48104-2201"
    orderInformationBillToCountry = "US"
    orderInformationBillToEmail = "test@cybs.com"
    orderInformationBillToPhoneNumber = "9321499232"
    orderInformationBillTo = Ptsv2paymentsidcapturesOrderInformationBillTo(
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        address1 = orderInformationBillToAddress1,
        locality = orderInformationBillToLocality,
        administrative_area = orderInformationBillToAdministrativeArea,
        postal_code = orderInformationBillToPostalCode,
        country = orderInformationBillToCountry,
        email = orderInformationBillToEmail,
        phone_number = orderInformationBillToPhoneNumber
    )

    orderInformation = Ptsv2paymentsidrefundsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    requestObj = CreateCreditRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_indermediate_configuration()
        api_instance = CreditApi(client_config)
        return_data, status, body = api_instance.create_credit(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling CreditApi->create_credit: %s\n" % e)

if __name__ == "__main__":
    AzureIntermediateTesting()
