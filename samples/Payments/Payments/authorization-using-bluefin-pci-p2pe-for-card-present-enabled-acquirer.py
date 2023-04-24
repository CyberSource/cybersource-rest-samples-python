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

def authorization_using_bluefin_pci_p2pe_for_card_present_enabled_acquirer():
    clientReferenceInformationCode = "demomerchant"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    processingInformationCapture = False
    processingInformationCommerceIndicator = "retail"
    processingInformation = Ptsv2paymentsProcessingInformation(
        capture = processingInformationCapture,
        commerce_indicator = processingInformationCommerceIndicator
    )

    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2050"
    paymentInformationCard = Ptsv2paymentsPaymentInformationCard(
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear
    )

    paymentInformationFluidDataDescriptor = "Ymx1ZWZpbg=="
    paymentInformationFluidDataValue = "02d700801f3c20008383252a363031312a2a2a2a2a2a2a2a303030395e46444d53202020202020202020202020202020202020202020205e323231322a2a2a2a2a2a2a2a3f2a3b363031312a2a2a2a2a2a2a2a303030393d323231322a2a2a2a2a2a2a2a3f2a7a75ad15d25217290c54b3d9d1c3868602136c68d339d52d98423391f3e631511d548fff08b414feac9ff6c6dede8fb09bae870e4e32f6f462d6a75fa0a178c3bd18d0d3ade21bc7a0ea687a2eef64551751e502d97cb98dc53ea55162cdfa395431323439323830303762994901000001a000731a8003"
    paymentInformationFluidData = Ptsv2paymentsPaymentInformationFluidData(
        descriptor = paymentInformationFluidDataDescriptor,
        value = paymentInformationFluidDataValue
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        card = paymentInformationCard.__dict__,
        fluid_data = paymentInformationFluidData.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "100.00"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Deo"
    orderInformationBillToAddress1 = "201 S. Division St."
    orderInformationBillToLocality = "Ann Arbor"
    orderInformationBillToAdministrativeArea = "MI"
    orderInformationBillToPostalCode = "48104-2201"
    orderInformationBillToCountry = "US"
    orderInformationBillToDistrict = "MI"
    orderInformationBillToEmail = "test@cybs.com"
    orderInformationBillToPhoneNumber = "999999999"
    orderInformationBillTo = Ptsv2paymentsOrderInformationBillTo(
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        address1 = orderInformationBillToAddress1,
        locality = orderInformationBillToLocality,
        administrative_area = orderInformationBillToAdministrativeArea,
        postal_code = orderInformationBillToPostalCode,
        country = orderInformationBillToCountry,
        district = orderInformationBillToDistrict,
        email = orderInformationBillToEmail,
        phone_number = orderInformationBillToPhoneNumber
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__
    )

    pointOfSaleInformationCatLevel = 1
    pointOfSaleInformationEntryMode = "keyed"
    pointOfSaleInformationTerminalCapability = 2
    pointOfSaleInformation = Ptsv2paymentsPointOfSaleInformation(
        cat_level = pointOfSaleInformationCatLevel,
        entry_mode = pointOfSaleInformationEntryMode,
        terminal_capability = pointOfSaleInformationTerminalCapability
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__,
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
    authorization_using_bluefin_pci_p2pe_for_card_present_enabled_acquirer()
