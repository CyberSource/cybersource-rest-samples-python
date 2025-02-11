from CyberSource import *
from CyberSource.rest import ApiException
from CyberSource.models import Upv1capturecontextsCaptureMandate, Upv1capturecontextsOrderInformationAmountDetails, Upv1capturecontextsOrderInformation, GenerateUnifiedCheckoutCaptureContextRequest
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
    allowedPaymentTypes.append("CLICKTOPAY")
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

    orderInformation = Upv1capturecontextsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    requestObj = GenerateUnifiedCheckoutCaptureContextRequest(
        client_version = clientVersion,
        target_origins = targetOrigins,
        allowed_card_networks = allowedCardNetworks,
        allowed_payment_types = allowedPaymentTypes,
        country = country,
        locale = locale,
        capture_mandate = captureMandate.__dict__,
        order_information = orderInformation.__dict__
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

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling TaxesApi->calculate_tax: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    generate_unified_checkout_capture_context()
