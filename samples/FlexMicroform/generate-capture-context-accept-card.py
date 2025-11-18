from CyberSource import *
from CyberSource.utilities.flex.CaptureContextParsingUtility import parse_capture_context_response
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

def generate_capture_context_accept_card():
    clientVersion = "v2"

    targetOrigins = []
    targetOrigins.append("https://www.test.com")
    allowedPaymentTypes = []
    allowedPaymentTypes.append("CARD")

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
    requestObj = GenerateCaptureContextRequest(
        client_version = clientVersion,
        target_origins = targetOrigins,
        allowed_card_networks = allowedCardNetworks,
        allowed_payment_types=allowedPaymentTypes

    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = MicroformIntegrationApi(client_config)
        return_data, status, body = api_instance.generate_capture_context(requestObj)

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
        write_log_audit(e.status)
        print("\nException when calling MicroformIntegrationApi->generate_capture_context: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    generate_capture_context_accept_card()