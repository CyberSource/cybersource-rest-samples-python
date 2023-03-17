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

def digital_payment_googlepay(flag):
    clientReferenceInformationCode = "TC_1231223"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    processingInformationCapture = False
    if flag:
        processingInformationCapture = True

    processingInformationPaymentSolution = "012"
    processingInformation = Ptsv2paymentsProcessingInformation(
        capture = processingInformationCapture,
        payment_solution = processingInformationPaymentSolution
    )

    paymentInformationTokenizedCardNumber = "4111111111111111"
    paymentInformationTokenizedCardExpirationMonth = "12"
    paymentInformationTokenizedCardExpirationYear = "2020"
    paymentInformationTokenizedCardCryptogram = "EHuWW9PiBkWvqE5juRwDzAUFBAk="
    paymentInformationTokenizedCardTransactionType = "1"
    paymentInformationTokenizedCard = Ptsv2paymentsPaymentInformationTokenizedCard(
        number = paymentInformationTokenizedCardNumber,
        expiration_month = paymentInformationTokenizedCardExpirationMonth,
        expiration_year = paymentInformationTokenizedCardExpirationYear,
        cryptogram = paymentInformationTokenizedCardCryptogram,
        transaction_type = paymentInformationTokenizedCardTransactionType
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        tokenized_card = paymentInformationTokenizedCard.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "20"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Deo"
    orderInformationBillToAddress1 = "901 Metro Center Blvd"
    orderInformationBillToLocality = "Foster City"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToPostalCode = "94404"
    orderInformationBillToCountry = "US"
    orderInformationBillToEmail = "test@cybs.com"
    orderInformationBillToPhoneNumber = "6504327113"
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

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
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

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    digital_payment_googlepay(False)
