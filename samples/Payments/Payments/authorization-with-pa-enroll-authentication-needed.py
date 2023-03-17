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

def authorization_with_pa_enroll_authentication_needed():
    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )


    processingInformationActionList = []
    processingInformationActionList.append("CONSUMER_AUTHENTICATION")
    processingInformationCapture = False
    processingInformation = Ptsv2paymentsProcessingInformation(
        action_list = processingInformationActionList,
        capture = processingInformationCapture
    )

    paymentInformationCardNumber = "4000000000001091"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2023"
    paymentInformationCard = Ptsv2paymentsPaymentInformationCard(
        number = paymentInformationCardNumber,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        card = paymentInformationCard.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "100.00"
    orderInformationAmountDetailsCurrency = "usd"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Smith"
    orderInformationBillToAddress1 = "201 S. Division St._1"
    orderInformationBillToAddress2 = "Suite 500"
    orderInformationBillToLocality = "Foster City"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToPostalCode = "94404"
    orderInformationBillToCountry = "US"
    orderInformationBillToEmail = "accept@cybersource.com"
    orderInformationBillToPhoneNumber = "6504327113"
    orderInformationBillTo = Ptsv2paymentsOrderInformationBillTo(
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        address1 = orderInformationBillToAddress1,
        address2 = orderInformationBillToAddress2,
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

    consumerAuthenticationInformationRequestorId = "123123197675"
    consumerAuthenticationInformationReferenceId = "CybsCruiseTester-8ac0b02f"
    consumerAuthenticationInformation = Ptsv2paymentsConsumerAuthenticationInformation(
        requestor_id = consumerAuthenticationInformationRequestorId,
        reference_id = consumerAuthenticationInformationReferenceId
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__,
        consumer_authentication_information = consumerAuthenticationInformation.__dict__
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
    authorization_with_pa_enroll_authentication_needed()
