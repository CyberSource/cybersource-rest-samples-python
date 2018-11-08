from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()


def purchase_and_refund():
    try:
        start_time = "2018-05-01T12:00:00-05:00"
        end_time = "2018-05-30T12:00:00-05:00"

        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        purchase_refund_obj = PurchaseAndRefundDetailsApi(details_dict1)
        return_data, status, body =purchase_refund_obj.get_purchase_and_refund_details(start_time, end_time)
        print(status)
        print(body)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    purchase_and_refund()
