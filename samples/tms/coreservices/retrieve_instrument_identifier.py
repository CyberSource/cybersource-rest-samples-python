from CyberSource import *
import create_instrument_identifier
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()

def retrieve_instrument_identifier():
    try:
        api_instrument_identifier_response=create_instrument_identifier.create_instrument_identifier()
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        instrument_identifier=InstrumentIdentifierApi(details_dict1)
        return_data, status, body =instrument_identifier.instrumentidentifiers_token_id_get("93B32398-AD51-4CC2-A682-EA3E93614EB1",api_instrument_identifier_response.id)
        print(status)
        print(body)
        return return_data
    except Exception as e:
        print(e)

if __name__ == "__main__":
    retrieve_instrument_identifier()
