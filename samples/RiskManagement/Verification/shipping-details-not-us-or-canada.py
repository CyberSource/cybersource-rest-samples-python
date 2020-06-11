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

def shipping_details_not_us_or_canada():
    clientReferenceInformationCode = "addressEg"
    clientReferenceInformationComments = "dav-All fields"
    clientReferenceInformation = Riskv1addressverificationsClientReferenceInformation(
        code = clientReferenceInformationCode,
        comments = clientReferenceInformationComments
    )

    orderInformationBillToAddress1 = "12301 research st"
    orderInformationBillToAddress2 = "1"
    orderInformationBillToAddress3 = "2"
    orderInformationBillToAddress4 = "3"
    orderInformationBillToAdministrativeArea = "TX"
    orderInformationBillToCountry = "US"
    orderInformationBillToLocality = "Austin"
    orderInformationBillToPostalCode = "78759"
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

    orderInformationShipToAddress1 = "4R.ILHA TERCEIRA,232-R/C-ESQ"
    orderInformationShipToAddress2 = " "
    orderInformationShipToAddress3 = ""
    orderInformationShipToAddress4 = ""
    orderInformationShipToAdministrativeArea = "WI"
    orderInformationShipToCountry = "PT"
    orderInformationShipToLocality = "Carcavelos"
    orderInformationShipToPostalCode = "29681"
    orderInformationShipTo = Riskv1addressverificationsOrderInformationShipTo(
        address1 = orderInformationShipToAddress1,
        address2 = orderInformationShipToAddress2,
        address3 = orderInformationShipToAddress3,
        address4 = orderInformationShipToAddress4,
        administrative_area = orderInformationShipToAdministrativeArea,
        country = orderInformationShipToCountry,
        locality = orderInformationShipToLocality,
        postal_code = orderInformationShipToPostalCode
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
        ship_to = orderInformationShipTo.__dict__,
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
    shipping_details_not_us_or_canada()
