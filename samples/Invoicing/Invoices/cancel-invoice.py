from CyberSource import *
from pathlib import Path
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

create_invoice_path = os.path.join(os.getcwd(), "samples", "Invoicing", "Invoices", "create-draft-invoice.py")
create_invoice = SourceFileLoader("module.name", create_invoice_path).load_module()


def cancel_invoice():
    try:
        invoice_id = create_invoice.create_draft_invoice().id
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InvoicesApi(client_config)
        return_data, status, body = api_instance.perform_cancel_action(invoice_id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling InvoicesApi->perform_cancel_action: %s\n" % e)


def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    cancel_invoice()
