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

def bin_lookup_with_tms_jwt_transient_token():
    tokenInformationTransientTokenJwt = "eyJraWQiOiIwODd0bk1DNU04bXJHR3JHMVJQTkwzZ2VyRUh5VWV1ciIsImFsZyI6IlJTMjU2In0.eyJpc3MiOiJGbGV4LzA4IiwiZXhwIjoxNjYwMTk1ODcwLCJ0eXBlIjoiYXBpLTAuMS4wIiwiaWF0IjoxNjYwMTk0OTcwLCJqdGkiOiIxRTBXQzFHTzg3SkcxQkRQMENROFNDUjFUVEs4NlU5Tjk4SDNXSDhJRk05TVZFV1RJWUZJNjJGNDk0MUU3QTkyIiwiY29udGVudCI6eyJwYXltZW50SW5mb3JtYXRpb24iOnsiY2FyZCI6eyJudW1iZXIiOnsibWFza2VkVmFsdWUiOiJYWFhYWFhYWFhYWFgxMTExIiwiYmluIjoiNDExMTExIn0sInR5cGUiOnsidmFsdWUiOiIwMDEifX19fX0.MkCLbyvufN4prGRvHJcqCu1WceDVlgubZVpShNWQVjpuFQUuqwrKg284sC7ucVKuIsOU0DTN8_OoxDLduvZhS7X_5TnO0QjyA_aFxbRBvU_bEz1l9V99VPADG89T-fox_L6sLUaoTJ8T4PyD7rkPHEA0nmXbqQCVqw4Czc5TqlKCwmL-Fe0NBR2HlOFI1PrSXT-7_wI-JTgXI0dQzb8Ub20erHwOLwu3oni4_ZmS3rGI_gxq2MHi8pO-ZOgA597be4WfVFAx1wnMbareqR72a0QM4DefeoltrpNqXSaASVyb5G0zuqg-BOjWJbawmg2QgcZ_vE3rJ6PDgWROvp9Tbw"
    tokenInformation = Binv1binlookupTokenInformation(
        transient_token_jwt = tokenInformationTransientTokenJwt
    )

    requestObj = CreateBinLookupRequest(
        token_information = tokenInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = BinLookupApi(client_config)
        return_data, status, body = api_instance.get_account_info(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return return_data
    except Exception as e:
        write_log_audit(e.status)
        print("\nException when calling BinLookupApi->get_account_info: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    bin_lookup_with_tms_jwt_transient_token()