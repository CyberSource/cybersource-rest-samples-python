from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

process_payment_path = os.path.join(os.getcwd(), "samples", "Payments", "Payments", "simple-authorizationinternet.py")
process_payment = SourceFileLoader("module.name", process_payment_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def void_payment():
    api_payment_response = process_payment.simple_authorizationinternet(False)
    id = api_payment_response.id

    clientReferenceInformationCode = "test_void"
    clientReferenceInformation = Ptsv2paymentsidreversalsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    requestObj = VoidPaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = VoidApi(client_config)
        return_data, status, body = api_instance.void_payment(requestObj, id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling VoidApi->void_payment: %s\n" % e)

if __name__ == "__main__":
    void_payment()
