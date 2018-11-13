# Python Sample Code for the CyberSource SDK

This repository contains working code samples which demonstrate python integration with the CyberSource REST APIs through the CyberSource Python SDK.

**__NOTE: THIS REPO OF CODE SAMPLES HAS BEEN MADE PUBLIC FOR SDK TESTING AND SHOULD NOT BE USED FOR PRODUCTION - YET.  PLEASE RAISE AN ISSUE ON THIS REPO IF YOU HAVE FURTHER QUESTIONS AND CHECK BACK SOON FOR GENERAL AVAILABILITY__**

The samples are organized into categories and common usage examples.

The samples are organized into categories and common usage examples, just like our [API Reference Guide](https://developer.cybersource.com/api/reference/api-reference.html). Our API Reference Guide is an interactive reference for the CyberSource API. It explains the request and response parameters for each API method and has embedded code windows to allow you to send actual requests right within the API Reference Guide.


## Using the Sample Code

The samples are all completely independent and self-contained. You can analyze them to get an understanding of how a particular method works, or you can use the snippets as a starting point for your own project.

You can also run each sample directly from the command line.

## Requirements
Python 3.6 Onwards

## Running the Samples From the Command Line
* Clone this repository:
```
    $ git clone https://github.com/CyberSource/cybersource-rest-samples-python.git
```
* Install the CyberSource Python SDK:
```
    $ pip install cybersource-rest-client-python
```  
* Run the individual samples by name. For example:
```
    $ python samples\payments\coreservices\[CodeSampleName]
```
e.g.
```
    $ python samples\payments\coreservices\process_payment.py
```

#### To set your API credentials for an API request,Configure the following information in data/configuration.py file:
  
  * Http

```
        self.authentication_type = "http_signature"
        self.merchantid = "Your Merchant ID"
        self.run_environment = "CyberSource.Environment.SANDBOX"
        self.request_json_path = os.getcwd()+"\\resources\\request.json"
        self.key_alias = "your key alias"
        self.key_pass = "your key password"
        self.key_file_name = "your key filename"
        self.keys_directory = os.getcwd()+"\\resources\\"
        self.merchant_keyid = "your key id"
        self.merchant_secretkey = "your secret key"
        self.enable_log = False
        self.timeout = 1000
        self.log_file_name = "cybs"
        self.log_maximum_size = 10487560
        self.log_directory = "../../../../cybersource-rest-samples-python/Logs/"
        self.proxy_address = "proxy.com"
        self.proxy_port = ""
```

### Switching between the sandbox environment and the production environment
CyberSource maintains a complete sandbox environment for testing and development purposes. This sandbox environment is an exact
duplicate of our production environment with the transaction authorization and settlement process simulated. By default, this SDK is 
configured to communicate with the sandbox environment. To switch to the production environment, set the appropriate environment 
constant in data/Configuration.py file.  For example:

```python
// For PRODUCTION use
  self.run_environment = "CyberSource.Environment.PRODUCTION"
```

## API Reference

The [API Reference Guide](https://developer.cybersource.com/api/reference/api-reference.html) provides examples of what information is needed for a particular request and how that information would be formatted. Using those examples, you can easily determine what methods would be necessary to include that information in a request
using this SDK.

