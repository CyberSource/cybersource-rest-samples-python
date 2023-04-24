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

def committed_tax_refund_call_request():
    clientReferenceInformationCode = "TAX_TC001"
    clientReferenceInformation = Vasv2taxClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    taxInformationShowTaxPerLineItem = "Yes"
    taxInformationCommitIndicator = True
    taxInformationRefundIndicator = True
    taxInformation = Vasv2taxTaxInformation(
        show_tax_per_line_item = taxInformationShowTaxPerLineItem,
        commit_indicator = taxInformationCommitIndicator,
        refund_indicator = taxInformationRefundIndicator
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

    orderInformationShippingDetailsShipFromLocality = "Cambridge Bay"
    orderInformationShippingDetailsShipFromCountry = "CA"
    orderInformationShippingDetailsShipFromPostalCode = "A0G 1T0"
    orderInformationShippingDetailsShipFromAdministrativeArea = "NL"
    orderInformationShippingDetails = Vasv2taxOrderInformationShippingDetails(
        ship_from_locality = orderInformationShippingDetailsShipFromLocality,
        ship_from_country = orderInformationShippingDetailsShipFromCountry,
        ship_from_postal_code = orderInformationShippingDetailsShipFromPostalCode,
        ship_from_administrative_area = orderInformationShippingDetailsShipFromAdministrativeArea
    )

    orderInformationShipToCountry = "US"
    orderInformationShipToAdministrativeArea = "FL"
    orderInformationShipToLocality = "Panama City"
    orderInformationShipToPostalCode = "32401"
    orderInformationShipToAddress1 = "123 Russel St."
    orderInformationShipTo = Vasv2taxOrderInformationShipTo(
        country = orderInformationShipToCountry,
        administrative_area = orderInformationShipToAdministrativeArea,
        locality = orderInformationShipToLocality,
        postal_code = orderInformationShipToPostalCode,
        address1 = orderInformationShipToAddress1
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
        shipping_details = orderInformationShippingDetails.__dict__,
        ship_to = orderInformationShipTo.__dict__,
        line_items = orderInformationLineItems
    )

    merchantInformationVatRegistrationNumber = "abcdef"
    merchantInformation = Vasv2taxMerchantInformation(
        vat_registration_number = merchantInformationVatRegistrationNumber
    )

    requestObj = TaxRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        tax_information = taxInformation.__dict__,
        order_information = orderInformation.__dict__,
        merchant_information = merchantInformation.__dict__
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

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling TaxesApi->calculate_tax: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    committed_tax_refund_call_request()
