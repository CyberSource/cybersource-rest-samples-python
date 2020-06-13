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

def restaurant_authorization():
    clientReferenceInformationCode = "demomerchant"
    clientReferenceInformationPartnerThirdPartyCertificationNumber = "123456789012"
    clientReferenceInformationPartner = Ptsv2paymentsClientReferenceInformationPartner(
        third_party_certification_number = clientReferenceInformationPartnerThirdPartyCertificationNumber
    )

    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode,
        partner = clientReferenceInformationPartner.__dict__
    )

    processingInformationCapture = False
    processingInformationCommerceIndicator = "retail"
    processingInformationAuthorizationOptionsPartialAuthIndicator = True
    processingInformationAuthorizationOptionsIgnoreAvsResult = False
    processingInformationAuthorizationOptionsIgnoreCvResult = False
    processingInformationAuthorizationOptions = Ptsv2paymentsProcessingInformationAuthorizationOptions(
        partial_auth_indicator = processingInformationAuthorizationOptionsPartialAuthIndicator,
        ignore_avs_result = processingInformationAuthorizationOptionsIgnoreAvsResult,
        ignore_cv_result = processingInformationAuthorizationOptionsIgnoreCvResult
    )

    processingInformation = Ptsv2paymentsProcessingInformation(
        capture = processingInformationCapture,
        commerce_indicator = processingInformationCommerceIndicator,
        authorization_options = processingInformationAuthorizationOptions.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "100.00"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    pointOfSaleInformationEntryMode = "swiped"
    pointOfSaleInformationTerminalCapability = 2
    pointOfSaleInformationTrackData = "%B38000000000006^TEST/CYBS         ^2012121019761100      00868000000?"
    pointOfSaleInformation = Ptsv2paymentsPointOfSaleInformation(
        entry_mode = pointOfSaleInformationEntryMode,
        terminal_capability = pointOfSaleInformationTerminalCapability,
        track_data = pointOfSaleInformationTrackData
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        order_information = orderInformation.__dict__,
        point_of_sale_information = pointOfSaleInformation.__dict__
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
    restaurant_authorization()
