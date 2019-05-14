from authenticationsdk.core.Authorization import *
import requests
from lib.sampleapiclient.connection.Headers import *
from lib.sampleapiclient.connection.Connection import *
import lib.sampleapiclient.masking.Masking
import authenticationsdk.util.ExceptionAuth
import authenticationsdk.util.Utility


# Here all the data ( header + claimSet + Signature ) are set inside the HTTP connection and the call is
# made to APIserver. On successful transaction, response message and response code : 200 is obtained


class JwtUrlConnection(Headers, Connection):
    def __init__(self):
        self.merchantconfig = None
        self.jwt_method = None
        self.jwt_get_id = None
        self.date_time = None

    def jwt_url_connection(self, mconfig, logger):
        self.merchantconfig = mconfig
        self.jwt_method = mconfig.request_type_method
        self.date_time = mconfig.get_time()
        self.jwt_connection(logger)

    # Establishing connection based on whether the method is Get or Post
    def jwt_connection(self, logger):
        try:
            response_message = ""
            mask_values = ""

            if self.jwt_method.upper() == GlobalLabelParameters.GET:
                response_message = self.get(logger)
            elif self.jwt_method.upper() == GlobalLabelParameters.POST:
                response_message = self.post(logger)
            elif self.jwt_method.upper() == GlobalLabelParameters.PUT:
                response_message = self.put(logger)
            elif self.jwt_method.upper() == GlobalLabelParameters.DELETE:
                response_message = self.delete(logger)
            message = response_message.content.decode("utf-8")
            if self.jwt_method.upper() == GlobalLabelParameters.GET or self.jwt_method.upper() == GlobalLabelParameters.POST or self.jwt_method.upper() == GlobalLabelParameters.PUT:
                mask_values = lib.sampleapiclient.masking.Masking.masking(response_message.content.decode('utf-8'))
                message = mask_values
            if self.merchantconfig.enable_log is True:
                logger.info(GlobalLabelParameters.URL + ":   " + self.merchantconfig.url)
                if not (response_message.headers.get('v-c-correlation-id') is None):
                    logger.info(
                        GlobalLabelParameters.V_C_CORRELATION_ID + ":   " + response_message.headers['v-c-correlation-id'])
                logger.info("Response code:    " + str(response_message.status_code))
                logger.info("Response-Message:   " + message)
                logger.info("Status Information :   " + authenticationsdk.util.Utility.get_response_code_message(
                    response_message.status_code))

            if self.jwt_method.upper() == GlobalLabelParameters.POST or self.jwt_method.upper() == GlobalLabelParameters.PUT:
                if self.merchantconfig.enable_log is True:
                    payload = self.merchantconfig.request_json_path_data
                    masked_payload = lib.sampleapiclient.masking.Masking.masking(payload)
                    logger.info("Request Body:    " + masked_payload)
            if self.merchantconfig.enable_log is True:
                logger.info("END> ======================================= ")
                logger.info("\n")

            # Setting the response values to the Merchant Configuration object
            self.merchantconfig.v_c_correlation_id=""
            self.merchantconfig.response_code = response_message.status_code
            self.merchantconfig.response_message = response_message.text.encode('utf-8')
            if not (response_message.headers.get('v-c-correlation-id') is None):
                self.merchantconfig.v_c_correlation_id = response_message.headers[
                    'v-c-correlation-id']
        except Exception as e:
            authenticationsdk.util.ExceptionAuth.log_exception(logger, repr(e), self.merchantconfig)

    # JWT-Get Connection
    def get(self, logger):

        # Add Request Header :: "Content-Type"
        header = self.set_json_application()
        # Add Request Header :: "authorization-bearer"
        date_time = self.date_time
        authorization_headers_1 = self.set_signature(date_time, logger)
        header.update(authorization_headers_1)
        # Add the Accept-Encoding Header
        additional_header = {'Accept-Encoding': '*'}
        header.update(additional_header)
        # Add proxy headers
        proxies = self.set_proxy_connection()
        # Establishing connection and obtaining response based on request type
        r = self.open_connection(self.merchantconfig, header, proxies)

        return r

    # JWT-Post-Connection
    def post(self, logger):

        # Add Request Header :: "Content-Type"
        header = self.set_json_application()
        # Add Request Header :: "authorization-bearer"
        date_time = self.date_time
        authorization_headers_1 = self.set_signature(date_time, logger)
        header.update(authorization_headers_1)
        # Add proxy headers
        proxies = self.set_proxy_connection()
        # Establishing connection and obtaining response based on request type
        r = self.open_connection(self.merchantconfig, header, proxies)

        return r

    def put(self, logger):

        # Add Request Header :: "Content-Type"
        header = self.set_json_application()
        # Add Request Header :: "authorization-bearer"
        date_time = self.date_time
        authorization_headers_1 = self.set_signature(date_time, logger)
        header.update(authorization_headers_1)
        # Add proxy headers
        proxies = self.set_proxy_connection()
        # Establishing connection and obtaining response based on request type
        r = self.open_connection(self.merchantconfig, header, proxies)

        return r

    def delete(self, logger):

        # Add Request Header :: "Content-Type"
        header = self.set_json_application()
        # Add Request Header :: "authorization-bearer"
        date_time = self.date_time
        authorization_headers_1 = self.set_signature(date_time, logger)
        header.update(authorization_headers_1)
        # Add the Accept-Encoding Header
        additional_header = {'Accept-Encoding': '*'}
        header.update(additional_header)
        # Add proxy headers
        proxies = self.set_proxy_connection()
        # Establishing connection and obtaining response based on request type
        r = self.open_connection(self.merchantconfig, header, proxies)

        return r

    def set_json_application(self):
        headers = {GlobalLabelParameters.CONTENT_TYPE: GlobalLabelParameters.APPLICATION_JSON}
        return headers

    def set_signature(self, date_time, logger):
        # This method calls the Authorization class which inturn decides whether to call HTTP_Signature
        # or JWT Signature based on the request type
        authorization = Authorization()
        temp = authorization.get_token(self.merchantconfig, self.date_time, logger)
        temp_token = "Bearer " + temp.decode("utf-8")
        authorization_headers = {GlobalLabelParameters.AUTHORIZATION_BEARER: str(temp_token)}

        return authorization_headers

    def set_proxy_connection(self):
        if self.merchantconfig.proxy_address is None or self.merchantconfig.proxy_address == "" or self.merchantconfig.proxy_port is None or self.merchantconfig.proxy_port == "":
            return
        else:
            proxies_url = {GlobalLabelParameters.PROXY_PREFIX: str(
                GlobalLabelParameters.HTTP_URL_PREFIX + self.merchantconfig.proxy_address + ":" + self.merchantconfig.proxy_port)}
        return proxies_url

    def open_connection(self, merchantconfig, header, proxies):
        response = ""
        if self.jwt_method.upper() == GlobalLabelParameters.GET:
            response = requests.get(url=merchantconfig.url, headers=header,
                                    timeout=1000, verify=False, proxies=proxies)
        elif self.jwt_method.upper() == GlobalLabelParameters.POST:

            response = requests.post(url=merchantconfig.url, data=self.merchantconfig.request_json_path_data,
                                     headers=header,
                                     timeout=1000, verify=False, proxies=proxies)  # verify=False, proxies=proxies
        elif self.jwt_method.upper() == GlobalLabelParameters.PUT:

            response = requests.put(url=merchantconfig.url, data=self.merchantconfig.request_json_path_data,
                                    headers=header,
                                    timeout=1000, verify=False, proxies=proxies)
        elif self.jwt_method.upper() == GlobalLabelParameters.DELETE:

            response = requests.delete(url=merchantconfig.url, headers=header,
                                       timeout=1000, verify=False, proxies=proxies)  # verify=False, proxies=proxies

        return response

    def set_user_agent(self):
        pass

    def set_digest(self):
        pass

    def set_header_data(self):
        pass
