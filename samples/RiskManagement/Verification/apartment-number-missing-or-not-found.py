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

def apartment_number_missing_or_not_found():
    clientReferenceInformationCode = "addressEg"
    clientReferenceInformationComments = "dav-error response check"
    clientReferenceInformation = Riskv1decisionsClientReferenceInformation(
        code = clientReferenceInformationCode,
        comments = clientReferenceInformationComments
    )

    orderInformationBillToAddress1 = "6th 4th ave"
    orderInformationBillToAddress2 = ""
    orderInformationBillToAdministrativeArea = "NY"
    orderInformationBillToCountry = "US"
    orderInformationBillToLocality = "rensslaer"
    orderInformationBillToPostalCode = "12144"
    orderInformationBillTo = Riskv1addressverificationsOrderInformationBillTo(
        address1 = orderInformationBillToAddress1,
        address2 = orderInformationBillToAddress2,
        administrative_area = orderInformationBillToAdministrativeArea,
        country = orderInformationBillToCountry,
        locality = orderInformationBillToLocality,
        postal_code = orderInformationBillToPostalCode
    )


    orderInformationLineItems = []
    orderInformationLineItems1 = Riskv1addressverificationsOrderInformationLineItems(
        unit_price = "120.50",
        quantity = 3,
        product_sku = "996633",
        product_name = "qwerty",
        product_code = "handling"
    )

    orderInformationLineItems.append(orderInformationLineItems1.__dict__)

    orderInformation = Riskv1addressverificationsOrderInformation(
        bill_to = orderInformationBillTo.__dict__,
        line_items = orderInformationLineItems
    )

    requestObj = VerifyCustomerAddressRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        order_information = orderInformation.__dict__
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

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling VerificationApi->verify_customer_address: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    apartment_number_missing_or_not_found()
