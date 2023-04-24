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

def payment_with_flex_tokencreate_permanent_tms_token():
    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )


    processingInformationActionList = []
    processingInformationActionList.append("TOKEN_CREATE")

    processingInformationActionTokenTypes = []
    processingInformationActionTokenTypes.append("customer")
    processingInformationActionTokenTypes.append("paymentInstrument")
    processingInformationActionTokenTypes.append("shippingAddress")
    processingInformationCapture = False
    processingInformation = Ptsv2paymentsProcessingInformation(
        action_list = processingInformationActionList,
        action_token_types = processingInformationActionTokenTypes,
        capture = processingInformationCapture
    )

    orderInformationAmountDetailsTotalAmount = "102.21"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Doe"
    orderInformationBillToAddress1 = "1 Market St"
    orderInformationBillToLocality = "san francisco"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToPostalCode = "94105"
    orderInformationBillToCountry = "US"
    orderInformationBillToEmail = "test@cybs.com"
    orderInformationBillToPhoneNumber = "4158880000"
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

    orderInformationShipToFirstName = "John"
    orderInformationShipToLastName = "Doe"
    orderInformationShipToAddress1 = "1 Market St"
    orderInformationShipToLocality = "san francisco"
    orderInformationShipToAdministrativeArea = "CA"
    orderInformationShipToPostalCode = "94105"
    orderInformationShipToCountry = "US"
    orderInformationShipTo = Ptsv2paymentsOrderInformationShipTo(
        first_name = orderInformationShipToFirstName,
        last_name = orderInformationShipToLastName,
        address1 = orderInformationShipToAddress1,
        locality = orderInformationShipToLocality,
        administrative_area = orderInformationShipToAdministrativeArea,
        postal_code = orderInformationShipToPostalCode,
        country = orderInformationShipToCountry
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__,
        ship_to = orderInformationShipTo.__dict__
    )

    tokenInformationTransientTokenJwt = "eyJraWQiOiIwODVLd3ZiZHVqZW1DZDN3UnNxVFg3RG5nZzlZVk04NiIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjp7Im51bWJlciI6IjQxMTExMVhYWFhYWDExMTEiLCJ0eXBlIjoiMDAxIn0sImlzcyI6IkZsZXgvMDgiLCJleHAiOjE1OTU2MjAxNTQsInR5cGUiOiJtZi0wLjExLjAiLCJpYXQiOjE1OTU2MTkyNTQsImp0aSI6IjFFMTlWWVlBUEFEUllPSzREUUM1NFhRN1hUVTlYN01YSzBCNTc5UFhCUU1HUUExVU1MOFI1RjFCM0IzQTU4MkIifQ.NKSM8zuT9TQC2OIUxIFJQk4HKeHhj_RGWmEqOQhBi0TIynt_kCIup1UVtAlhPzUfPWLwRrUVXnA9dyjLt_Q-pFZnvZ2lVANbiOq_R0us88MkM_mqaELuInCwxFeFZKA4gl8XmDFARgX1aJttC19Le6NYOhK2gpMrV4i0yz-IkbScsk0_vCH3raayNacFU2Wy9xei6H_V0yw2GeOs7kF6wdtMvBNw_uoLXd77LGE3LmV7z1TpJcG1SXy2s0bwYhEvkQGnrq6FfY8w7-UkDBWT1GhU3ZVP4y7h0l1WEX2xqf_ze25ZiYJQfWrEWPBHXRubOpAuaf4rfeZei0mRwPU-sQ"
    tokenInformation = Ptsv2paymentsTokenInformation(
        transient_token_jwt = tokenInformationTransientTokenJwt
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        order_information = orderInformation.__dict__,
        token_information = tokenInformation.__dict__
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
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    payment_with_flex_tokencreate_permanent_tms_token()
