from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

def get_payment_batch_summary_data():

    startTime = "2019-05-01T12:00:00Z"
    endTime = "2019-08-30T12:00:00Z"
    organizationId = "testrest"
	
    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentBatchSummariesApi(client_config)
        return_data, status, body = api_instance.get_payment_batch_summary(startTime, endTime, organization_id=organizationId)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        print("API RESPONSE BODY : ", return_data)
    except Exception as e:
        print("Exception when calling PaymentBatchSummariesApi->get_payment_batch_summary: %s\n" % e)


if __name__ == "__main__":
    get_payment_batch_summary_data()
