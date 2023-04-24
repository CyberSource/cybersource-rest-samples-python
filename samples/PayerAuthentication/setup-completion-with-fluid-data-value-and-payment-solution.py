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

def setup_completion_with_fluid_data_value_and_payment_solution():
    clientReferenceInformationCode = "cybs_test"
    clientReferenceInformation = Riskv1decisionsClientReferenceInformation(
        code = clientReferenceInformationCode
    )

    paymentInformationFluidDataValue = "eyJkYXRhIjoiOFJTK2o1a2ZLRjZkcTRWTUV1ZG9FNUh1UjBcLzRQMXJmdG9EVlpwNnhFdnF1STY5dkt2YnZHcXpmTkpUNjVnPT0iLCJ2ZXJzaW9uIjoiRUNfdjEiLCJoZWFkZXIiOnsiYXBwbGljYXRpb25EYXRhIjoiNzQ2NTczNzQ2MTcwNzA2QzY5NjM2MTc0Njk2RjZFNjQ2MTc0NjEiLCJ0cmFuc2FjdGlvbklkIjoiNzQ2NTczNzQ3NDcyNjE2RTczNjE2Mzc0Njk2RjZFNjk2NCIsImVwaGVtZXJhbFB1YmxpY0tleSI6Ik1JSUJTekNDQVFNR0J5cUdTTTQ5QWdFd2dmY0NBUUV3TEFZSEtvWkl6ajBCQVFJaEFQXC9cL1wvXC84QUFBQUJBQUFBQUFBQUFBQUFBQUFBXC9cL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC9NRnNFSVBcL1wvXC9cLzhBQUFBQkFBQUFBQUFBQUFBQUFBQUFcL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC9cL1wvXC84QkNCYXhqWFlxanFUNTdQcnZWVjJtSWE4WlIwR3NNeFRzUFk3emp3K0o5SmdTd01WQU1TZE5naUc1d1NUYW1aNDRST2RKcmVCbjM2UUJFRUVheGZSOHVFc1FrZjR2T2JsWTZSQThuY0RmWUV0NnpPZzlLRTVSZGlZd3BaUDQwTGlcL2hwXC9tNDduNjBwOEQ1NFdLODR6VjJzeFhzN0x0a0JvTjc5UjlRSWhBUFwvXC9cL1wvOEFBQUFBXC9cL1wvXC9cL1wvXC9cL1wvXC8rODV2cXRweGVlaFBPNXlzTDhZeVZSQWdFQkEwSUFCQmJHK2xtTHJIWWtKSVwvSUUwcTU3dEN0bE5jK2pBWHNudVMrSnFlOFVcLzc0cSs5NVRnbzVFRjBZNks3b01LTUt5cTMwY3VQbmtIenkwMjVpU1BGdWczRT0iLCJwdWJsaWNLZXlIYXNoIjoieCtQbUhHMzdUNjdBWUFIenVqbGJyaW1JdzZZaFlYaVpjYjV3WnJCNGpRdz0ifSwic2lnbmF0dXJlIjoiTUlJRFFnWUpLb1pJaHZjTkFRY0NvSUlETXpDQ0F5OENBUUV4Q3pBSkJnVXJEZ01DR2dVQU1Bc0dDU3FHU0liM0RRRUhBYUNDQWlzd2dnSW5NSUlCbEtBREFnRUNBaEJjbCtQZjMrVTRwazEzblZEOW53UVFNQWtHQlNzT0F3SWRCUUF3SnpFbE1DTUdBMVVFQXg0Y0FHTUFhQUJ0QUdFQWFRQkFBSFlBYVFCekFHRUFMZ0JqQUc4QWJUQWVGdzB4TkRBeE1ERXdOakF3TURCYUZ3MHlOREF4TURFd05qQXdNREJhTUNjeEpUQWpCZ05WQkFNZUhBQmpBR2dBYlFCaEFHa0FRQUIyQUdrQWN3QmhBQzRBWXdCdkFHMHdnWjh3RFFZSktvWklodmNOQVFFQkJRQURnWTBBTUlHSkFvR0JBTkM4K2tndGdtdldGMU96amdETnJqVEVCUnVvXC81TUt2bE0xNDZwQWY3R3g0MWJsRTl3NGZJWEpBRDdGZk83UUtqSVhZTnQzOXJMeXk3eER3YlwvNUlrWk02MFRaMmlJMXBqNTVVYzhmZDRmek9wazNmdFphUUdYTkxZcHRHMWQ5VjdJUzgyT3VwOU1NbzFCUFZyWFRQSE5jc005OUVQVW5QcWRiZUdjODdtMHJBZ01CQUFHalhEQmFNRmdHQTFVZEFRUlJNRStBRUhaV1ByV3RKZDdZWjQzMWhDZzdZRlNoS1RBbk1TVXdJd1lEVlFRREhod0FZd0JvQUcwQVlRQnBBRUFBZGdCcEFITUFZUUF1QUdNQWJ3QnRnaEJjbCtQZjMrVTRwazEzblZEOW53UVFNQWtHQlNzT0F3SWRCUUFEZ1lFQWJVS1lDa3VJS1M5UVEybUZjTVlSRUltMmwrWGc4XC9KWHYrR0JWUUprT0tvc2NZNGlOREZBXC9iUWxvZ2Y5TExVODRUSHdOUm5zdlYzUHJ2N1JUWTgxZ3EwZHRDOHpZY0FhQWtDSElJM3lxTW5KNEFPdTZFT1c5a0prMjMyZ1NFN1dsQ3RIYmZMU0tmdVNnUVg4S1hRWXVaTGsyUnI2M044QXBYc1h3QkwzY0oweGdlQXdnZDBDQVFFd096QW5NU1V3SXdZRFZRUURIaHdBWXdCb0FHMEFZUUJwQUVBQWRnQnBBSE1BWVFBdUFHTUFid0J0QWhCY2wrUGYzK1U0cGsxM25WRDlud1FRTUFrR0JTc09Bd0lhQlFBd0RRWUpLb1pJaHZjTkFRRUJCUUFFZ1lBMG9MXC9KSWFTN0tra1RFNG1pOGRmU2tQVVwvdlp2cVwva2NYZ1pUdGJZbENtTFM4YzNuS2VZNVE0c2s4MXJnZkI1ampBMWJRZldhUHBKc05tVWNSS3gzS0FGUEtpNzE0WWVYdGUrcmc2V1k4MnVxcnlwRERiTkhqSWVpNjVqV0dvcGRZUEx6TEk5c1Z3NDh5OHlqSXY3SjFaQVlycnp6YjBwNzUzcUJUQ0ZEN1p3PT0ifQ=="
    paymentInformationFluidData = Riskv1authenticationsetupsPaymentInformationFluidData(
        value = paymentInformationFluidDataValue
    )

    paymentInformation = Riskv1authenticationsetupsPaymentInformation(
        fluid_data = paymentInformationFluidData.__dict__
    )

    processingInformationPaymentSolution = "001"
    processingInformation = Riskv1authenticationsetupsProcessingInformation(
        payment_solution = processingInformationPaymentSolution
    )

    requestObj = PayerAuthSetupRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        processing_information = processingInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PayerAuthenticationApi(client_config)
        return_data, status, body = api_instance.payer_auth_setup(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling PayerAuthenticationApi->payer_auth_setup: %s\n" % e)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    setup_completion_with_fluid_data_value_and_payment_solution()
