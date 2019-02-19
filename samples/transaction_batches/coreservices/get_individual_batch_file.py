from CyberSource import *
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def get_individual_batch_file():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        transction_api_obj = TransactionBatchApi(details_dict1)
        batch_file_id = "Owcyk6pl"
        response_data = transction_api_obj.pts_v1_transaction_batches_id_get(batch_file_id)
        # Calling api_client variable in Configuration file to access the request_headers
        config = Configuration()
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())
    except Exception as e:
        print("\nException when calling TransactionBatchApi->pts_v1_transaction_batches_id_get: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    get_individual_batch_file()
