from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader
from pathlib import Path

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

create_plan_path = os.path.join(os.getcwd(), "samples", "RecurringBillingSubscriptions", "Plans", "create-plan.py")
create_plan = SourceFileLoader("module.name", create_plan_path).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def update_plan():
    planInformationName = "Gold Plan NA"
    planInformationDescription = "Updated Gold Plan"
    planInformationBillingPeriodLength = "2"
    planInformationBillingPeriodUnit = "W"
    planInformationBillingPeriod = GetAllPlansResponsePlanInformationBillingPeriod(
        length = planInformationBillingPeriodLength,
        unit = planInformationBillingPeriodUnit
    )

    planInformationBillingCyclesTotal = "11"
    planInformationBillingCycles = Rbsv1plansPlanInformationBillingCycles(
        total = planInformationBillingCyclesTotal
    )

    planInformation = Rbsv1plansidPlanInformation(
        name = planInformationName,
        description = planInformationDescription,
        billing_period = planInformationBillingPeriod.__dict__,
        billing_cycles = planInformationBillingCycles.__dict__
    )

    processingInformationSubscriptionBillingOptionsApplyTo = "ALL"
    processingInformationSubscriptionBillingOptions = Rbsv1plansidProcessingInformationSubscriptionBillingOptions(
        apply_to = processingInformationSubscriptionBillingOptionsApplyTo
    )

    processingInformation = Rbsv1plansidProcessingInformation(
        subscription_billing_options = processingInformationSubscriptionBillingOptions.__dict__
    )

    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetailsBillingAmount = "11"
    orderInformationAmountDetailsSetupFee = "2"
    orderInformationAmountDetails = GetAllPlansResponseOrderInformationAmountDetails(
        currency = orderInformationAmountDetailsCurrency,
        billing_amount = orderInformationAmountDetailsBillingAmount,
        setup_fee = orderInformationAmountDetailsSetupFee
    )

    orderInformation = GetAllPlansResponseOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__
    )

    requestObj = UpdatePlanRequest(
        plan_information = planInformation.__dict__,
        processing_information = processingInformation.__dict__,
        order_information = orderInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        create_plan_response = create_plan.create_plan()
        id = create_plan_response.id
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PlansApi(client_config)
        return_data, status, body = api_instance.update_plan(id, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling PlansApi->update_plan: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    update_plan()