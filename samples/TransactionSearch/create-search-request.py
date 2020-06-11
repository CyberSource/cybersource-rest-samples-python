from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def create_search_request():
    save = False
    name = "MRN"
    timezone = "America/Chicago"
    query = "clientReferenceInformation.code:TC50171_3 AND submitTimeUtc:[NOW/DAY-7DAYS TO NOW/DAY+1DAY}"
    offset = 0
    limit = 100
    sort = "id:asc,submitTimeUtc:asc"
    requestObj = CreateSearchRequest(
        save = save,
        name = name,
        timezone = timezone,
        query = query,
        offset = offset,
        limit = limit,
        sort = sort
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = SearchTransactionsApi(client_config)
        return_data, status, body = api_instance.create_search(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling SearchTransactionsApi->create_search: %s\n" % e)

if __name__ == "__main__":
    create_search_request()
