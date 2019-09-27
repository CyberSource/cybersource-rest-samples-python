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

def process_authorization_reversal(id):
    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Ptsv2paymentsidreversalsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    reversalInformationAmountDetailsTotalAmount = "102.21"
    reversalInformationAmountDetails = Ptsv2paymentsidreversalsReversalInformationAmountDetails(
        total_amount = reversalInformationAmountDetailsTotalAmount
    )

    reversalInformationReason = "testing"
    reversalInformation = Ptsv2paymentsidreversalsReversalInformation(
        amount_details = reversalInformationAmountDetails.__dict__,
        reason = reversalInformationReason
    )

    requestObj = AuthReversalRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        reversal_information = reversalInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ReversalApi(client_config)
        return_data, status, body = api_instance.auth_reversal(id, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)
        print("\nAPI RESPONSE : ", return_data)

        return return_data
    except Exception as e:
        print("\nException when calling ReversalApi->auth_reversal: %s\n" % e)

if __name__ == "__main__":
    print("\nInput missing path parameter <id>:")
    id = input()

    process_authorization_reversal(id)
