"""
Configuration for JWT authentication with Shared Secret (symmetric / HS256).

Why JWT with Shared Secret?
----------------------------
* HTTP Signature is being deprecated. JWT with Shared Secret provides a
  seamless migration path — it uses the **same** merchantKeyId and
  merchantsecretKey credentials you already have for HTTP Signature.

* Enables MLE (Message Level Encryption). MLE requires JWT authentication.
  By switching to JWT with Shared Secret, you can enable MLE without managing
  a P12 certificate file.

* Zero credential changes. Your existing Key ID and Shared Secret from the
  CyberSource Business Center work as-is.

Credentials
-----------
The merchantKeyId and merchantsecretKey are the same credentials used for
HTTP Signature authentication. You can obtain them from the CyberSource
Business Center:

- Test: https://businesscentertest.cybersource.com/ebc2
- Production: https://businesscenter.cybersource.com/ebc2
"""

import os
from CyberSource.logging.log_configuration import LogConfiguration


class JwtSharedSecretConfiguration:
    """Configuration class for JWT with Shared Secret authentication."""
    
    def __init__(self):
        # Authentication: JWT with Shared Secret (HS256)
        self.authentication_type = "jwt"
        self.jwt_key_type = "SHARED_SECRET"
        
        self.merchantid = "testrest"
        self.run_environment = "apitest.cybersource.com"
        
        # Shared Secret credentials — same as HTTP Signature credentials
        self.merchant_keyid = "08c94330-f618-42a3-b09d-e1e43be5efda"
        self.merchant_secretkey = "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE="
        
        # MetaKey Parameters
        self.portfolio_id = ""
        self.use_metakey = False
        
        # Timeout
        self.timeout = 1000
        
        # Log Parameters
        self.enable_log = True
        self.log_file_name = "cybs"
        self.log_maximum_size = 10487560
        self.log_directory = os.path.join(os.getcwd(), "Logs")
        self.log_level = "Debug"
        self.enable_masking = True
        self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        self.log_date_format = "%Y-%m-%d %H:%M:%S"
    
    def get_configuration(self):
        """
        Returns merchant configuration for JWT authentication with Shared Secret.
        
        This is a drop-in replacement for HTTP Signature authentication.
        The only changes from a typical HTTP Signature configuration are:
        1. authentication_type = 'jwt' (instead of 'http_signature')
        2. jwt_key_type = 'SHARED_SECRET' (new property)
        
        The merchantKeyId and merchantsecretKey remain the same.
        
        Returns:
            dict: Configuration dictionary for JWT with Shared Secret
        """
        configuration_dictionary = {}
        configuration_dictionary["authentication_type"] = self.authentication_type
        configuration_dictionary["jwt_key_type"] = self.jwt_key_type
        configuration_dictionary["merchantid"] = self.merchantid
        configuration_dictionary["run_environment"] = self.run_environment
        configuration_dictionary["merchant_keyid"] = self.merchant_keyid
        configuration_dictionary["merchant_secretkey"] = self.merchant_secretkey
        configuration_dictionary["use_metakey"] = self.use_metakey
        configuration_dictionary["portfolio_id"] = self.portfolio_id
        configuration_dictionary["timeout"] = self.timeout
        
        # Log configuration
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


class JwtSharedSecretConfigurationWithMLE:
    """Configuration class for JWT with Shared Secret + MLE authentication."""
    
    def __init__(self):
        # Authentication: JWT with Shared Secret (HS256)
        self.authentication_type = "jwt"
        self.jwt_key_type = "SHARED_SECRET"
        
        self.merchantid = "testrest"
        self.run_environment = "apitest.cybersource.com"
        
        # Shared Secret credentials — same as HTTP Signature credentials
        self.merchant_keyid = "08c94330-f618-42a3-b09d-e1e43be5efda"
        self.merchant_secretkey = "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE="
        
        # MLE Configuration
        self.enableRequestMLEForOptionalApisGlobally = True
        self.mleForRequestPublicCertPath = os.path.join(os.getcwd(), "resources", "mle_cert.pem")
        self.enableResponseMleGlobally = False
        self.responseMlePrivateKeyFilePath = ""
        self.responseMlePrivateKeyFilePassword = ""
        self.responseMleKID = ""
        
        # MetaKey Parameters
        self.portfolio_id = ""
        self.use_metakey = False
        
        # Timeout
        self.timeout = 1000
        
        # Log Parameters
        self.enable_log = True
        self.log_file_name = "cybs"
        self.log_maximum_size = 10487560
        self.log_directory = os.path.join(os.getcwd(), "Logs")
        self.log_level = "Debug"
        self.enable_masking = True
        self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        self.log_date_format = "%Y-%m-%d %H:%M:%S"
    
    def get_configuration(self):
        """
        Returns merchant configuration for JWT with Shared Secret + MLE enabled.
        
        This configuration enables Message Level Encryption (MLE) for request payloads.
        Response MLE is also supported — set enableResponseMleGlobally to True
        and provide the response MLE private key settings.
        
        Returns:
            dict: Configuration dictionary for JWT with Shared Secret + MLE
        """
        configuration_dictionary = {}
        configuration_dictionary["authentication_type"] = self.authentication_type
        configuration_dictionary["jwt_key_type"] = self.jwt_key_type
        configuration_dictionary["merchantid"] = self.merchantid
        configuration_dictionary["run_environment"] = self.run_environment
        configuration_dictionary["merchant_keyid"] = self.merchant_keyid
        configuration_dictionary["merchant_secretkey"] = self.merchant_secretkey
        configuration_dictionary["use_metakey"] = self.use_metakey
        configuration_dictionary["portfolio_id"] = self.portfolio_id
        configuration_dictionary["timeout"] = self.timeout
        
        # MLE Configuration
        configuration_dictionary["enableRequestMLEForOptionalApisGlobally"] = self.enableRequestMLEForOptionalApisGlobally
        configuration_dictionary["mleForRequestPublicCertPath"] = self.mleForRequestPublicCertPath
        configuration_dictionary["enableResponseMleGlobally"] = self.enableResponseMleGlobally
        if self.responseMlePrivateKeyFilePath:
            configuration_dictionary["responseMlePrivateKeyFilePath"] = self.responseMlePrivateKeyFilePath
        if self.responseMlePrivateKeyFilePassword:
            configuration_dictionary["responseMlePrivateKeyFilePassword"] = self.responseMlePrivateKeyFilePassword
        if self.responseMleKID:
            configuration_dictionary["responseMleKID"] = self.responseMleKID
        
        # Log configuration
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
