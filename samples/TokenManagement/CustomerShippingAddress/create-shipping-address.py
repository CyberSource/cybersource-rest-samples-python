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

def create_shipping_address():
    customerTokenId = "AB695DA801DD1BB6E05341588E0A3BDC"

    shipToFirstName = "John"
    shipToLastName = "Doe"
    shipToCompany = "CyberSource"
    shipToAddress1 = "1 Market St"
    shipToLocality = "San Francisco"
    shipToAdministrativeArea = "CA"
    shipToPostalCode = "94105"
    shipToCountry = "US"
    shipToEmail = "test@cybs.com"
    shipToPhoneNumber = "4158880000"
    shipTo = Tmsv2customersEmbeddedDefaultShippingAddressShipTo(
        first_name = shipToFirstName,
        last_name = shipToLastName,
        company = shipToCompany,
        address1 = shipToAddress1,
        locality = shipToLocality,
        administrative_area = shipToAdministrativeArea,
        postal_code = shipToPostalCode,
        country = shipToCountry,
        email = shipToEmail,
        phone_number = shipToPhoneNumber
    )

    requestObj = PostCustomerShippingAddressRequest(
        ship_to = shipTo.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CustomerShippingAddressApi(client_config)
        return_data, status, body = api_instance.post_customer_shipping_address(customerTokenId, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling CustomerShippingAddressApi->post_customer_shipping_address: %s\n" % e)

if __name__ == "__main__":
    create_shipping_address()
