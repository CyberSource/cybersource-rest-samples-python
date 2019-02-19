from CyberSource import *
import json
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_search_request():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        # Setting the json message body
        create_search_request = TssV2TransactionsPostResponse()
        create_search_request.save = "false"
        create_search_request.name = "TSS search"
        create_search_request.timezone = "America/Chicago"
        create_search_request.query = "clientReferenceInformation.code:12345"
        create_search_request.offset = 0
        create_search_request.limit = 100
        create_search_request.sort = "id:asc, submitTimeUtc:asc"
        message_body = json.dumps(create_search_request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        search_transaction_obj = SearchTransactionsApi(details_dict1)
        # Calling api_client variable in Configuration file
        config = Configuration()
        print("\nAPI REQUEST BODY: ",
              config.api_client.masking(json.dumps(config.api_client.replace_underscore(json.loads(message_body)))))
        response_data = search_transaction_obj.create_search(message_body)
        # Calling api_client variable in Configuration file
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())

    except Exception as e:
        print("\nException when calling SearchTransactionsApi->create_search: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    create_search_request()
