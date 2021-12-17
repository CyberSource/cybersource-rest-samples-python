# Python Sample Code for the CyberSource SDK

[![Travis CI Status](https://travis-ci.org/CyberSource/cybersource-rest-samples-python.svg?branch=master)](https://travis-ci.org/CyberSource/cybersource-rest-samples-python)

This repository contains working code samples which demonstrate python integration with the CyberSource REST APIs through the [CyberSource Python SDK](https://github.com/CyberSource/cybersource-rest-client-python).

## Using the Sample Code

The samples are all completely independent and self-contained. You can analyze them to get an understanding of how a particular method works, or you can use the snippets as a starting point for your own project.  The samples are organized into categories and common usage examples, similar to the [CyberSource API Reference](http://developer.cybersource.com/api/reference).

You can run each sample directly from the command line.

## Requirements

* Python 3.6 or later
* [CyberSource Account](https://developer.cybersource.com/api/developer-guides/dita-gettingstarted/registration.html)
* [CyberSource API Keys](https://developer.cybersource.com/api/developer-guides/dita-gettingstarted/registration/createCertSharedKey.html)

## Running the Samples From the Command Line

* Clone this repository:

```bash
    git clone https://github.com/CyberSource/cybersource-rest-samples-python.git
```

* Install the CyberSource Python SDK:

```bash
    pip install cybersource-rest-client-python
```

* Install the Sample Codes (required for running Authentication samples only)

```bash
    pip install -e .
```

* Run the individual samples by name. For example:

```bash
    python [DirectoryPath]\[CodeSampleName]
```

e.g.

```bash
    python samples\Payments\Payments\simple-authorizationinternet.py
```

### Setting your own API credentials for an API Request

Configure the following information in data/configuration.py file:

* Http Signature

```python
        self.authentication_type      = "http_signature"
        self.merchantid               = "Your Merchant ID"
        self.merchant_keyid           = "Your key id"
        self.merchant_secretkey       = "Your secret key"
```

* Jwt

```python
        self.authentication_type      = "jwt"
        self.merchantid               = "Your Merchant ID"
        self.key_alias                = "Your key alias"
        self.key_pass                 = "Your key password"
        self.key_file_name            = "Your key filename"
        self.keys_directory           = os.getcwd()+"\\resources\\"
```

* MetaKey Http

```python
        self.authentication_type      = "http_Signature"
        self.merchantid               = "your_child_merchant_id"
        self.merchant_keyid           = "your_metakey_serial_number"
        self.merchant_secretkey       = "your_metakey_shared_secret"
        self.portfolio_id             = "your_portfolio_id"
        self.use_metakey              = true
```

* MetaKey JWT

```python
        self.authentication_type      = "jwt"
        self.merchantid               = "your_child_merchant_id"
        self.key_alias                = "your_child_merchant_id"
        self.key_pass                 = "your_portfolio_id"
        self.key_file_name            = "your_portfolio_id"
        self.keys_directory           = os.getcwd()+"\\resources\\"
        self.use_metakey              = true
```

### Switching between the sandbox environment and the production environment

CyberSource maintains a complete sandbox environment for testing and development purposes. This sandbox environment is an exact duplicate of our production environment with the transaction authorization and settlement process simulated. By default, this SDK is configured to communicate with the sandbox environment. To switch to the production environment, set the appropriate environment constant in data/Configuration.py file.  For example:

```python
   For TESTING use
   self.run_environment = "apitest.cybersource.com"
   # For PRODUCTION use
   # self.run_environment = "api.cybersource.com"
```

## API Reference

The [API Reference Guide](https://developer.cybersource.com/api/reference/api-reference.html) provides examples of what information is needed for a particular request and how that information would be formatted. Using those examples, you can easily determine what methods would be necessary to include that information in a request using this SDK.

### Logging

[![Generic badge](https://img.shields.io/badge/LOGGING-NEW-GREEN.svg)](https://shields.io/)

Since v0.0.31, a new logging framework has been introduced in the SDK. This new logging framework makes use of Python's native logging, and standardizes the logging so that it can be integrated with the logging in the client application.

More information about this new logging framework can be found in this file : [Logging.md](Logging.md)

## Run Environments

The run environments that were supported in CyberSource Python SDK have been deprecated.
Moving forward, the SDKs will only support the direct hostname as the run environment.

For the old run environments previously used, they should be replaced by the following hostnames:

| Old Run Environment                             | New Hostname Value           |
| ----------------------------------------------- | ---------------------------- |
| `cybersource.environment.sandbox`               | `apitest.cybersource.com`    |
| `cybersource.environment.production`            | `api.cybersource.com`        |
| `cybersource.in.environment.sandbox`            | `apitest.cybersource.com`    |
| `cybesource.in.environment.production`          | `api.in.cybersource.com`     |

For example, replace the following code in the Configuration file:

```python
   For TESTING use
     self.run_environment = "cybersource.environment.sandbox"
   # For PRODUCTION use
   # self.run_environment = "cybersource.environment.production"
```

with the following code:

```python
   For TESTING use
     self.run_environment = "apitest.cybersource.com"
   # For PRODUCTION use
   # self.run_environment = "api.cybersource.com"
```
