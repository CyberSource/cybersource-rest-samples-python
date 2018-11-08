from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configaration.py"
configaration = SourceFileLoader("module.name", config_file).load_module()

def notification_of_change():
    try:
        start_time = "2018-09-01T12:00:00-05:00"
        end_time = "2018-09-30T12:00:00-05:00"
        config_obj = configaration.Configaration()
        details_dict1 = config_obj.get_configaration()
        notification_obj = NotificationOfChangesApi(details_dict1)
        return_data, status, body =notification_obj.get_notification_of_change_report(start_time,end_time)
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    notification_of_change()
