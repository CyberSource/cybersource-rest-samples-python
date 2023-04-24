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

def sale_using_emv_technology_with_contactless_read_for_card_present_enabled_acquirer():
    clientReferenceInformationCode = "123456"
    clientReferenceInformationPartnerOriginalTransactionId = "510be4aef90711e6acbc7d88388d803d"
    clientReferenceInformationPartner = Ptsv2paymentsClientReferenceInformationPartner(
        original_transaction_id = clientReferenceInformationPartnerOriginalTransactionId
    )

    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode,
        partner = clientReferenceInformationPartner.__dict__
    )

    processingInformationCapture = True
    processingInformationCommerceIndicator = "retail"
    processingInformation = Ptsv2paymentsProcessingInformation(
        capture = processingInformationCapture,
        commerce_indicator = processingInformationCommerceIndicator
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

    pointOfSaleInformationCatLevel = 1
    pointOfSaleInformationEntryMode = "contactless"
    pointOfSaleInformationTerminalCapability = 5
    pointOfSaleInformationEmvTags = "9F3303204000950500000000009F3704518823719F100706011103A000009F26081E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005F2A0208409F0306000000000000"
    pointOfSaleInformationEmvCardholderVerificationMethodUsed = 2
    pointOfSaleInformationEmvCardSequenceNumber = "1"
    pointOfSaleInformationEmvFallback = False
    pointOfSaleInformationEmv = Ptsv2paymentsPointOfSaleInformationEmv(
        tags = pointOfSaleInformationEmvTags,
        cardholder_verification_method_used = pointOfSaleInformationEmvCardholderVerificationMethodUsed,
        card_sequence_number = pointOfSaleInformationEmvCardSequenceNumber,
        fallback = pointOfSaleInformationEmvFallback
    )

    pointOfSaleInformationTrackData = "%B4111111111111111^TEST/CYBS         ^2012121019761100      00868000000?;"

    pointOfSaleInformationCardholderVerificationMethod = []
    pointOfSaleInformationCardholderVerificationMethod.append("pin")
    pointOfSaleInformationCardholderVerificationMethod.append("signature")

    pointOfSaleInformationTerminalInputCapability = []
    pointOfSaleInformationTerminalInputCapability.append("contact")
    pointOfSaleInformationTerminalInputCapability.append("contactless")
    pointOfSaleInformationTerminalInputCapability.append("keyed")
    pointOfSaleInformationTerminalInputCapability.append("swiped")
    pointOfSaleInformationTerminalCardCaptureCapability = "1"
    pointOfSaleInformationDeviceId = "123lkjdIOBK34981slviLI39bj"
    pointOfSaleInformationEncryptedKeySerialNumber = "01043191"
    pointOfSaleInformation = Ptsv2paymentsPointOfSaleInformation(
        cat_level = pointOfSaleInformationCatLevel,
        entry_mode = pointOfSaleInformationEntryMode,
        terminal_capability = pointOfSaleInformationTerminalCapability,
        emv = pointOfSaleInformationEmv.__dict__,
        track_data = pointOfSaleInformationTrackData,
        cardholder_verification_method = pointOfSaleInformationCardholderVerificationMethod,
        terminal_input_capability = pointOfSaleInformationTerminalInputCapability,
        terminal_card_capture_capability = pointOfSaleInformationTerminalCardCaptureCapability,
        device_id = pointOfSaleInformationDeviceId,
        encrypted_key_serial_number = pointOfSaleInformationEncryptedKeySerialNumber
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

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    sale_using_emv_technology_with_contactless_read_for_card_present_enabled_acquirer()
