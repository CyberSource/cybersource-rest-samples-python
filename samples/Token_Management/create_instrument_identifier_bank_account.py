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

def create_instrument_identifier_bank_account(profileid):
    bankAccountNumber = "4100"
    bankAccountRoutingNumber = "071923284"
    bankAccount = Tmsv1instrumentidentifiersBankAccount(
        number = bankAccountNumber,
        routing_number = bankAccountRoutingNumber
    )

    requestObj = CreateInstrumentIdentifierRequest(
        bank_account = bankAccount.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InstrumentIdentifierApi(client_config)
        return_data, status, body = api_instance.create_instrument_identifier(profileid, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)
        print("\nAPI RESPONSE : ", return_data)

        return return_data
    except Exception as e:
        print("\nException when calling InstrumentIdentifierApi->create_instrument_identifier: %s\n" % e)

if __name__ == "__main__":
    print("\nInput missing header parameter <profile-id>:")
    profileid = input()

    create_instrument_identifier_bank_account(profileid)
