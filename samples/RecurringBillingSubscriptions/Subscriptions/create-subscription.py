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

def create_subscription():
    clientReferenceInformationCode = "TC501713"
    clientReferenceInformationPartnerDeveloperId = "ABCD1234"
    clientReferenceInformationPartnerSolutionId = "GEF1234"
    clientReferenceInformationPartner = Rbsv1subscriptionsClientReferenceInformationPartner(
        developer_id = clientReferenceInformationPartnerDeveloperId,
        solution_id = clientReferenceInformationPartnerSolutionId
    )

    clientReferenceInformationApplicationName = "CYBS-SDK"
    clientReferenceInformationApplicationVersion = "v1"
    clientReferenceInformation = Rbsv1subscriptionsClientReferenceInformation(
        code = clientReferenceInformationCode,
        partner = clientReferenceInformationPartner.__dict__,
        application_name = clientReferenceInformationApplicationName,
        application_version = clientReferenceInformationApplicationVersion
    )

    processingInformationCommerceIndicator = "recurring"
    processingInformationAuthorizationOptionsInitiatorType = "merchant"
    processingInformationAuthorizationOptionsInitiator = Rbsv1subscriptionsProcessingInformationAuthorizationOptionsInitiator(
        type = processingInformationAuthorizationOptionsInitiatorType
    )

    processingInformationAuthorizationOptions = Rbsv1subscriptionsProcessingInformationAuthorizationOptions(
        initiator = processingInformationAuthorizationOptionsInitiator.__dict__
    )

    processingInformation = Rbsv1subscriptionsProcessingInformation(
        commerce_indicator = processingInformationCommerceIndicator,
        authorization_options = processingInformationAuthorizationOptions.__dict__
    )

    subscriptionInformationPlanId = "6868912495476705603955"
    subscriptionInformationName = "Subscription with PlanId"
    subscriptionInformationStartDate = "2025-06-11"
    subscriptionInformation = Rbsv1subscriptionsSubscriptionInformation(
        plan_id = subscriptionInformationPlanId,
        name = subscriptionInformationName,
        start_date = subscriptionInformationStartDate
    )

    paymentInformationCustomerId = "C24F5921EB870D99E053AF598E0A4105"
    paymentInformationCustomer = Rbsv1subscriptionsPaymentInformationCustomer(
        id = paymentInformationCustomerId
    )

    paymentInformation = Rbsv1subscriptionsPaymentInformation(
        customer = paymentInformationCustomer.__dict__
    )

    requestObj = CreateSubscriptionRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        subscription_information = subscriptionInformation.__dict__,
        payment_information = paymentInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = SubscriptionsApi(client_config)
        return_data, status, body = api_instance.create_subscription(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling SubscriptionsApi->create_subscription: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    create_subscription()