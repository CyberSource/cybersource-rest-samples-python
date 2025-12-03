from CyberSource import *
from pathlib import Path
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

def update_customer():
    customerTokenId = "AB695DA801DD1BB6E05341588E0A3BDC"
    buyerInformationMerchantCustomerID = "Your customer identifier"
    buyerInformationEmail = "test@cybs.com"
    buyerInformation = Tmsv2tokenizeTokenInformationCustomerBuyerInformation(
        merchant_customer_id = buyerInformationMerchantCustomerID,
        email = buyerInformationEmail
    )

    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Tmsv2tokenizeTokenInformationCustomerClientReferenceInformation(
        code = clientReferenceInformationCode
    )


    merchantDefinedInformation = []
    merchantDefinedInformation1 = Tmsv2tokenizeTokenInformationCustomerMerchantDefinedInformation(
        name = "data1",
        value = "Your customer data"
    )

    merchantDefinedInformation.append(merchantDefinedInformation1.__dict__)

    requestObj = PatchCustomerRequest(
        buyer_information = buyerInformation.__dict__,
        client_reference_information = clientReferenceInformation.__dict__,
        merchant_defined_information = merchantDefinedInformation
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = CustomerApi(client_config)
        return_data, status, body = api_instance.patch_customer(customerTokenId, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling CustomerApi->patch_customer: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    update_customer()
