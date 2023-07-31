from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
from pathlib import Path

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

cancel_subscription_path = os.path.join(os.getcwd(), "samples", "RecurringBillingSubscriptions", "Subscriptions", "cancel-subscription.py")
cancel_subscription_module = SourceFileLoader("module.name", cancel_subscription_path).load_module()


def activate_subscription():
    try:
        cancelled_subscription_id = cancel_subscription_module.cancel_subscription().id
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = SubscriptionsApi(client_config)
        return_data, status, body = api_instance.activate_subscription(cancelled_subscription_id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling SubscriptionsApi->activate_subscription: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    activate_subscription()
