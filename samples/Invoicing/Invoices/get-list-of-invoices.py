from CyberSource import *
from pathlib import Path
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def get_list_of_invoices():
    try:
        offset = 0
        limit = 10
        status = None

        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InvoicesApi(client_config)
        return_data, status, body = api_instance.get_all_invoices(offset, limit, status=status)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling InvoicesApi->get_all_invoices: %s\n" % e)


def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    get_list_of_invoices()
