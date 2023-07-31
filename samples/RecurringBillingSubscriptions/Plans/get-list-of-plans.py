from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
from pathlib import Path

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def get_list_of_plans():
    try:
        offset = 0
        limit = 10
        code = None
        status = None
        name = None

        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PlansApi(client_config)
        return_data, status, body = api_instance.get_plans(offset=offset, limit=limit)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling PlansApi->get_list_of_plans: %s\n" % e)


def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    get_list_of_plans()
