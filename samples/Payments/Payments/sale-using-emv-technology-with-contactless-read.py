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

def sale_using_emv_technology_with_contactless_read():
    clientReferenceInformationCode = "123456"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
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

    pointOfSaleInformationCatLevel = 2
    pointOfSaleInformationEntryMode = "contactless"
    pointOfSaleInformationTerminalCapability = 5
    pointOfSaleInformationEmvTags = "9F3303204000950500000000009F3704518823719F100706011103A000009F26081E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005F2A0208409F0306000000000000"
    pointOfSaleInformationEmvCardSequenceNumber = "1"
    pointOfSaleInformationEmvFallback = False
    pointOfSaleInformationEmv = Ptsv2paymentsPointOfSaleInformationEmv(
        tags = pointOfSaleInformationEmvTags,
        card_sequence_number = pointOfSaleInformationEmvCardSequenceNumber,
        fallback = pointOfSaleInformationEmvFallback
    )

    pointOfSaleInformationTrackData = "%B38000000000006^TEST/CYBS         ^2012121019761100      00868000000?;38000000000006=20121210197611868000?"
    pointOfSaleInformation = Ptsv2paymentsPointOfSaleInformation(
        cat_level = pointOfSaleInformationCatLevel,
        entry_mode = pointOfSaleInformationEntryMode,
        terminal_capability = pointOfSaleInformationTerminalCapability,
        emv = pointOfSaleInformationEmv.__dict__,
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
    sale_using_emv_technology_with_contactless_read()
