from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def enrol_with_travel_information():
    try:
        # Setting the json message body
        request = CheckPayerAuthEnrollmentRequest()
        client_reference = Riskv1authenticationsClientReferenceInformation("cybs_test")
        request.client_reference_information = client_reference.__dict__

        consumer_authentication_information = Riskv1authenticationsConsumerAuthenticationInformation(mcc = '', reference_id = '', transaction_mode = '')
        consumer_authentication_information.authentication_transaction_id = 'gNNV7Q5e2rr2NOik5I30'

        request.consumer_authentication_information = consumer_authentication_information.__dict__

        message_body = json.dumps(request.__dict__)

        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()

        dm_obj = PayerAuthenticationApi(details_dict1)
        return_data, status, body = dm_obj.check_payer_auth_enrollment(message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("Exception when calling PayerAuthenticationApi->enrol_with_travel_information: %s\n" % e)


if __name__ == "__main__":
    enrol_with_travel_information()

