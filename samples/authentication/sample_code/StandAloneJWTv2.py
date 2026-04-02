import hashlib
import base64
import ssl
import urllib3
import os
import jwt
import warnings
import time
import uuid

from datetime import date, datetime
from time import mktime
from wsgiref.handlers import format_date_time
from six import PY3, integer_types, iteritems, text_type
from OpenSSL import crypto
from pathlib import Path
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import pkcs12

class StandAloneJWT:

    def write_log_audit(self, status):
        print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

    def __init__(self):
        self.request_host = "apitest.cybersource.com"
        self.merchant_id = "testrest"
        self.merchant_key_id = "08c94330-f618-42a3-b09d-e1e43be5efda"
        self.merchant_secret_key = "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE="

        # REQUEST PAYLOAD
        self.payload = ("{\n" +
                "  \"clientReferenceInformation\": {\n" +
                "    \"code\": \"TC50171_3\"\n" +
                "  },\n" +
                "  \"processingInformation\": {\n" +
                "    \"commerceIndicator\": \"internet\"\n" +
                "  },\n" +
                "  \"orderInformation\": {\n" +
                "    \"billTo\": {\n" +
                "      \"firstName\": \"john\",\n" +
                "      \"lastName\": \"doe\",\n" +
                "      \"address1\": \"201 S. Division St.\",\n" +
                "      \"postalCode\": \"48104-2201\",\n" +
                "      \"locality\": \"Ann Arbor\",\n" +
                "      \"administrativeArea\": \"MI\",\n" +
                "      \"country\": \"US\",\n" +
                "      \"phoneNumber\": \"999999999\",\n" +
                "      \"email\": \"test@cybs.com\"\n" +
                "    },\n" +
                "    \"amountDetails\": {\n" +
                "      \"totalAmount\": \"10\",\n" +
                "      \"currency\": \"USD\"\n" +
                "    }\n" +
                "  },\n" +
                "  \"paymentInformation\": {\n" +
                "    \"card\": {\n" +
                "      \"expirationYear\": \"2031\",\n" +
                "      \"number\": \"5555555555554444\",\n" +
                "      \"securityCode\": \"123\",\n" +
                "      \"expirationMonth\": \"12\",\n" +
                "      \"type\": \"002\"\n" +
                "    }\n" +
                "  }\n" +
                "}")

        self.pool_manager = urllib3.PoolManager(
                num_pools=4,
                maxsize=4,
                cert_reqs=ssl.CERT_REQUIRED,
                ca_certs=None,
                cert_file=None,
                key_file=None
            )

        self.PRIMITIVE_TYPES = (float, bool, bytes, text_type) + integer_types
        self.NATIVE_TYPES_MAPPING = {
            'int': int,
            'long': int if PY3 else long,
            'float': float,
            'str': str,
            'bool': bool,
            'date': date,
            'datetime': datetime,
            'object': object,
        }

    def sanitize_for_serialization(self, obj):
        """
        Builds a JSON POST object.
        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is swagger model, return the properties dict.
        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `swagger_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in iteritems(obj.swagger_types)
                        if getattr(obj, attr) is not None}

        return {key: self.sanitize_for_serialization(val)
                for key, val in iteritems(obj_dict)}

    def parameters_to_tuples(self, params, collection_formats):
        """
        Get parameters as list of tuples, formatting collections.
        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in iteritems(params) if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def get_digest(self, payload):
        hashobj = hashlib.sha256()
        hashobj.update(payload.encode('utf-8'))
        hash_data = hashobj.digest()
        digest = base64.b64encode(hash_data)

        return digest

    def extract_serial_number_from_certificate(self, certificate):
        """
        Extract serial number from X.509 certificate subject field.
        :param certificate: OpenSSL X.509 certificate object
        :return: Serial number as string
        """
        try:
            # Get certificate subject components
            subject = certificate.get_subject()
            
            # Look for serialNumber in subject components using get_components()
            components = subject.get_components()
            for component in components:
                if component[0].decode('utf-8') == 'serialNumber':
                    return component[1].decode('utf-8')
            
            # If serialNumber not found in subject, raise exception
            raise ValueError("Serial number not found in certificate subject field")
            
        except Exception as e:
            raise ValueError(f"Error extracting serial number from certificate: {str(e)}")

    def extract_resource_path(self, resource_path):
        """
        Extract resource path without query parameters.
        :param resource_path: Full resource path with potential query parameters
        :return: Resource path without query parameters
        """
        if not resource_path:
            return ""
        
        # Split the string to remove the query params
        parts = resource_path.split('?', 1)
        return parts[0]

    def get_jwtv2_payload_claims(self, method, resource_path, payload_data=None):
        """
        Generate JWTv2 payload with all required claims.
        :param method: HTTP method (GET, POST, etc.)
        :param resource_path: API resource path
        :param payload_data: Request payload for POST/PUT/PATCH requests
        :return: JWT payload dictionary
        """
        jwt_payload = {}
        
        # Setting the JWT digest and digest Algorithm when a POST, PUT, or PATCH request is made
        if method.upper() in ['POST', 'PUT', 'PATCH']:
            digest = self.get_digest(self.payload)
            jwt_payload["digest"] = digest.decode("utf-8")
            jwt_payload["digestAlgorithm"] = "SHA-256"
        
        # Set the iat and exp claims using epoch timestamps
        current_time = int(time.time())
        jwt_payload["iat"] = current_time
        jwt_payload["exp"] = current_time + 120  # The token is set to expire 2 minutes after creation
        
        # Set the request method, host and resource path in the JWT body
        jwt_payload["request-method"] = method.upper()
        jwt_payload["request-host"] = self.request_host
        jwt_payload["request-resource-path"] = self.extract_resource_path(resource_path)
        
        # Set issuer claim - Using merchant ID for non-metaKey implementation. (Use portfolio ID if metaKey is being used).
        jwt_payload["iss"] = self.merchant_id
        
        # Generate unique JWT ID
        jwt_payload["jti"] = str(uuid.uuid4())
        
        # Set JWT version and merchant ID
        jwt_payload["v-c-jwt-version"] = "2"
        jwt_payload["v-c-merchant-id"] = self.merchant_id
        
        return jwt_payload

    def fetch_certificate_info(self):
        filecache = {}
        filename = 'testrest' #This is the filename of the PKCS12 file without the .p12 extension. For example, if the file is named "testrest.p12", then the filename variable should be set to "testrest".
        filepath = "samples/authentication/Resources" # This is the relative path to the directory containing the PKCS12 file from the current working directory. For example, if the PKCS12 file is located in "samples/authentication/Resources/testrest.p12", then the filepath variable should be set to "samples/authentication/Resources".
        
        # Load PKCS12 file
        with open(os.path.join(os.getcwd(), filepath, filename) + ".p12", 'rb') as f:
            p12_data = f.read()
        
        # Parse PKCS12 using cryptography library
        private_key_crypto, certificate_crypto, additional_certificates = pkcs12.load_key_and_certificates(
            p12_data, self.merchant_id.encode('utf-8')
        )
        
        # Convert to OpenSSL format for compatibility
        cert_pem = certificate_crypto.public_bytes(serialization.Encoding.PEM)
        private_key_pem = private_key_crypto.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        # Create OpenSSL certificate object for serial number extraction
        x509_certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem)
        private_key_str = private_key_pem.decode("utf-8")

        filecache.setdefault(str(filename), []).append(private_key_str)
        filecache.setdefault(str(filename), []).append(x509_certificate)  # Add X.509 certificate object

        return filecache[filename]

    def get_token(self, method, resource_path):
        """
        Generate JWTv2 compliant token.
        :param method: HTTP method (GET, POST, etc.)
        :param resource_path: API resource path
        :return: JWT token string
        """
        try:
            # Generate JWTv2 payload with all required claims
            jwt_payload = self.get_jwtv2_payload_claims(method, resource_path)
            
            # Get certificate information including X.509 certificate object
            cache_memory = self.fetch_certificate_info()
            private_key = cache_memory[0]
            x509_certificate = cache_memory[1]  # X.509 certificate object
            
            # Extract serial number for kid header
            serial_number = self.extract_serial_number_from_certificate(x509_certificate)
            
            # Generate JWT with kid in header (JWTv2 specification)
            # PyJWT supports the typ and alg header claims by default if algorithm is specified.
            # To add new header claims that are not registred in PyJWT, add the key value pair to the header_claims dictionary below.
            # adding `kid` as per JWTv2 specification.
            header_claims = {"kid": str(serial_number)}
            
            # Generate the JWT token
            encoded_jwt = jwt.encode(jwt_payload, private_key, algorithm='RS256', headers=header_claims)
            
            return encoded_jwt
            
        except Exception as e:
            print(f"Error generating JWTv2 token: {str(e)}")
            raise e

    def process_post(self):
        resource = '/pts/v2/payments/'
        method = 'post'

        header_params = {}
        header_params['Accept'] = 'application/hal+json;charset=utf-8'
        header_params['Content-Type'] = 'application/json;charset=utf-8'

        url = "https://" + self.request_host + resource

        print("\n -- RequestURL -- ")
        print("\tURL : " + url)
        print("\n -- HTTP Headers -- ")
        print("\tContent-Type : " + header_params['Accept'])
        print("\tv-c-merchant-id : " + self.merchant_id)
        print("\tHost : " + self.request_host)

        # Pass resource path to get_token for JWTv2
        token = self.get_token(method, resource)

        print("\n -- TOKEN --\n" + token)

        token = "Bearer " + token

        header_params['Authorization'] = str(token)

        header_params = self.sanitize_for_serialization(header_params)
        header_params = dict(self.parameters_to_tuples(header_params, None))

        # Only required for POST request
        body = self.sanitize_for_serialization(self.payload)

        # HTTP Client POST Call
        timeout = None

        try :
            r = self.pool_manager.request(method, url, body=body, preload_content=False, timeout=timeout, headers=header_params)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            return -1

        print("\n -- Response Message -- " )
        print("\tResponse Code :" + str(r.status))
        print("\tv-c-correlation-id :" + r.getheaders().get('v-c-correlation-id'))
        print("\tResponse Data :\n" + r.data.decode('utf-8') + "\n")

        return r.status

    def process_get(self):
        # Updated to TMS endpoint as per PHP samples PR
        resource = '/tms/v2/customers/AB695DA801DD1BB6E05341588E0A3BDC/shipping-addresses/AB6A54B97C00FCB6E05341588E0A3935'
        method = 'get'

        header_params = {}
        # Updated Accept header as per PHP samples PR
        header_params['Accept'] = 'application/json;charset=utf-8'
        header_params['Content-Type'] = 'application/json;charset=utf-8'

        url = "https://" + self.request_host + resource

        print("\n -- RequestURL -- ")
        print("\tURL : " + url)
        print("\n -- HTTP Headers -- ")
        print("\tContent-Type : " + header_params['Content-Type'])
        print("\tv-c-merchant-id : " + self.merchant_id)
        print("\tHost : " + self.request_host)

        # Pass resource path to get_token for JWTv2
        token = self.get_token(method, resource)

        print("\n -- TOKEN --\n" + token)

        token = "Bearer " + token

        header_params['Authorization'] = str(token)

        header_params = self.sanitize_for_serialization(header_params)
        header_params = dict(self.parameters_to_tuples(header_params, None))

        # HTTP Client GET Call
        timeout = None

        try :
            r = self.pool_manager.request(method, url, preload_content=False, timeout=timeout, headers=header_params)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            return -1

        print("\n -- Response Message -- " )
        print("\tResponse Code :" + str(r.status))
        print("\tv-c-correlation-id :" + r.getheaders().get('v-c-correlation-id'))
        print("\tResponse Data :\n" + r.data.decode('utf-8') + "\n")

        return r.status
    
    def is_success(self, status_code):
        return 200 <= status_code <= 299

    def process_standalone_jwt(self):
        # HTTP POST REQUEST
        print("\n\nSample 1: POST call - CyberSource Payments API - HTTP POST Payment request")
        status_code_post = self.process_post()

        if self.is_success(status_code_post):
            print("STATUS : SUCCESS (HTTP Status = " + str(status_code_post) + ")")
        else:
            print("STATUS : ERROR (HTTP Status = " + str(status_code_post) + ")")

        # HTTP GET REQUEST
        print("\n\nSample 2: GET call - CyberSource Customer Shipping Address API - HTTP GET Customer Shipping Address request")
        status_code_get = self.process_get()

        if self.is_success(status_code_get):
            print("STATUS : SUCCESS (HTTP Status = " + str(status_code_get) + ")")
        else:
            print("STATUS : ERROR (HTTP Status = " + str(status_code_get) + ")")

        if self.is_success(status_code_post) and self.is_success(status_code_get):
            self.write_log_audit(200)
        else:
            self.write_log_audit(400)

if __name__ == "__main__":
    standalone_jwt_obj = StandAloneJWT()
    standalone_jwt_obj.process_standalone_jwt()
