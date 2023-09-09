from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
from pathlib import Path

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

activate_plan_path = os.path.join(os.getcwd(), "samples", "RecurringBillingSubscriptions", "Plans", "activate-plan.py")
activate_plan = SourceFileLoader("module.name", activate_plan_path).load_module()


def deactivate_plan():
    try:
        activate_plan_response = activate_plan.activate_plan()
        plan_id = activate_plan_response.id
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PlansApi(client_config)
        return_data, status, body = api_instance.deactivate_plan(plan_id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling PlansApi->deactivate_plan: %s\n" % e)


def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    deactivate_plan()
