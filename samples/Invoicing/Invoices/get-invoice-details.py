from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

create_invoice_path = os.path.join(os.getcwd(), "samples", "Invoicing", "Invoices", "create-draft-invoice.py")
create_invoice = SourceFileLoader("module.name", create_invoice_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def get_invoice_details():
    id = create_invoice.create_draft_invoice().id
    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InvoicesApi(client_config)
        return_data, status, body = api_instance.get_invoice(id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling InvoicesApi->get_invoice: %s\n" % e)

if __name__ == "__main__":
    get_invoice_details()
