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
        elif isinstance(value, list):
            for item in value:
                del_none(item)
    return d

def store_oauth_credentials(v_c_correlation_id, v_c_sender_organization_id, v_c_permissions):
    clientRequestAction = "STORE"
    keyInformationProvider = "merchantName"
    keyInformationTenant = "nrtd"
    keyInformationKeyType = "oAuthClientCredentials"
    keyInformationOrganizationId = "merchantName"
    keyInformationClientKeyId = "client username"
    keyInformationKey = "client secret"
    keyInformationExpiryDuration = "365"
    keyInformation = Kmsegressv2keyssymKeyInformation(
        provider = keyInformationProvider,
        tenant = keyInformationTenant,
        key_type = keyInformationKeyType,
        organization_id = keyInformationOrganizationId,
        client_key_id = keyInformationClientKeyId,
        key = keyInformationKey,
        expiry_duration = keyInformationExpiryDuration
    )

    requestObj = SaveSymEgressKey(
        client_request_action = clientRequestAction,
        key_information = keyInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CreateNewWebhooksApi(client_config)
        return_data, status, body = api_instance.save_sym_egress_key(v_c_sender_organization_id, v_c_permissions, requestObj, v_c_correlation_id = v_c_correlation_id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling CreateNewWebhooksApi->save_sym_egress_key: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    store_oauth_credentials(v_c_correlation_id, v_c_sender_organization_id, v_c_permissions)