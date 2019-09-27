import json
import hashlib
import base64
import ssl
import urllib3
import re
import hmac
import os
import jwt

from datetime import date, datetime
from time import mktime
from wsgiref.handlers import format_date_time
from six import PY3, integer_types, iteritems, text_type
from OpenSSL import crypto

class StandAloneJWT:
    def get_time(self):
        now = datetime.now()
        stamp = mktime(now.timetuple())

        return format_date_time(stamp)
        
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
        
    def get_digest(self):
        hashobj = hashlib.sha256()
        hashobj.update(self.payload.encode('utf-8'))
        hash_data = hashobj.digest()
        digest = base64.b64encode(hash_data)
        
        return digest
        
    def fetch_certificate_info(self):
        filecache = {}
        filename = 'testrest'
        
        p12 = crypto.load_pkcs12(open(os.path.join(os.getcwd(), "samples/authentication/Resources", filename) + ".p12", 'rb').read(), self.merchant_id)
        
        cert_str = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())
        der_cert_string = base64.b64encode(ssl.PEM_cert_to_DER_cert(cert_str.decode("utf-8")))
        private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey()).decode("utf-8")

        filecache.setdefault(str(filename), []).append(der_cert_string)
        filecache.setdefault(str(filename), []).append(private_key)
            
        return filecache[filename]
        
    def get_token(self, method, time):   
        if method.upper() == 'POST':
            digest = self.get_digest()
            jwt_body = { "digest": digest.decode("utf-8"), "digestAlgorithm": "SHA-256", "iat": time }
        elif method.upper() == 'GET':
            jwt_body = { "iat": time }
        
        # Reading the .p12 file
        cache_memory = self.fetch_certificate_info()
        der_cert_string = cache_memory[0]
        private_key = cache_memory[1]
        
        # Setting the headers - merchant_id and the public key
        headers_jwt = { "v-c-merchant-id": str(self.merchant_id) }
        
        public_key_list = ([])
        public_key_list.append(der_cert_string.decode("utf-8"))
        public_key_headers = { "x5c": public_key_list }
        
        headers_jwt.update(public_key_headers)
        
        # generating the token of jwt
        encoded_jwt = jwt.encode(jwt_body, private_key, algorithm='RS256', headers=headers_jwt)

        return encoded_jwt.decode("utf-8")

    def process_post(self):
        resource = '/pts/v2/payments/'
        method = 'post'
        
        time = self.get_time()

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
        
        token = self.get_token(method, time)
        
        print("\n -- TOKEN --\n" + token);
        
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
        
        if not 200 <= r.status <= 299:
            return -1
        
        return 0
    
    def process_get(self):
        # resource = '/reporting/v3/reports?startTime=2019-05-01T00:00:00.0Z&endTime=2019-05-30T23:59:59.0Z&timeQueryType=executedTime&reportMimeType=application/xml'
        resource = '/ums/v1/users?organizationId=testrest'
        method = 'get'
        
        time = self.get_time()        
        
        header_params = {}
        header_params['Accept'] = 'application/hal+json;charset=utf-8'
        header_params['Content-Type'] = 'application/json;charset=utf-8'

        url = "https://" + self.request_host + resource
        
        print("\n -- RequestURL -- ")
        print("\tURL : " + url)
        print("\n -- HTTP Headers -- ")
        print("\tContent-Type : " + header_params['Content-Type'])
        print("\tv-c-merchant-id : " + self.merchant_id)
        print("\tHost : " + self.request_host)
        
        token = self.get_token(method, time)
        
        print("\n -- TOKEN --\n" + token);
        
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
        
        if not 200 <= r.status <= 299:
            return -1
        
        return 0        

    def process_standalone_jwt(self):
        # HTTP POST REQUEST
        print("\n\nSample 1: POST call - CyberSource Payments API - HTTP POST Payment request")
        status_code = self.process_post()
        
        if status_code == 0:
            print("STATUS : SUCCESS (HTTP Status = " + str(status_code) + ")")
        else:
            print("STATUS : ERROR (HTTP Status = " + str(status_code) + ")")
            
        # HTTP GET REQUEST
        print("\n\nSample 2: GET call - CyberSource Reporting API - HTTP GET Reporting request")
        status_code = self.process_get()
        
        if status_code == 0:
            print("STATUS : SUCCESS (HTTP Status = " + str(status_code) + ")")
        else:
            print("STATUS : ERROR (HTTP Status = " + str(status_code) + ")")

if __name__ == "__main__":
    standalone_jwt_obj = StandAloneJWT()
    standalone_jwt_obj.process_standalone_jwt()
