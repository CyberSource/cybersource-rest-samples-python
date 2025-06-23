from CyberSource import *
import os
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


def batch_upload_mtls_with_keys():

    input_file_path = os.path.join(
        os.getcwd(), "data", "batchAPIMTLS", "batchapiTest.csv"
    )
    public_key_file = os.path.join(
        os.getcwd(), "data", "batchAPIMTLS", "bts-encryption-public.asc"
    )
    client_certificate_file = os.path.join(
        os.getcwd(), "data", "batchAPIMTLS", "client_cert.crt"
    )
    private_key_file = os.path.join(
        os.getcwd(), "data", "batchAPIMTLS", "client_private_key.key"
    )
    server_certificate_file = os.path.join(
        os.getcwd(), "data", "batchAPIMTLS", "server.crt.pem"
    )
    env_host_name = "secure-batch-test.cybersource.com"  # cas env

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = BatchUploadWithMTLSApi(client_config["log_config"])
        body, status, headers = (
            api_instance.upload_batch_api_with_key_and_certs_file(
                input_file_path=input_file_path,
                environment_hostname=env_host_name,
                pgp_encryption_public_key_path=public_key_file,
                server_trust_cert_path=server_certificate_file,
                client_cert_path=client_certificate_file,
                client_key_path=private_key_file,
            )
        )
        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)

        return body
    except Exception as e:
        write_log_audit(getattr(e, "status", "0"))
        print(
            "\nException when calling BatchUploadMTLS->upload_batch_api_with_key_and_certs_file: %s\n"
            % e
        )


def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    batch_upload_mtls_with_keys()
