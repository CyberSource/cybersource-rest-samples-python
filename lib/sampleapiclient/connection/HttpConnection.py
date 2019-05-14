import requests
from authenticationsdk.core.Authorization import *
from authenticationsdk.payloaddigest.PayLoadDigest import *
from lib.sampleapiclient.connection.Headers import *
from lib.sampleapiclient.connection.Connection import *
import lib.sampleapiclient.masking.Masking
import authenticationsdk.util.ExceptionAuth
import authenticationsdk.util.Utility


# Here all the data ( header + digest + Signature ) are set inside the HTTP connection
# and the call is made to API server
# and response message and  response code is obtained
class HttpConnection(Headers, Connection):
    def __init__(self):
        self.http_merchant_config = None

        self.request_type = None
        self.http_get_id = None
        self.url = None
        self.merchant_key_id = None
        self.merchant_id = None
        self.merchant_secret_key = None

    def http_connection(self, mconfig, logger):

        try:

            self.http_merchant_config = mconfig
            self.request_type = mconfig.request_type_method
            self.merchant_id = mconfig.merchant_id
            self.merchant_key_id = mconfig.merchant_keyid
            self.merchant_secret_key = mconfig.merchant_secretkey

            self.http_connection_request(logger)
        except Exception as e:
            authenticationsdk.util.ExceptionAuth.log_exception(logger, repr(e), mconfig)

    # Establish the connection with server and receives the response message and code
    def http_connection_request(self, logger):
        try:

            # Add Request Header :: "v-c-merchant-id" set value to Cybersource Merchant ID or v-c-merchant-id
            # which can be found in EBC portal
            header = self.set_header_data()

            # Add Request Header :: "Date" The date and time that the message was originated from.
            # HTTP-date" format as defined by RFC7231
            date_time =  self.http_merchant_config.get_time()

            date_header = {GlobalLabelParameters.DATE: date_time}
            header.update(date_header)
            # Add Request Header :: "Host"
            host_header = {
                GlobalLabelParameters.HOST: self.http_merchant_config.request_host}
            header.update(host_header)
            if self.request_type.upper() == GlobalLabelParameters.POST or self.request_type.upper() == GlobalLabelParameters.PUT:
                digest_header = self.set_digest()
                header.update(digest_header)

            # Add Request Header :: "User-Agent"
            user_agent_header = self.set_user_agent()
            header.update(user_agent_header)
            # Add Request Header :: "Content-Type"
            application_header = self.set_json_application()
            header.update(application_header)
            # Add Request Header :: "Accept-Encoding"
            encoding_header = {'Accept-Encoding': '*'}
            header.update(encoding_header)
            # Proxy headers

            proxies = self.set_proxy_connection()

            # Add Request Header :: "Signature"
            signature_header = self.set_signature(date_time, logger)

            header.update(signature_header)

            # Establishing connection and obtaining response based on request type
            # HTTP-Get-Connection

            r = self.open_connection(self.http_merchant_config, header, proxies)

            # HTTP-Post Connection

            # Setting the response values to the Merchant Configuration object
            self.http_merchant_config.v_c_correlation_id = ""
            self.http_merchant_config.response_code = r.status_code
            self.http_merchant_config.response_message = r.content
            if not (r.headers.get('v-c-correlation-id') is None):
                self.http_merchant_config.v_c_correlation_id = r.headers['v-c-correlation-id']

            # Masking the values
            mask_values = ""
            message = r.content.decode("utf-8")

            if not (self.request_type.upper() == GlobalLabelParameters.DELETE):
                mask_values = lib.sampleapiclient.masking.Masking.masking(r.content.decode('utf-8'))
                message = mask_values

            # Logging the URL,v_c_correlation_id,status code,content
            if self.http_merchant_config.enable_log is True:
                logger.info(GlobalLabelParameters.URL + ":   " + self.http_merchant_config.url)
                if not (r.headers.get('v-c-correlation-id') is None):
                    logger.info(GlobalLabelParameters.V_C_CORRELATION_ID + ":   " + r.headers['v-c-correlation-id'])
                logger.info("Response code:    " + str(r.status_code))

                logger.info("Response-Message:   " + message)
                logger.info("Status Information :   " + authenticationsdk.util.Utility.get_response_code_message(
                    r.status_code))

            if self.request_type.upper() == GlobalLabelParameters.POST or self.request_type.upper() == GlobalLabelParameters.PUT:
                if self.http_merchant_config.enable_log is True:
                    payload = self.http_merchant_config.request_json_path_data

                    masked_payload = lib.sampleapiclient.masking.Masking.masking(payload)

                    logger.info("Request Body:    " + masked_payload)
            if self.http_merchant_config.enable_log is True:
                logger.info("END> ======================================= ")
                logger.info("\n")
        except TypeError as e:
            authenticationsdk.util.ExceptionAuth.log_exception(logger, repr(e), self.http_merchant_config)
        except Exception as e:

            authenticationsdk.util.ExceptionAuth.log_exception(logger, repr(e), self.http_merchant_config)

    def set_header_data(self):

        set_merchant_header = {
            GlobalLabelParameters.MERCHANT_ID: str(self.merchant_id)}
        return set_merchant_header

    def set_digest(self):
        digest_obj = DigestAndPayload()

        encoded_digest = digest_obj.string_digest_generation(
            self.http_merchant_config.request_json_path_data)

        set_digest_header = {GlobalLabelParameters.DIGEST: GlobalLabelParameters.DIGEST_PREFIX + encoded_digest.decode("utf-8")}

        return set_digest_header

    def set_signature(self, date_time, logger):
        # This method calls the Authorization class which inturn decides whether to call HTTP_Signature
        # or JWT Signature based on the request type
        authorization = Authorization()

        signature_header_value = authorization.get_token(self.http_merchant_config,
                                                         date_time, logger)

        set_signature_header = {GlobalLabelParameters.SIGNATURE: str(signature_header_value)}

        return set_signature_header

    def set_user_agent(self):

        set_user_agent_header = {
            GlobalLabelParameters.USER_AGENT: GlobalLabelParameters.USER_AGENT_VALUE}
        return set_user_agent_header

    def set_json_application(self):
        set_json_application_header = {GlobalLabelParameters.CONTENT_TYPE: GlobalLabelParameters.APPLICATION_JSON}
        return set_json_application_header

    def set_proxy_connection(self):
        if self.http_merchant_config.proxy_address is None or self.http_merchant_config.proxy_address == "" or self.http_merchant_config.proxy_port is None or self.http_merchant_config.proxy_port == "":

            return
        else:

            proxies_url = {
                GlobalLabelParameters.PROXY_PREFIX: str(
                    GlobalLabelParameters.HTTP_URL_PREFIX + self.http_merchant_config.proxy_address + ":" + self.http_merchant_config.proxy_port)}
        return proxies_url

    def open_connection(self, merchantconfig, header, proxies):
        response = ""
        if self.request_type.upper() == GlobalLabelParameters.GET:

            response = requests.get(url=merchantconfig.url, headers=header,
                                    timeout=1000, verify=False, proxies=proxies)

        elif self.request_type.upper() == GlobalLabelParameters.POST:

            response = requests.post(url=merchantconfig.url, data=self.http_merchant_config.request_json_path_data,
                                     headers=header,
                                     timeout=1000, verify=False, proxies=proxies)  # verify=False, proxies=proxies
        elif self.request_type.upper() == GlobalLabelParameters.PUT:

            response = requests.put(url=merchantconfig.url, data=self.http_merchant_config.request_json_path_data,
                                    headers=header,
                                    timeout=1000, verify=False, proxies=proxies)  # verify=False, proxies=proxies
        elif self.request_type.upper() == GlobalLabelParameters.DELETE:

            response = requests.delete(url=merchantconfig.url, headers=header,
                                       timeout=1000, verify=False, proxies=proxies)  # verify=False, proxies=proxies

        return response
