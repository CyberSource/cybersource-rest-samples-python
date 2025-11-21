from CyberSource import *
from CyberSource.rest import ApiException
from CyberSource.utilities.flex.CaptureContextParsingUtility import parse_capture_context_response
from CyberSource.models import Upv1capturecontextsCaptureMandate, Upv1capturecontextsOrderInformationAmountDetails, Upv1capturecontextsOrderInformation, GenerateUnifiedCheckoutCaptureContextRequest, Upv1capturecontextsCompleteMandate, Upv1capturecontextsDataOrderInformationBillTo, Upv1capturecontextsDataOrderInformationBillToCompany, Upv1capturecontextsDataOrderInformationShipTo
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

def generate_unified_checkout_capture_context():

    clientVersion = "0.23"

    targetOrigins = []
    targetOrigins.append("https://yourCheckoutPage.com")

    allowedCardNetworks = []
    allowedCardNetworks.append("VISA")
    allowedCardNetworks.append("MASTERCARD")
    allowedCardNetworks.append("AMEX")
    allowedCardNetworks.append("CARNET")
    allowedCardNetworks.append("CARTESBANCAIRES")
    allowedCardNetworks.append("CUP")
    allowedCardNetworks.append("DINERSCLUB")
    allowedCardNetworks.append("DISCOVER")
    allowedCardNetworks.append("EFTPOS")
    allowedCardNetworks.append("ELO")
    allowedCardNetworks.append("JCB")
    allowedCardNetworks.append("JCREW")
    allowedCardNetworks.append("MADA")
    allowedCardNetworks.append("MAESTRO")
    allowedCardNetworks.append("MEEZA")

    allowedPaymentTypes = []
    allowedPaymentTypes.append("APPLEPAY")
    allowedPaymentTypes.append("CHECK")
    allowedPaymentTypes.append("CLICKTOPAY")
    allowedPaymentTypes.append("GOOGLEPAY")
    allowedPaymentTypes.append("PANENTRY")
    allowedPaymentTypes.append("PAZE")
    country = "US"
    locale = "en_US"
    captureMandateBillingType = "FULL"
    captureMandateRequestEmail = True
    captureMandateRequestPhone = True
    captureMandateRequestShipping = True

    captureMandateShipToCountries = []
    captureMandateShipToCountries.append("US")
    captureMandateShipToCountries.append("GB")
    captureMandateShowAcceptedNetworkIcons = True
    captureMandate = Upv1capturecontextsCaptureMandate(
        billing_type = captureMandateBillingType,
        request_email = captureMandateRequestEmail,
        request_phone = captureMandateRequestPhone,
        request_shipping = captureMandateRequestShipping,
        ship_to_countries = captureMandateShipToCountries,
        show_accepted_network_icons = captureMandateShowAcceptedNetworkIcons
    )

    orderInformationAmountDetailsTotalAmount = "21.00"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Upv1capturecontextsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToAddress1 = "277 Park Avenue"
    orderInformationBillToAddress2 = "50th Floor"
    orderInformationBillToAddress3 = "Desk NY-50110"
    orderInformationBillToAddress4 = "address4"
    orderInformationBillToAdministrativeArea = "NY"
    orderInformationBillToBuildingNumber = "buildingNumber"
    orderInformationBillToCountry = "US"
    orderInformationBillToDistrict = "district"
    orderInformationBillToLocality = "New York"
    orderInformationBillToPostalCode = "10172"
    orderInformationBillToCompanyName = "Visa Inc"
    orderInformationBillToCompanyAddress1 = "900 Metro Center Blvd"
    orderInformationBillToCompanyAddress2 = "address2"
    orderInformationBillToCompanyAddress3 = "address3"
    orderInformationBillToCompanyAddress4 = "address4"
    orderInformationBillToCompanyAdministrativeArea = "CA"
    orderInformationBillToCompanyBuildingNumber = "1"
    orderInformationBillToCompanyCountry = "US"
    orderInformationBillToCompanyDistrict = "district"
    orderInformationBillToCompanyLocality = "Foster City"
    orderInformationBillToCompanyPostalCode = "94404"
    orderInformationBillToCompany = Upv1capturecontextsDataOrderInformationBillToCompany(
        name = orderInformationBillToCompanyName,
        address1 = orderInformationBillToCompanyAddress1,
        address2 = orderInformationBillToCompanyAddress2,
        address3 = orderInformationBillToCompanyAddress3,
        address4 = orderInformationBillToCompanyAddress4,
        administrative_area = orderInformationBillToCompanyAdministrativeArea,
        building_number = orderInformationBillToCompanyBuildingNumber,
        country = orderInformationBillToCompanyCountry,
        district = orderInformationBillToCompanyDistrict,
        locality = orderInformationBillToCompanyLocality,
        postal_code = orderInformationBillToCompanyPostalCode
    )

    orderInformationBillToEmail = "john.doe@visa.com"
    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Doe"
    orderInformationBillToMiddleName = "F"
    orderInformationBillToNameSuffix = "Jr"
    orderInformationBillToTitle = "Mr"
    orderInformationBillToPhoneNumber = "1234567890"
    orderInformationBillToPhoneType = "phoneType"
    orderInformationBillTo = Upv1capturecontextsDataOrderInformationBillTo(
        address1 = orderInformationBillToAddress1,
        address2 = orderInformationBillToAddress2,
        address3 = orderInformationBillToAddress3,
        address4 = orderInformationBillToAddress4,
        administrative_area = orderInformationBillToAdministrativeArea,
        building_number = orderInformationBillToBuildingNumber,
        country = orderInformationBillToCountry,
        district = orderInformationBillToDistrict,
        locality = orderInformationBillToLocality,
        postal_code = orderInformationBillToPostalCode,
        company = orderInformationBillToCompany.__dict__,
        email = orderInformationBillToEmail,
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        middle_name = orderInformationBillToMiddleName,
        name_suffix = orderInformationBillToNameSuffix,
        title = orderInformationBillToTitle,
        phone_number = orderInformationBillToPhoneNumber,
        phone_type = orderInformationBillToPhoneType
    )

    orderInformationShipToAddress1 = "CyberSource"
    orderInformationShipToAddress2 = "Victoria House"
    orderInformationShipToAddress3 = "15-17 Gloucester Street"
    orderInformationShipToAddress4 = "string"
    orderInformationShipToAdministrativeArea = "CA"
    orderInformationShipToBuildingNumber = "string"
    orderInformationShipToCountry = "GB"
    orderInformationShipToDistrict = "string"
    orderInformationShipToLocality = "Belfast"
    orderInformationShipToPostalCode = "BT1 4LS"
    orderInformationShipToFirstName = "Joe"
    orderInformationShipToLastName = "Soap"
    orderInformationShipTo = Upv1capturecontextsDataOrderInformationShipTo(
        address1 = orderInformationShipToAddress1,
        address2 = orderInformationShipToAddress2,
        address3 = orderInformationShipToAddress3,
        address4 = orderInformationShipToAddress4,
        administrative_area = orderInformationShipToAdministrativeArea,
        building_number = orderInformationShipToBuildingNumber,
        country = orderInformationShipToCountry,
        district = orderInformationShipToDistrict,
        locality = orderInformationShipToLocality,
        postal_code = orderInformationShipToPostalCode,
        first_name = orderInformationShipToFirstName,
        last_name = orderInformationShipToLastName
    )

    orderInformation = Upv1capturecontextsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__,
        ship_to = orderInformationShipTo.__dict__
    )
    
    completemandate = Upv1capturecontextsCompleteMandate(
        type= "CAPTURE",
        decision_manager = False
    )

    requestObj = GenerateUnifiedCheckoutCaptureContextRequest(
        client_version = clientVersion,
        target_origins = targetOrigins,
        allowed_card_networks = allowedCardNetworks,
        allowed_payment_types = allowedPaymentTypes,
        country = country,
        locale = locale,
        capture_mandate = captureMandate.__dict__,
        order_information = orderInformation.__dict__,
        complete_mandate = completemandate.__dict__ 

    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = UnifiedCheckoutCaptureContextApi(client_config)
        return_data, status, body = api_instance.generate_unified_checkout_capture_context(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        # Parse the capture context response
        try:
            parsed_result = parse_capture_context_response(
                jwt_value=return_data,
                merchant_config=api_instance.api_client.mconfig,
                verify_jwt_signature=True
            )
            
            print("\nParsed Capture Context : ", json.dumps(parsed_result, indent=2))
        except Exception as parse_error:
            print("\nError in Capture Context Parsing : ", str(parse_error))

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling TaxesApi->calculate_tax: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    generate_unified_checkout_capture_context()
