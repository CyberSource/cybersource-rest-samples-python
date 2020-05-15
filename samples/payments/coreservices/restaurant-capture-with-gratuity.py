from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

authorization_path = os.path.join(os.getcwd(), "samples", "payments", "coreservices", "restaurant-authorization.py")
restaurant_authorization = SourceFileLoader("module.name", authorization_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def restaurant_capture_with_gratuity():
    authResponse = restaurant_authorization.restaurant_authorization()
    id = authResponse.id
    clientReferenceInformationCode = "1234567890"
    clientReferenceInformationPartnerThirdPartyCertificationNumber = "123456789012"
    clientReferenceInformationPartner = Ptsv2paymentsClientReferenceInformationPartner(
        third_party_certification_number = clientReferenceInformationPartnerThirdPartyCertificationNumber
    )

    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode,
        partner = clientReferenceInformationPartner.__dict__
    )

    processingInformationCapture = False
    processingInformationIndustryDataType = "restaurant"
    processingInformation = Ptsv2paymentsProcessingInformation(
        capture = processingInformationCapture,
        industry_data_type = processingInformationIndustryDataType
    )

    orderInformationAmountDetailsTotalAmount = "100"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetailsGratuityAmount = "11.50"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency,
        gratuity_amount = orderInformationAmountDetailsGratuityAmount
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    requestObj = CapturePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        order_information = orderInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CaptureApi(client_config)
        return_data, status, body = api_instance.capture_payment(requestObj, id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

if __name__ == "__main__":
    restaurant_capture_with_gratuity()
