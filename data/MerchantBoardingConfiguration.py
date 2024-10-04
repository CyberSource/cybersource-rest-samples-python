import os
from CyberSource.logging.log_configuration import LogConfiguration

class Configuration:
    def __init__(self):
        self.authentication_type ="jwt"
        self.merchantid = "<insert merchantId here for testing the boarding samples>"
        
        self.run_environment = "apitest.cybersource.com"
        # new property has been added for user to configure the base path so that request can route the API calls via Azure Management URL.
        # Example: If intermediate url is https://manage.windowsazure.com then in property input can be same url or manage.windowsazure.com.
       
        self.IntermediateHost="https://manage.windowsazure.com"
        self.request_json_path = "src/main/resources/request.json"

        # JWT PARAMETERS
        self.key_alias = "<insert keyAlias (merchantId)  here for testing the boarding samples>"
        self.key_pass = "<insert p12 file password here for testing the boarding samples>"
        self.key_file_name = "<insert p12 file without .p12 extension here for testing the boarding samples>"
        self.keys_directory = "<insert p12 file directory path>"

        # HTTP PARAMETERS
        self.merchant_keyid = ""
        self.merchant_secretkey = ""


        # META KEY PARAMETERS
        self.use_metakey = False
        self.portfolio_id = ''
        # CONNECTION TIMEOUT PARAMETER
        self.timeout = 1000
        # LOG PARAMETERS
        self.enable_log = True
        self.log_file_name = "cybs"
        self.log_maximum_size = 10487560
        self.log_directory = os.path.join(os.getcwd(), "Logs")
        self.log_level = "Debug"
        self.enable_masking = False
        self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        self.log_date_format = "%Y-%m-%d %H:%M:%S"
        # PROXY PARAMETERS
        #self.proxy_address = "userproxy.com"
        #self.proxy_port = ""

        #Optional default Axa/Client Headers- Client can add additional headers
        # self.default_headers ={ "Ocp-Apim-Subscription-Key":"=fchgfchgvjhvjh5536hg",
        #                         "Ocp-Apim-Trace":"dfgcjgvjkhbkjkjhnkjvjgchdxh",
        #                         "Host":"manage.windowsazure.com"}

	    # PEM Key file path for decoding JWE Response Enter the folder path where the .pem file is located.
		# It is optional property, require adding only during JWE decryption.
       # self.JWEPemFIleDirectory = os.path.join(os.getcwd(), "resources", "NetworkTokenCert.pem")

    # Assigning the configuration properties in the configuration dictionary
    def get_merchant_boarding_configuration(self):
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
        configuration_dictionary["use_metakey"] = self.use_metakey
        configuration_dictionary["portfolio_id"] = self.portfolio_id
        configuration_dictionary["timeout"] = self.timeout
       # configuration_dictionary['jwePEMFileDirectory'] = self.JWEPemFIleDirectory
        log_config = LogConfiguration()
        log_config.set_enable_log(self.enable_log)
        log_config.set_log_directory(self.log_directory)
        log_config.set_log_file_name(self.log_file_name)
        log_config.set_log_maximum_size(self.log_maximum_size)
        log_config.set_log_level(self.log_level)
        log_config.set_enable_masking(self.enable_masking)
        log_config.set_log_format(self.log_format)
        log_config.set_log_date_format(self.log_date_format)
        configuration_dictionary["log_config"] = log_config
        #configuration_dictionary["proxy_address"] = self.proxy_address
        #configuration_dictionary["proxy_port"] = self.proxy_port
        return configuration_dictionary

    
