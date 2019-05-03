from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def retrieve_transaction():
    try:
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        transction_details_obj = TransactionDetailsApi(details_dict1)
        retrieve_transaction_id = "5568628895326770703005"
        return_data, status, body = transction_details_obj.get_transaction(retrieve_transaction_id)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling TransactionDetailsApi->get_transaction: %s\n" % e)


if __name__ == "__main__":
    retrieve_transaction()
