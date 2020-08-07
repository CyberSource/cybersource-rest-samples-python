from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

authorization_path = os.path.join(os.getcwd(), "samples", "Payments", "Payments", "authorization-capture-for-timeout-void-flow.py")
authorization = SourceFileLoader("module.name", authorization_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def timeout_void():
    id = authorization.authorization_capture_for_timeout_void_flow().id
    timeoutVoidTransactionId = authorization.timeoutVoidTransactionId

    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformationTransactionId = timeoutVoidTransactionId
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode,
        transaction_id = clientReferenceInformationTransactionId
    )

    requestObj = MitVoidRequest(
        client_reference_information = clientReferenceInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = VoidApi(client_config)
        return_data, status, body = api_instance.mit_void(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling VoidApi->mit_void: %s\n" % e)

if __name__ == "__main__":
    timeout_void()
