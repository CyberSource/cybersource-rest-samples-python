from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

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

def mark_as_suspect(id):
    riskInformationMarkingDetailsNotes = "Adding this transaction as suspect"
    riskInformationMarkingDetailsReason = "suspected"

    riskInformationMarkingDetailsFieldsIncluded = []
    riskInformationMarkingDetailsFieldsIncluded.append("customer_email")
    riskInformationMarkingDetailsFieldsIncluded.append("customer_phone")
    riskInformationMarkingDetailsAction = "add"
    riskInformationMarkingDetails = Riskv1decisionsidmarkingRiskInformationMarkingDetails(
        notes = riskInformationMarkingDetailsNotes,
        reason = riskInformationMarkingDetailsReason,
        fields_included = riskInformationMarkingDetailsFieldsIncluded,
        action = riskInformationMarkingDetailsAction
    )

    riskInformation = Riskv1decisionsidmarkingRiskInformation(
        marking_details = riskInformationMarkingDetails.__dict__
    )

    requestObj = FraudMarkingActionRequest(
        risk_information = riskInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = DecisionManagerApi(client_config)
        return_data, status, body = api_instance.fraud_update(id, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling DecisionManagerApi->fraud_update: %s\n" % e)

if __name__ == "__main__":
    id = "5825489395116729903003"

    mark_as_suspect(id)
