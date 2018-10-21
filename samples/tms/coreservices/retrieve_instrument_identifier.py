from cybersource_rest_client_python import *
import cybersource_rest_samples_python.samples.tms.coreservices.create_instrument_identifier
def retrieve_instrument_identifier():
    try:
        api_instrument_identifier_response=cybersource_rest_samples_python.samples.tms.coreservices.create_instrument_identifier.create_instrument_identifier()
        instrument_identifier=InstrumentIdentifierApi()
        return instrument_identifier.instrumentidentifiers_token_id_get("93B32398-AD51-4CC2-A682-EA3E93614EB1",api_instrument_identifier_response.id)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    retrieve_instrument_identifier()
