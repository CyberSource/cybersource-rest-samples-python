from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

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


def create_plan():
    # Required to make the sample code activate-plan.py work
    planInformationStatus = "DRAFT"

    planInformationName = "Gold Plan"
    planInformationDescription = "New Gold Plan"
    planInformationBillingPeriodLength = "1"
    planInformationBillingPeriodUnit = "M"
    planInformationBillingPeriod = InlineResponse200PlanInformationBillingPeriod(
        length = planInformationBillingPeriodLength,
        unit = planInformationBillingPeriodUnit
    )

    planInformationBillingCyclesTotal = "12"
    planInformationBillingCycles = Rbsv1plansPlanInformationBillingCycles(
        total = planInformationBillingCyclesTotal
    )

    planInformation = Rbsv1plansPlanInformation(
        name = planInformationName,
        description = planInformationDescription,
        status = planInformationStatus,
        billing_period = planInformationBillingPeriod.__dict__,
        billing_cycles = planInformationBillingCycles.__dict__
    )

    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetailsBillingAmount = "10"
    orderInformationAmountDetailsSetupFee = "2"
    orderInformationAmountDetails = Rbsv1plansOrderInformationAmountDetails(
        currency = orderInformationAmountDetailsCurrency,
        billing_amount = orderInformationAmountDetailsBillingAmount,
        setup_fee = orderInformationAmountDetailsSetupFee
    )

    orderInformation = Rbsv1plansOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    requestObj = CreatePlanRequest(
        plan_information = planInformation.__dict__,
        order_information = orderInformation.__dict__
    )

    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PlansApi(client_config)
        return_data, status, body = api_instance.create_plan(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling PlansApi->create_plan: %s\n" % e)


def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    create_plan()
