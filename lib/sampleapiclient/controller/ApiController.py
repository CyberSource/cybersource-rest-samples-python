from lib.sampleapiclient.service.PaymentRequestService import *
from authenticationsdk.core.Authorization import *
import authenticationsdk.util.ExceptionAuth


# ApiContoller has a overloaded payment method which is designed accordingly for JWT and HTTP depending
# on the parameters
# The controller class decides the next step in moving the logic from lib.sample code to servicing the payment request
class ApiController:

    # JWT_HTTP GET_POST
    # merchantConfig : This object contains all the details present in the cybs.properties.
    # requestType    : Method which is under process or execution (Get or Post).
    # getID          : The Get unique ID.

    def __init__(self):
        self.logger = LogFactory.setup_logger(self.__class__.__name__)

    # noinspection PyMethodMayBeStatic
    def payment_get(self, mconfig):
        try:
            authorization = Authorization()
            authorization.validate_request_type_method(mconfig)
            # Calls PaymentRequestService class of service of sampleapiclient
            payment_req_obj = PaymentRequestService()
            payment_req_obj.payment_request_service(mconfig)
        except ApiException as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger, e, mconfig.log_config)
        except Exception as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger, repr(e), mconfig.log_config)

    # noinspection PyMethodMayBeStatic
    def payment_post(self, mconfig):
        try:
            authorization = Authorization()
            authorization.validate_request_type_method(mconfig)
            # Calls PaymentRequestService class of service of sampleapiclient
            payment_req_obj = PaymentRequestService()
            payment_req_obj.payment_request_service(mconfig)
        except ApiException as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger, e, mconfig.log_config)

        except Exception as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger, repr(e), mconfig.log_config)

    # noinspection PyMethodMayBeStatic
    def payment_put(self, mconfig):
        try:
            authorization = Authorization()
            authorization.validate_request_type_method(mconfig)
            # Calls PaymentRequestService class of service of sampleapiclient
            payment_req_obj = PaymentRequestService()
            payment_req_obj.payment_request_service(mconfig)
        except ApiException as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger, e, mconfig.log_config)

        except Exception as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger, repr(e), mconfig.log_config)

    def payment_delete(self, mconfig):
        try:
            authorization = Authorization()
            authorization.validate_request_type_method(mconfig)
            # Calls PaymentRequestService class of service of sampleapiclient
            payment_req_obj = PaymentRequestService()
            payment_req_obj.payment_request_service(mconfig)
        except ApiException as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger, e, mconfig.log_config)

        except Exception as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger, repr(e), mconfig.log_config)
