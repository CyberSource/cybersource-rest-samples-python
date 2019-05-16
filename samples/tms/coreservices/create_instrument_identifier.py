from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_instrument_identifier():
    try:
        # Setting the json message body
        request = CreateInstrumentIdentifierRequest()
        card_info = Tmsv1instrumentidentifiersCard()
        card_info.number = "123456789098765"
        request.card = card_info.__dict__

        message_body = del_none(request.__dict__)
        message_body = json.dumps(message_body)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        instrument_identifier_obj = InstrumentIdentifierApi(details_dict1)
        return_data, status, body = instrument_identifier_obj.create_instrument_identifier(
            "93B32398-AD51-4CC2-A682-EA3E93614EB1", create_instrument_identifier_request=message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        return return_data
    except Exception as e:
        print("Exception when calling InstrumentIdentifierApi->create_instrument_identifier: %s\n" % e)

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


if __name__ == "__main__":
    create_instrument_identifier()
