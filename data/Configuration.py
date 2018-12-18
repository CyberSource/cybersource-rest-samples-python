import os


class Configuration:
    def __init__(self):
        self.authentication_type ="http_signature"
        self.merchantid = "testrest"
        self.run_environment = "CyberSource.Environment.SANDBOX"
        self.request_json_path = ""
        # JWT PARAMETERS
        self.key_alias = "testrest"
        self.key_pass = "testrest"
        self.key_file_name = "testrest"
        self.keys_directory = os.path.join(os.getcwd(), "resources")
        # HTTP PARAMETERS
        self.merchant_keyid = "08c94330-f618-42a3-b09d-e1e43be5efda"
        self.merchant_secretkey = "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE="
        # CONNECTION TIMEOUT PARAMETER
        self.timeout = 1000
        # LOG PARAMETERS
        self.enable_log = True
        self.log_file_name = "cybs"
        self.log_maximum_size = 10487560
        self.log_directory = os.path.join(os.getcwd(), "Logs")
        # PROXY PARAMETERS
        #self.proxy_address = "userproxy.com"
        #self.proxy_port = ""

    # Assigning the configuration properties in the configuration dictionary
    def get_configuration(self):
        configuration_dictionary = ({})
        configuration_dictionary["authentication_type"] = self.authentication_type
        configuration_dictionary["merchantid"] = self.merchantid
        configuration_dictionary["run_environment"] = self.run_environment
        configuration_dictionary["request_json_path"] = self.request_json_path
        configuration_dictionary["key_alias"] = self.key_alias
        configuration_dictionary["key_password"] = self.key_pass
        configuration_dictionary["key_file_name"] = self.key_file_name
        configuration_dictionary["keys_directory"] = self.keys_directory
        configuration_dictionary["merchant_keyid"] = self.merchant_keyid
        configuration_dictionary["merchant_secretkey"] = self.merchant_secretkey
        configuration_dictionary["enable_log"] = self.enable_log
        configuration_dictionary["timeout"] = self.timeout
        configuration_dictionary["log_file_name"] = self.log_file_name
        configuration_dictionary["log_maximum_size"] = self.log_maximum_size
        configuration_dictionary["log_directory"] = self.log_directory
        #configuration_dictionary["proxy_address"] = self.proxy_address
        #configuration_dictionary["proxy_port"] = self.proxy_port
        return configuration_dictionary
