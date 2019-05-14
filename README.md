# Python Sample Code for the CyberSource SDK
[![Travis CI Status](https://travis-ci.org/CyberSource/cybersource-rest-samples-python.svg?branch=master)](https://travis-ci.org/CyberSource/cybersource-rest-samples-python)

This repository contains working code samples which demonstrate python integration with the CyberSource REST APIs through the [CyberSource Python SDK](https://github.com/CyberSource/cybersource-rest-client-python).


## Using the Sample Code

The samples are all completely independent and self-contained. You can analyze them to get an understanding of how a particular method works, or you can use the snippets as a starting point for your own project.  The samples are organized into categories and common usage examples, similar to the [CyberSource API Reference](http://developer.cybersource.com/api/reference).

You can run each sample directly from the command line.

## Requirements
* Python 3.4 or later
* [CyberSource Account](https://developer.cybersource.com/api/developer-guides/dita-gettingstarted/registration.html)
* [CyberSource API Keys](https://developer.cybersource.com/api/developer-guides/dita-gettingstarted/registration/createCertSharedKey.html)


## Running the Samples From the Command Line
* Clone this repository:
```
    $ git clone https://github.com/CyberSource/cybersource-rest-samples-python.git
```
* Install the CyberSource Python SDK:
```
    $ pip install cybersource-rest-client-python
```  
* Install the Sample Codes (required for running Authentication samples only)
```
	$ pip install -e .
```
* Run the individual samples by name. For example:
```
    $ python [DirectoryPath]\[CodeSampleName]
```
e.g.
```
    $ python samples\payments\coreservices\process_payment.py
```

### Setting your own API credentials for an API Request

Configure the following information in data/configuration.py file:
  
  * Http Signature

```python
        self.authentication_type = "http_signature"
        self.merchantid = "Your Merchant ID"
        self.merchant_keyid = "your key id"
        self.merchant_secretkey = "your secret key"
```
  * Jwt

```python
        self.authentication_type = "jwt"
        self.merchantid = "Your Merchant ID"
        self.key_alias = "your key alias"
        self.key_pass = "your key password"
        self.key_file_name = "your key filename"
        self.keys_directory = os.getcwd()+"\\resources\\"
```

### Switching between the sandbox environment and the production environment
CyberSource maintains a complete sandbox environment for testing and development purposes. This sandbox environment is an exact
duplicate of our production environment with the transaction authorization and settlement process simulated. By default, this SDK is 
configured to communicate with the sandbox environment. To switch to the production environment, set the appropriate environment 
constant in data/Configuration.py file.  For example:

```python
   For TESTING use
    self.run_environment = "CyberSource.Environment.SANDBOX"
   #For PRODUCTION use
   #self.run_environment = "CyberSource.Environment.PRODUCTION"
```

## API Reference

The [API Reference Guide](https://developer.cybersource.com/api/reference/api-reference.html) provides examples of what information is needed for a particular request and how that information would be formatted. Using those examples, you can easily determine what methods would be necessary to include that information in a request
using this SDK.

