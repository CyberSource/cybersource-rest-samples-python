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

def get_notification_of_changes():
    startTime = "2021-10-01T12:00:00Z"
    endTime = "2021-10-10T12:00:00Z"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = NotificationOfChangesApi(client_config)
        return_data, status, body = api_instance.get_notification_of_change_report(startTime, endTime)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling NotificationOfChangesApi->get_notification_of_change_report: %s\n" % e)

if __name__ == "__main__":
    get_notification_of_changes()
