from authenticationsdk.core.Authorization import *
from authenticationsdk.payloaddigest.PayLoadDigest import *
from authenticationsdk.core.MerchantConfiguration import *
import authenticationsdk.logger.Log
from authenticationsdk.util.PropertiesUtil import *
import authenticationsdk.util.ExceptionAuth
from importlib.machinery import SourceFileLoader

request_file = os.path.join(os.getcwd(), "samples/authentication/data", "RequestData.py")
request_data = SourceFileLoader("module.name", request_file).load_module()

class PostGenerateHeaders:
    def __init__(self):
        # REQUEST TARGET [EDITABLE]
        self.request_target = "/pts/v2/payments"
        # REQUEST-TYPE [NOT-EDITABLE]
        self.request_type = "POST"
        # REQUEST-JSON-PATH [NOT-EDITABLE]
        self.request_json_path = "samples/authentication/Resources/request.json"
        self.merchant_config = None
        self.date = None

    def post_generate_header(self):
        try:
            util_obj = PropertiesUtil()
            util_obj.cybs_path = os.path.join(os.getcwd(), "samples/authentication/Resources", "cybs.json")
            details_dict1 = util_obj.properties_util()
            
            mconfig = MerchantConfiguration()
            mconfig.set_merchantconfig(details_dict1)
            
            mconfig.validate_merchant_details(details_dict1, mconfig)
			
            mconfig.request_json_path_data = request_data.json_file_data(self.request_json_path, mconfig)
				
            self.merchant_config = mconfig
            self.merchant_config.request_host = mconfig.request_host
            self.merchant_config.request_type_method = self.request_type
            mconfig.request_target = self.request_target
            self.date = mconfig.get_time()
            self.post_method_headers()
        except ApiException as e:
            print(e)
        except KeyError as e:
            print(GlobalLabelParameters.NOT_ENTERED + str(e))
        except IOError as e:
            print(GlobalLabelParameters.FILE_NOT_FOUND + str(e.filename))
        except Exception as e:
            print(repr(e))

    # This method prints values obtained in our code by connecting to AUTH sdk
    def post_method_headers(self):
        logger = self.merchant_config.log
        try:
            auth = Authorization()
            digest = DigestAndPayload()
            authentication_type = self.merchant_config.authentication_type
            
            print("Request Type    :" + self.request_type)
            print(GlobalLabelParameters.CONTENT_TYPE + "       :" + GlobalLabelParameters.APPLICATION_JSON)
            
            if authentication_type.upper() == GlobalLabelParameters.HTTP.upper():
                print(" " + GlobalLabelParameters.USER_AGENT + "          : " + GlobalLabelParameters.USER_AGENT_VALUE)
                print(" MerchantID          : " + self.merchant_config.merchant_id)
                print(" Date                : " + self.merchant_config.get_time())
                print("digest               :" + GlobalLabelParameters.DIGEST_PREFIX + digest.string_digest_generation(
                    self.merchant_config.request_json_path_data).decode("utf-8"))
                
                temp_sig = auth.get_token(self.merchant_config, self.date, logger)
                print("Signature Header      :" + str(temp_sig))
                print("Host                  :" + self.merchant_config.request_host)
            else:
                temp_sig = auth.get_token(self.merchant_config, self.date, logger)
                print("Authorization Bearer            :" + str(temp_sig.decode("utf-8")))
            if self.merchant_config.enable_log is True:
                logger.info("END> ======================================= ")
                logger.info("\n")
        except ApiException as e:
            authenticationsdk.util.ExceptionAuth.log_exception(logger, e, self.merchant_config)
        except Exception as e:
            authenticationsdk.util.ExceptionAuth.log_exception(logger, repr(e), self.merchant_config)


if __name__ == "__main__":
    post_generate_obj = PostGenerateHeaders()
    post_generate_obj.post_generate_header()
