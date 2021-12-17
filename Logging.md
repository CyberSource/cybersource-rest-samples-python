[![Generic badge](https://img.shields.io/badge/LOGGING-NEW-GREEN.svg)](https://shields.io/)

# Logging in CyberSource REST Client SDK (Python)

Since v0.0.31, a new logging framework has been introduced in the SDK. This new logging framework makes use of Python's native logging, and standardizes the logging so that it can be integrated with the logging in the client application.

## Python's native logging Configuration

In order to leverage the new logging framework, the following configuration settings may be added to the merchant configuration as part of **`LogConfiguration`**:

* enableLog
* log_directory
* log_file_name
* log_format
* log_date_format
* log_max_size
* log_level
* enable_masking

In our [sample Configuration.py](https://github.com/CyberSource/cybersource-rest-samples-python/blob/master/data/Configuration.py) file, the following lines have been added to support this new framework:

```python
    self.enable_log = True
    self.log_file_name = "cybs"
    self.log_maximum_size = 10487560
    self.log_directory = os.path.join(os.getcwd(), "Logs")
    self.log_level = "Debug"
    self.enable_masking = False
    self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    self.log_date_format = "%Y-%m-%d %H:%M:%S"
    ...
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
```

### Important Notes

The variable `enableMasking` needs to be set to `true` if sensitive data in the request/response should be hidden/masked.

Sensitive data fields are listed below:

  * Card Security Code
  * Card Number
  * Any field with `number` in the name
  * Card Expiration Month
  * Card Expiration Year
  * Account
  * Routing Number
  * Email
  * First Name & Last Name
  * Phone Number
  * Type
  * Token
  * Signature
