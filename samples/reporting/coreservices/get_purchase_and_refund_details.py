from CyberSource import *
import os
import inspect
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "input_configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def purchase_and_refund():
    try:
        print("\n[BEGIN] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)
        start_time = "2018-05-01T12:00:00-05:00"
        end_time = "2018-05-30T12:00:00-05:00"
        # Reading Merchant details from Configuration file
        config_obj = configuration.InputConfiguration()
        details_dict1 = config_obj.get_configuration()
        purchase_refund_obj = PurchaseAndRefundDetailsApi(details_dict1)
        response_data = purchase_refund_obj.get_purchase_and_refund_details(start_time, end_time)
        # Calling api_client variable in Configuration file to access the request_headers
        config = Configuration()
        request_headers = config.api_client.request_headers
        # Statements to print on console
        print("\nAPI REQUEST HEADERS: ", request_headers)
        print("\nAPI RESPONSE CODE : ", response_data.status)
        print("\nAPI RESPONSE BODY : ", response_data.data)
        print("\nAPI RESPONSE HEADERS: ", response_data.getheaders())

    except Exception as e:
        print("\nException when calling PurchaseAndRefundDetailsApi->get_purchase_and_refund_details: %s\n" % e)
    finally:
        print("\n[END] EXECUTION OF SAMPLE CODE:" + inspect.currentframe().f_code.co_name)


if __name__ == "__main__":
    purchase_and_refund()
