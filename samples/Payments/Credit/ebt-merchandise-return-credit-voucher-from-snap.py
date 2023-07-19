from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

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

def ebt_merchandise_return_credit_voucher_from_snap():
    clientReferenceInformationCode = "Merchandise Return / Credit Voucher from SNAP"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    processingInformationCommerceIndicator = "retail"
    processingInformationPurchaseOptionsIsElectronicBenefitsTransfer = True
    processingInformationPurchaseOptions = Ptsv2creditsProcessingInformationPurchaseOptions(
        is_electronic_benefits_transfer = processingInformationPurchaseOptionsIsElectronicBenefitsTransfer
    )

    processingInformationElectronicBenefitsTransferCategory = "FOOD"
    processingInformationElectronicBenefitsTransfer = Ptsv2creditsProcessingInformationElectronicBenefitsTransfer(
        category = processingInformationElectronicBenefitsTransferCategory
    )

    processingInformation = Ptsv2creditsProcessingInformation(
        commerce_indicator = processingInformationCommerceIndicator,
        purchase_options = processingInformationPurchaseOptions.__dict__,
        electronic_benefits_transfer = processingInformationElectronicBenefitsTransfer.__dict__
    )

    paymentInformationCardType = "001"
    paymentInformationCard = Ptsv2paymentsidrefundsPaymentInformationCard(
        type = paymentInformationCardType
    )

    paymentInformationPaymentTypeName = "CARD"
    paymentInformationPaymentTypeSubTypeName = "DEBIT"
    paymentInformationPaymentType = Ptsv2paymentsidrefundsPaymentInformationPaymentType(
        name = paymentInformationPaymentTypeName,
        sub_type_name = paymentInformationPaymentTypeSubTypeName
    )

    paymentInformation = Ptsv2paymentsidrefundsPaymentInformation(
        card = paymentInformationCard.__dict__,
        payment_type = paymentInformationPaymentType.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "204.00"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsidcapturesOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformation = Ptsv2paymentsidrefundsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    merchantInformationCategoryCode = 5411
    merchantInformation = Ptsv2paymentsidrefundsMerchantInformation(
        category_code = merchantInformationCategoryCode
    )

    pointOfSaleInformationEntryMode = "swiped"
    pointOfSaleInformationTerminalCapability = 4
    pointOfSaleInformationTrackData = "%B4111111111111111^JONES/JONES ^3112101976110000868000000?;4111111111111111=16121019761186800000?"
    pointOfSaleInformationPinBlockEncodingFormat = 1
    pointOfSaleInformationEncryptedPin = "52F20658C04DB351"
    pointOfSaleInformationEncryptedKeySerialNumber = "FFFF1B1D140000000005"
    pointOfSaleInformation = Ptsv2paymentsPointOfSaleInformation(
        entry_mode = pointOfSaleInformationEntryMode,
        terminal_capability = pointOfSaleInformationTerminalCapability,
        track_data = pointOfSaleInformationTrackData,
        pin_block_encoding_format = pointOfSaleInformationPinBlockEncodingFormat,
        encrypted_pin = pointOfSaleInformationEncryptedPin,
        encrypted_key_serial_number = pointOfSaleInformationEncryptedKeySerialNumber
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
        write_log_audit(e.status)
        print("\nException when calling CreditApi->create_credit: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    ebt_merchandise_return_credit_voucher_from_snap()