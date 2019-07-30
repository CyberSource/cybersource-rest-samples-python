from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def create_search_request():
    try:
        # Setting the json message body
        create_search_request = CreateSearchRequest()
        create_search_request.save = "false"
        create_search_request.name = "TSS search"
        create_search_request.timezone = "America/Chicago"
        create_search_request.query = "clientReferenceInformation.code:TC50171_3 AND submitTimeUtc:[NOW/DAY-7DAYS TO NOW/DAY+1DAY}"
        create_search_request.offset = 0
        create_search_request.limit = 10
        create_search_request.sort = "id:asc, submitTimeUtc:asc"
        message_body = json.dumps(create_search_request.__dict__)
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        search_transaction_obj = SearchTransactionsApi(details_dict1)
        return_data, status, body = search_transaction_obj.create_search(message_body)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
        return return_data

    except Exception as e:
        print("Exception when calling SearchTransactionsApi->create_search: %s\n" % e)


if __name__ == "__main__":
    create_search_request()
