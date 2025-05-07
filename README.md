# Python Sample Code for the CyberSource SDK

[![Build Status](https://app.travis-ci.com/CyberSource/cybersource-rest-samples-python.svg?branch=master)](https://app.travis-ci.com/CyberSource/cybersource-rest-samples-python)

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

* Set the environment variable `PYTHONPATH` to the base directory of the Sample Codes.

    On Linux, run the following:

    ```bash
    export PYTHONPATH=$(pwd):$PYTHONPATH
    ```

    On Windows, run the following:

    ```bash
    set PYTHONPATH=%cd%
    ```

* Install the Sample Codes and its dependencies (required for running Authentication samples only)

    ```bash
    pip install -e .
    pip install requests munch
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
    # For TESTING use
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
    # For TESTING use
    self.run_environment = "cybersource.environment.sandbox"
    # For PRODUCTION use
    # self.run_environment = "cybersource.environment.production"
```

with the following code:

```python
    # For TESTING use
    self.run_environment = "apitest.cybersource.com"
    # For PRODUCTION use
    # self.run_environment = "api.cybersource.com"
```

## Disclaimer

Cybersource may allow Customer to access, use, and/or test a Cybersource product or service that may still be in development or has not been market-tested (“Beta Product”) solely for the purpose of evaluating the functionality or marketability of the Beta Product (a “Beta Evaluation”). Notwithstanding any language to the contrary, the following terms shall apply with respect to Customer’s participation in any Beta Evaluation (and the Beta Product(s)) accessed thereunder): The Parties will enter into a separate form agreement detailing the scope of the Beta Evaluation, requirements, pricing, the length of the beta evaluation period (“Beta Product Form”). Beta Products are not, and may not become, Transaction Services and have not yet been publicly released and are offered for the sole purpose of internal testing and non-commercial evaluation. Customer’s use of the Beta Product shall be solely for the purpose of conducting the Beta Evaluation. Customer accepts all risks arising out of the access and use of the Beta Products. Cybersource may, in its sole discretion, at any time, terminate or discontinue the Beta Evaluation. Customer acknowledges and agrees that any Beta Product may still be in development and that Beta Product is provided “AS IS” and may not perform at the level of a commercially available service, may not operate as expected and may be modified prior to release. CYBERSOURCE SHALL NOT BE RESPONSIBLE OR LIABLE UNDER ANY CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE RELATING TO A BETA PRODUCT OR THE BETA EVALUATION (A) FOR LOSS OR INACCURACY OF DATA OR COST OF PROCUREMENT OF SUBSTITUTE GOODS, SERVICES OR TECHNOLOGY, (B) ANY CLAIM, LOSSES, DAMAGES, OR CAUSE OF ACTION ARISING IN CONNECTION WITH THE BETA PRODUCT; OR (C) FOR ANY INDIRECT, INCIDENTAL OR CONSEQUENTIAL DAMAGES INCLUDING, BUT NOT LIMITED TO, LOSS OF REVENUES AND LOSS OF PROFITS.
