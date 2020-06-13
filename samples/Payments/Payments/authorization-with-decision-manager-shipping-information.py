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

def authorization_with_decision_manager_shipping_information():
    clientReferenceInformationCode = "54323007"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    paymentInformationCardNumber = "4444444444444448"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2020"
    paymentInformationCard = Ptsv2paymentsPaymentInformationCard(
        number = paymentInformationCardNumber,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "144.14"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToFirstName = "James"
    orderInformationBillToLastName = "Smith"
    orderInformationBillToAddress1 = "96, powers street"
    orderInformationBillToLocality = "Clearwater milford"
    orderInformationBillToAdministrativeArea = "NH"
    orderInformationBillToPostalCode = "03055"
    orderInformationBillToCountry = "US"
    orderInformationBillToEmail = "test@visa.com"
    orderInformationBillToPhoneNumber = "7606160717"
    orderInformationBillTo = Ptsv2paymentsOrderInformationBillTo(
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

    orderInformationShipToFirstName = "James"
    orderInformationShipToLastName = "Smith"
    orderInformationShipToAddress1 = "96, powers street"
    orderInformationShipToLocality = "Clearwater milford"
    orderInformationShipToAdministrativeArea = "KA"
    orderInformationShipToPostalCode = "560056"
    orderInformationShipToCountry = "IN"
    orderInformationShipToPhoneNumber = "7606160717"
    orderInformationShipTo = Ptsv2paymentsOrderInformationShipTo(
        first_name = orderInformationShipToFirstName,
        last_name = orderInformationShipToLastName,
        address1 = orderInformationShipToAddress1,
        locality = orderInformationShipToLocality,
        administrative_area = orderInformationShipToAdministrativeArea,
        postal_code = orderInformationShipToPostalCode,
        country = orderInformationShipToCountry,
        phone_number = orderInformationShipToPhoneNumber
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__,
        ship_to = orderInformationShipTo.__dict__
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentsApi(client_config)
        return_data, status, body = api_instance.create_payment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

if __name__ == "__main__":
    authorization_with_decision_manager_shipping_information()
