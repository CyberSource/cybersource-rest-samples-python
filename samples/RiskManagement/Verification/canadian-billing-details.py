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

def canadian_billing_details():
    clientReferenceInformationCode = "addressEg"
    clientReferenceInformationComments = "dav-All fields"
    clientReferenceInformation = Riskv1decisionsClientReferenceInformation(
        code = clientReferenceInformationCode,
        comments = clientReferenceInformationComments
    )

    orderInformationBillToAddress1 = "1650 Burton Ave"
    orderInformationBillToAddress2 = ""
    orderInformationBillToAddress3 = ""
    orderInformationBillToAddress4 = ""
    orderInformationBillToAdministrativeArea = "BC"
    orderInformationBillToCountry = "CA"
    orderInformationBillToLocality = "VICTORIA"
    orderInformationBillToPostalCode = "V8T 2N6"
    orderInformationBillTo = Riskv1addressverificationsOrderInformationBillTo(
        address1 = orderInformationBillToAddress1,
        address2 = orderInformationBillToAddress2,
        address3 = orderInformationBillToAddress3,
        address4 = orderInformationBillToAddress4,
        administrative_area = orderInformationBillToAdministrativeArea,
        country = orderInformationBillToCountry,
        locality = orderInformationBillToLocality,
        postal_code = orderInformationBillToPostalCode
    )


    orderInformationLineItems = []
    orderInformationLineItems1 = Riskv1addressverificationsOrderInformationLineItems(
        unit_price = "120.50",
        quantity = 3,
        product_sku = "9966223",
        product_name = "headset",
        product_code = "electronic"
    )

    orderInformationLineItems.append(orderInformationLineItems1.__dict__)

    orderInformation = Riskv1addressverificationsOrderInformation(
        bill_to = orderInformationBillTo.__dict__,
        line_items = orderInformationLineItems
    )

    buyerInformationMerchantCustomerId = "ABCD"
    buyerInformation = Riskv1addressverificationsBuyerInformation(
        merchant_customer_id = buyerInformationMerchantCustomerId
    )

    requestObj = VerifyCustomerAddressRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        order_information = orderInformation.__dict__,
        buyer_information = buyerInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = VerificationApi(client_config)
        return_data, status, body = api_instance.verify_customer_address(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling VerificationApi->verify_customer_address: %s\n" % e)

if __name__ == "__main__":
    canadian_billing_details()
