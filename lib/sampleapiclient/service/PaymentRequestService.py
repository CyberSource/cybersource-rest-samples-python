from lib.sampleapiclient.connection.HttpConnection import *
from lib.sampleapiclient.connection.JwtUrlConnection import *
from authenticationsdk.core.ExceptionHandling import *


# Here the call is made to respective connection class (HTTPConnection or JWTConnection)
# depending on the Authentication type

class PaymentRequestService:
    def __init__(self):
        self.get_merchant_config = None

    # merchantConfig : This object contains all the details present in the cybs.properties.
    # requestType    : Method which is under process or execution (Get or Post).
    # getID          : The Get unique ID.

    def payment_request_service(self, mconfig,logger):

        self.process_payment_request(mconfig, logger)

    # merchantConfig : This object contains all the details present in the cybs.properties.
    # requestType    : Method which is under process or execution (Get or Post).
    # getID          : The Get unique ID.

    # noinspection PyMethodMayBeStatic
    def process_payment_request(self, mconfig, logger):

        authentication_type = mconfig.authentication_type
        # This method establishes Connection based on the Authorization Type
        if authentication_type.upper() == GlobalLabelParameters.HTTP.upper():
            httpconnection = HttpConnection()
            httpconnection.http_connection(mconfig, logger)
        elif authentication_type.upper() == GlobalLabelParameters.JWT.upper():
            jwt_url_obj = JwtUrlConnection()
            jwt_url_obj.jwt_url_connection(mconfig, logger)
        else:
            raise ApiException(1, GlobalLabelParameters.AUTH_ERROR)
