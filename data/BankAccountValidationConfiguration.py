import os
from CyberSource.logging.log_configuration import LogConfiguration

class BankAccountValidationConfiguration:
    """
    The ConfigurationForBankAccountValidation class provides the necessary settings for 
    Bank Account Validation (BAV) using the CyberSource REST API. 

    This configuration uses JWT authentication, which is required for Request MLE. 
    The BAV API mandates Request MLE, and JWT is the only supported authentication type for this feature.

    By Default SDK sends encrypted requests for the APIs having mandatory Request MLE flag.
    For more MLE features and configurations, please refer to CyberSource documentation at https://github.com/CyberSource/cybersource-rest-client-python/blob/master/MLE.md
    """
    def __init__(self):
        self.authentication_type ="JWT" #for MLE feature auth type should be JWT
        self.merchantid = "testcasmerchpd01001"
        self.run_environment = "apitest.cybersource.com"
     
        # JWT PARAMETERS
        self.key_alias = "testcasmerchpd01001"
        self.key_pass = "Authnet101!"
        self.key_file_name = "testcasmerchpd01001"
        self.keys_directory = os.path.join(os.getcwd(), "resources")

        # LOG PARAMETERS
        self.enable_log = True
        self.log_file_name = "cybs"
        self.log_maximum_size = 10487560
        self.log_directory = os.path.join(os.getcwd(), "Logs")
        self.log_level = "Debug"
        self.enable_masking = True
        self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        self.log_date_format = "%Y-%m-%d %H:%M:%S"
    
    def get_configuration_for_bav(self):
        configuration_dictionary = ({})
        configuration_dictionary["authentication_type"] = self.authentication_type
        configuration_dictionary["merchantid"] = self.merchantid
        configuration_dictionary["run_environment"] = self.run_environment
        configuration_dictionary["key_alias"] = self.key_alias
        configuration_dictionary["key_password"] = self.key_pass
        configuration_dictionary["key_file_name"] = self.key_file_name
        configuration_dictionary["keys_directory"] = self.keys_directory

        #Log Config
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
        return configuration_dictionary

