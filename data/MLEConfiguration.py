import os
from CyberSource.logging.log_configuration import LogConfiguration

class MLEConfiguration:
    def __init__(self):
        self.authentication_type ="JWT" #for MLE feature auth type should be JWT
        self.merchantid = "testrest"
        self.run_environment = "apitest.cybersource.com"
     
        # JWT PARAMETERS
        self.key_alias = "testrest"
        self.key_pass = "testrest"
        self.key_file_name = "testrest"
        self.keys_directory = os.path.join(os.getcwd(), "resources")

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
        self.enable_masking = True
        self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        self.log_date_format = "%Y-%m-%d %H:%M:%S"
        # PROXY PARAMETERS
        #self.proxy_address = "userproxy.com"
        #self.proxy_port = ""

	    # PEM Key file path for decoding JWE Response Enter the folder path where the .pem file is located.
		# It is optional property, require adding only during JWE decryption.
        self.JWEPemFIleDirectory = os.path.join(os.getcwd(), "resources", "NetworkTokenCert.pem")

    # MLEConfiguration1
    def get_configuration_with_mle_Type1(self):
        configuration_dictionary = ({})
        configuration_dictionary["authentication_type"] = self.authentication_type
        configuration_dictionary["merchantid"] = self.merchantid
        configuration_dictionary["run_environment"] = self.run_environment
        configuration_dictionary["key_alias"] = self.key_alias
        configuration_dictionary["key_password"] = self.key_pass
        configuration_dictionary["key_file_name"] = self.key_file_name
        configuration_dictionary["keys_directory"] = self.keys_directory
        configuration_dictionary["use_metakey"] = self.use_metakey
        configuration_dictionary["portfolio_id"] = self.portfolio_id
        configuration_dictionary["timeout"] = self.timeout
        configuration_dictionary['jwePEMFileDirectory'] = self.JWEPemFIleDirectory
       
        # MLE Config Use Type 1
        configuration_dictionary['useMLEGlobally'] = True #globally MLE will be enabled for all the MLE supported APIs by Cybs in SDK
        configuration_dictionary['mleKeyAlias'] = "CyberSource_SJC_US" #this is optional paramter, not required to set the parameter if custom value is not required for MLE key alias. Default value is "CyberSource_SJC_US".

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
        #configuration_dictionary["proxy_address"] = self.proxy_address
        #configuration_dictionary["proxy_port"] = self.proxy_port
        return configuration_dictionary

    # MLEConfiguration2
    def get_configuration_with_mle_Type2(self):
        configuration_dictionary = ({})
        configuration_dictionary["authentication_type"] = self.authentication_type
        configuration_dictionary["merchantid"] = self.merchantid
        configuration_dictionary["run_environment"] = self.run_environment
        configuration_dictionary["key_alias"] = self.key_alias
        configuration_dictionary["key_password"] = self.key_pass
        configuration_dictionary["key_file_name"] = self.key_file_name
        configuration_dictionary["keys_directory"] = self.keys_directory
        configuration_dictionary["use_metakey"] = self.use_metakey
        configuration_dictionary["portfolio_id"] = self.portfolio_id
        configuration_dictionary["timeout"] = self.timeout
        configuration_dictionary['jwePEMFileDirectory'] = self.JWEPemFIleDirectory
       
        # MLE Config Use Type 2
        configuration_dictionary['useMLEGlobally'] = True #globally MLE will be enabled for all the MLE supported APIs by Cybs in SDK
        configuration_dictionary['mapToControlMLEonAPI'] = {
            "create_payment":False, #only create_payment function will have MLE=false i.e. (/pts/v2/payments POST API) out of all MLE supported APIs
            "capture_payment":True #capture_payment function will have MLE=true i.e.  (/pts/v2/payments/{id}/captures POST API), if it not in list of MLE supportedAPIs else it will already have MLE=true by global MLE parameter.
        }
        configuration_dictionary['mleKeyAlias'] = "CyberSource_SJC_US" #this is optional paramter, not required to set the parameter if custom value is not required for MLE key alias. Default value is "CyberSource_SJC_US".

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
        #configuration_dictionary["proxy_address"] = self.proxy_address
        #configuration_dictionary["proxy_port"] = self.proxy_port
        return configuration_dictionary

    # MLEConfiguration3
    def get_configuration_with_mle_Type3(self):
        configuration_dictionary = ({})
        configuration_dictionary["authentication_type"] = self.authentication_type
        configuration_dictionary["merchantid"] = self.merchantid
        configuration_dictionary["run_environment"] = self.run_environment
        configuration_dictionary["key_alias"] = self.key_alias
        configuration_dictionary["key_password"] = self.key_pass
        configuration_dictionary["key_file_name"] = self.key_file_name
        configuration_dictionary["keys_directory"] = self.keys_directory
        configuration_dictionary["use_metakey"] = self.use_metakey
        configuration_dictionary["portfolio_id"] = self.portfolio_id
        configuration_dictionary["timeout"] = self.timeout
        configuration_dictionary['jwePEMFileDirectory'] = self.JWEPemFIleDirectory
       
        # MLE Config Use Type 3
        configuration_dictionary['useMLEGlobally'] = False #globally MLE will be disabled for all the APIs in SDK
        configuration_dictionary['mapToControlMLEonAPI'] ={
            "create_payment":True, #only create_payment function will have MLE=true i.e. (/pts/v2/payments POST API)
            "capture_payment":True #only capture_payment function will have MLE=true i.e. (/pts/v2/payments/{id}/captures POST API)
        }
        configuration_dictionary['mleKeyAlias'] = "CyberSource_SJC_US" #this is optional paramter, not required to set the parameter if custom value is not required for MLE key alias. Default value is "CyberSource_SJC_US".

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
        #configuration_dictionary["proxy_address"] = self.proxy_address
        #configuration_dictionary["proxy_port"] = self.proxy_port
        return configuration_dictionary
