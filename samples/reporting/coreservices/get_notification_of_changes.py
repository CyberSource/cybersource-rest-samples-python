from CyberSource import *
import os
from datetime import datetime, timedelta
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def notification_of_change():
    try:
        start_time = (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%dT%H:%M:%SZ%Z")
        end_time = (datetime.now()).strftime("%Y-%m-%dT%H:%M:%SZ%Z")
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        notification_obj = NotificationOfChangesApi(details_dict1)
        return_data, status, body = notification_obj.get_notification_of_change_report(start_time, end_time)
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling NotificationOfChangesApi->get_notification_of_change_report: %s\n" % e)


if __name__ == "__main__":
    notification_of_change()
