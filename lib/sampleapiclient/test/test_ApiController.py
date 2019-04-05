import unittest
from lib.sampleapiclient.controller.ApiController import *
from authenticationsdk.core.MerchantConfiguration import *
import authenticationsdk.util.PropertiesUtil
import authenticationsdk.logger.Log
import cybersource_authentication_sdk_python.data.RequestData
import logging
from authenticationsdk.core.MockData import *


class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.func = ApiController()

        self.url = GlobalLabelParameters.HTTP_URL_PREFIX

        self.merchant_config = MerchantConfiguration()
        self.date = self.merchant_config.get_time()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    # This Method checks Http get UnitTesting
    def test_for_get_http(self):
        self.merchant_config.request_type_method = "GET"
        self.merchant_config.authentication_type = "http_signature"
        self.merchant_config.set_merchantconfig(MockData.HTTP_VALUES)
        self.get_id = "5246387105766473203529"
        self.logger = authenticationsdk.logger.Log.setup_logger(self.merchant_config)
        self.merchant_config.log = self.logger
        self.merchant_config.request_target = "/pts/v2/payments/" + self.get_id
        self.merchant_config.url = self.url + self.merchant_config.request_host + self.merchant_config.request_target

        self.assertIsNone(self.func.payment_get(self.merchant_config))
        self.assertEqual(self.merchant_config.response_code, 200)

    # This Method checks Http post UnitTesting
    def test_for_post_http(self):
        self.merchant_config.request_type_method = "POST"
        self.merchant_config.authentication_type = "http_signature"
        self.merchant_config.set_merchantconfig(MockData.HTTP_VALUES)
        self.logger = authenticationsdk.logger.Log.setup_logger(self.merchant_config)
        self.merchant_config.log = self.logger
        self.request_json_path = "../../cybersource_authentication_sdk_python/Resources/request.json"
        self.merchant_config.request_json_path_data = cybersource_authentication_sdk_python.data.RequestData.sample_payment_data()

        self.merchant_config.request_target = "/pts/v2/payments"
        self.merchant_config.url = self.url + self.merchant_config.request_host + self.merchant_config.request_target

        self.assertIsNone(
            self.func.payment_post(self.merchant_config))
        self.assertEqual(self.merchant_config.response_code, 201)

    # This Method checks Http put UnitTesting
    def test_for_put_http(self):
        self.merchant_config.request_type_method = "PUT"
        self.merchant_config.authentication_type = "http_signature"
        self.merchant_config.set_merchantconfig(MockData.HTTP_VALUES)
        self.logger = authenticationsdk.logger.Log.setup_logger(self.merchant_config)
        self.merchant_config.log = self.logger
        self.request_json_path = "../../cybersource_authentication_sdk_python/Resources/trr_report.json"
        self.merchant_config.request_json_path_data = cybersource_authentication_sdk_python.data.RequestData.json_file_data(
            self.request_json_path, self.merchant_config)

        self.merchant_config.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest"
        self.merchant_config.url = self.url + self.merchant_config.request_host + self.merchant_config.request_target

        self.assertIsNone(
            self.func.payment_put(self.merchant_config))

    # This Method checks Http Delete UnitTesting
    def test_for_delete_http(self):
        self.merchant_config.request_type_method = "DELETE"
        self.merchant_config.authentication_type = "http_signature"
        self.merchant_config.set_merchantconfig(MockData.HTTP_VALUES)
        self.logger = authenticationsdk.logger.Log.setup_logger(self.merchant_config)
        self.merchant_config.log = self.logger

        self.merchant_config.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest/5246387105766473203529"
        self.merchant_config.url = self.url + self.merchant_config.request_host + self.merchant_config.request_target

        self.assertIsNone(self.func.payment_delete(self.merchant_config))

    # This Method checks Jwt get UnitTesting
    def test_for_get_jwt(self):
        self.merchant_config.set_merchantconfig(MockData.JWT_VALUES)
        self.merchant_config.request_type_method = "GET"
        self.merchant_config.authentication_type = "jwt"
        self.get_id = "5246387105766473203529"
        self.logger = authenticationsdk.logger.Log.setup_logger(self.merchant_config)
        self.merchant_config.log = self.logger

        self.merchant_config.request_target = "/pts/v2/payments/" + self.get_id
        self.merchant_config.url = self.url + self.merchant_config.request_host + self.merchant_config.request_target

        self.assertIsNone(self.func.payment_get(self.merchant_config))
        self.assertEqual(self.merchant_config.response_code, 200)

    # This Method checks Jwt Post UnitTesting
    def test_for_post_jwt(self):
        self.merchant_config.set_merchantconfig(MockData.JWT_VALUES)
        self.merchant_config.request_type_method = "POST"
        self.merchant_config.authentication_type = "jwt"

        self.logger = authenticationsdk.logger.Log.setup_logger(self.merchant_config)
        self.merchant_config.log = self.logger
        self.request_json_path = "../../cybersource_authentication_sdk_python/Resources/request.json"
        self.merchant_config.request_json_path_data = cybersource_authentication_sdk_python.data.RequestData.sample_payment_data()

        self.merchant_config.request_target = "/pts/v2/payments"
        self.merchant_config.url = self.url + self.merchant_config.request_host + self.merchant_config.request_target

        self.assertIsNone(
            self.func.payment_post(self.merchant_config))
        self.assertEqual(self.merchant_config.response_code, 201)

    # This Method checks Jwt Put UnitTesting
    def test_for_put_jwt(self):
        self.merchant_config.set_merchantconfig(MockData.JWT_VALUES)
        self.merchant_config.request_type_method = "PUT"
        self.merchant_config.authentication_type = "jwt"

        self.logger = authenticationsdk.logger.Log.setup_logger(self.merchant_config)
        self.merchant_config.log = self.logger
        self.request_json_path = "../../cybersource_authentication_sdk_python/Resources/trr_report.json"
        self.merchant_config.request_json_path_data = cybersource_authentication_sdk_python.data.RequestData.json_file_data(
            self.request_json_path, self.merchant_config)

        self.merchant_config.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest"
        self.merchant_config.url = self.url + self.merchant_config.request_host + self.merchant_config.request_target

        self.assertIsNone(
            self.func.payment_put(self.merchant_config))

    # This Method checks Jwt Delete UnitTesting
    def test_for_delete_jwt(self):
        self.merchant_config.set_merchantconfig(MockData.JWT_VALUES)
        self.merchant_config.request_type_method = "DELETE"
        self.merchant_config.authentication_type = "jwt"

        self.logger = authenticationsdk.logger.Log.setup_logger(self.merchant_config)
        self.merchant_config.log = self.logger

        self.merchant_config.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest/5246387105766473203529"
        self.merchant_config.url = self.url + self.merchant_config.request_host + self.merchant_config.request_target

        self.assertIsNone(self.func.payment_delete(self.merchant_config))


if __name__ == '__main__':
    unittest.main()
