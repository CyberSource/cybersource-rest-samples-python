from CyberSource import *
import samples.tms.coreservices.retrieve_instrument_identifier
from data.Configaration import *

def remove_instrument_identifiers():
    try:
        api_instrument_response=samples.tms.coreservices.retrieve_instrument_identifier.retrieve_instrument_identifier()
        config_obj = Configaration()
        details_dict1 = config_obj.get_configaration()
        instrument_identifier_obj = InstrumentIdentifierApi(details_dict1)
        return_data, status, body =instrument_identifier_obj.instrumentidentifiers_token_id_delete("93B32398-AD51-4CC2-A682-EA3E93614EB1",api_instrument_response.id)
        print(status)
        print(body)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    remove_instrument_identifiers()
