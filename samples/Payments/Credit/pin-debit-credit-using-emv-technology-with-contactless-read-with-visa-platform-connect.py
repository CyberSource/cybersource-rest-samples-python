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

def pin_debit_credit_using_emv_technology_with_contactless_read_with_visa_platform_connect():
    clientReferenceInformationCode = "2.2 Credit"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    processingInformationCommerceIndicator = "retail"
    processingInformation = Ptsv2creditsProcessingInformation(
        commerce_indicator = processingInformationCommerceIndicator
    )

    paymentInformationPaymentTypeName = "CARD"
    paymentInformationPaymentTypeSubTypeName = "DEBIT"
    paymentInformationPaymentType = Ptsv2paymentsidrefundsPaymentInformationPaymentType(
        name = paymentInformationPaymentTypeName,
        sub_type_name = paymentInformationPaymentTypeSubTypeName
    )

    paymentInformation = Ptsv2paymentsidrefundsPaymentInformation(
        payment_type = paymentInformationPaymentType.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "202.00"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsidcapturesOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsidrefundsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    merchantInformation = Ptsv2paymentsidrefundsMerchantInformation(
    )

    pointOfSaleInformationEntryMode = "contactless"
    pointOfSaleInformationTerminalCapability = 4
    pointOfSaleInformationEmvTags = "9F3303204000950500000000009F3704518823719F100706011103A000009F26081E1756ED0E2134E29F36020015820200009C01009F1A0208409A030006219F02060000000020005F2A0208409F0306000000000000"
    pointOfSaleInformationEmvCardSequenceNumber = "1"
    pointOfSaleInformationEmvFallback = False
    pointOfSaleInformationEmv = Ptsv2paymentsPointOfSaleInformationEmv(
        tags = pointOfSaleInformationEmvTags,
        card_sequence_number = pointOfSaleInformationEmvCardSequenceNumber,
        fallback = pointOfSaleInformationEmvFallback
    )

    pointOfSaleInformationTrackData = "%B4111111111111111^JONES/JONES ^3112101976110000868000000?;4111111111111111=16121019761186800000?"
    pointOfSaleInformation = Ptsv2paymentsPointOfSaleInformation(
        entry_mode = pointOfSaleInformationEntryMode,
        terminal_capability = pointOfSaleInformationTerminalCapability,
        emv = pointOfSaleInformationEmv.__dict__,
        track_data = pointOfSaleInformationTrackData
    )

    requestObj = CreateCreditRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__,
        merchant_information = merchantInformation.__dict__,
        point_of_sale_information = pointOfSaleInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_alternative_configuration()
        api_instance = CreditApi(client_config)
        return_data, status, body = api_instance.create_credit(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling CreditApi->create_credit: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    pin_debit_credit_using_emv_technology_with_contactless_read_with_visa_platform_connect()
