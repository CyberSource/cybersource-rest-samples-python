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

def create_asymmetric_key(v_c_correlation_id, v_c_sender_organization_id, v_c_permissions):
    clientRequestAction = "STORE"
    keyInformationProvider = "merchantName"
    keyInformationTenant = "nrtd"
    keyInformationKeyType = "publickey"
    keyInformationOrganizationId = "merchantName"
    keyInformationPub = "MIIDbDCCAlQCCQD4lcSlmasmCTANBgkqhkiG9w0BAQsFADB4MQswCQYDVQQGEwJVUzELMAkGA1UECAwCVFgxDzANBgNVBAcMBkF1c3RpbjENMAsGA1UECgwEVGVzdDEOMAwGA1UECwwFVGVzdDIxDjAMBgNVBAMMBVRlc3QzMRwwGgYJKoZIhvcNAQkBFg10ZXN0QHRlc3QuY29tMB4XDTIxMDgwOTE0MTcxNFoXDTIyMDgwOTE0MTcxNFoweDELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAlRYMQ8wDQYDVQQHDAZBdXN0aW4xDTALBgNVBAoMBFRlc3QxDjAMBgNVBAsMBVRlc3QyMQ4wDAYDVQQDDAVUZXN0MzEcMBoGCSqGSIb3DQEJARYNdGVzdEB0ZXN0LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMcHQWZRETqim3XzUQlAiujFEvsHIi1uJZKj+1lvPH36Ucqo3ORcoh/MM/zxVdahjhSyyp7MHuKBWnzft6bFeDEul6qKWGPAAzaxG/2xZSV3FggA9SyAZEDUpJ6mblwqm/EY4KmZi1FrNBUHfW2wwaqDexHPRDesRG6aI7Wuu4GdQUUqoTa2+Nv7kVgEDmGcfIjoWkGKHe+Yan95EITrq4jEFCE5Tg/vERnMvHfK2SovENZ13/pnwFYbeh1kfJSBzWW7yq8AyQAgAE9iqJXbJ/MAasir2vjUQ2+Hcl7WbkpoVjLqDt3rzV1T0Bsd4T9SC3wij9qjJSxa6vAgV4xn6bECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEADuMrtYW1Sf0IsZ4ZD9ipjUrFuTxqh+0M5Jk8h0QqAXEHA/MawedlU3JmE3NB/UR82/XUwdmtObGnFANuUQQ+8WMFpcNo/Sq2kg7juneHZroRh72o73UUMtHWHzo8s0fXElNal8h3SaAAnjMblCiN+gM1RvWMvhGrMTXp2XAcdIezXf8/FOZLlzOF9QylbSk1U4ayWBag6MydkxgHjkPKdShZROEm0oz/O7J/gNp/r7J8F42Rw9MmJh9qH3SFre13nQa8V7Kg+dJHZ/jpGtSlDHAxO0SSTrPXkwB+iBJ6hSkiL/J2Ep+lYHqVe3p5NXMOlTtJdbU4enHeLkD6PazKTw"
    keyInformationExpiryDuration = "365"
    keyInformation = Kmsegressv2keysasymKeyInformation(
        provider = keyInformationProvider,
        tenant = keyInformationTenant,
        key_type = keyInformationKeyType,
        organization_id = keyInformationOrganizationId,
        pub = keyInformationPub,
        expiry_duration = keyInformationExpiryDuration
    )

    requestObj = SaveAsymEgressKey(
        client_request_action = clientRequestAction,
        key_information = keyInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = ManageWebhooksApi(client_config)
        return_data, status, body = api_instance.save_asym_egress_key(v_c_sender_organization_id, v_c_permissions, requestObj, v_c_correlation_id = v_c_correlation_id)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling ManageWebhooksApi->save_asym_egress_key: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    create_asymmetric_key(v_c_correlation_id, v_c_sender_organization_id, v_c_permissions)