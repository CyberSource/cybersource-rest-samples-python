from CyberSource import *
import json
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()


def create_search_request():
    try:
        create_search_request = CreateSearchRequest()
        create_search_request.save = "false"
        create_search_request.name = "MRN"
        create_search_request.timezone = "America/Chicago"
        create_search_request.query = "clientReferenceInformation.code:TC50171_3"
        create_search_request.offset = 0
        create_search_request.limit = 100
        create_search_request.sort = "id:asc, submitTimeUtc:asc"
        message_body = json.dumps(create_search_request.__dict__)
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        search_transaction_obj = SearchTransactionsApi(details_dict1)
        return_data, status, body =search_transaction_obj.create_search(message_body)
        print(status)
        print(body)
        return return_data

    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_search_request()
