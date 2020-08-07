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

def basic_tax_calculation_request():
    clientReferenceInformationCode = "TAX_TC001"
    clientReferenceInformation = Vasv2taxClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    taxInformationShowTaxPerLineItem = "Yes"
    taxInformation = Vasv2taxTaxInformation(
        show_tax_per_line_item = taxInformationShowTaxPerLineItem
    )

    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = RiskV1DecisionsPost201ResponseOrderInformationAmountDetails(
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToAddress1 = "1 Market St"
    orderInformationBillToLocality = "San Francisco"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToPostalCode = "94105"
    orderInformationBillToCountry = "US"
    orderInformationBillTo = Vasv2taxOrderInformationBillTo(
        address1 = orderInformationBillToAddress1,
        locality = orderInformationBillToLocality,
        administrative_area = orderInformationBillToAdministrativeArea,
        postal_code = orderInformationBillToPostalCode,
        country = orderInformationBillToCountry
    )


    orderInformationLineItems = []
    orderInformationLineItems1 = Vasv2taxOrderInformationLineItems(
        product_sku = "07-12-00657",
        product_code = "50161815",
        quantity = 1,
        product_name = "Chewing Gum",
        unit_price = "1200"
    )

    orderInformationLineItems.append(orderInformationLineItems1.__dict__)

    orderInformationLineItems2 = Vasv2taxOrderInformationLineItems(
        product_sku = "07-12-00659",
        product_code = "50181905",
        quantity = 1,
        product_name = "Sugar Cookies",
        unit_price = "1240"
    )

    orderInformationLineItems.append(orderInformationLineItems2.__dict__)

    orderInformationLineItems3 = Vasv2taxOrderInformationLineItems(
        product_sku = "07-12-00658",
        product_code = "5020.11",
        quantity = 1,
        product_name = "Carbonated Water",
        unit_price = "9001"
    )

    orderInformationLineItems.append(orderInformationLineItems3.__dict__)

    orderInformation = Vasv2taxOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__,
        line_items = orderInformationLineItems
    )

    requestObj = TaxRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        tax_information = taxInformation.__dict__,
        order_information = orderInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = TaxesApi(client_config)
        return_data, status, body = api_instance.calculate_tax(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling TaxesApi->calculate_tax: %s\n" % e)

if __name__ == "__main__":
    basic_tax_calculation_request()
