from authenticationsdk.core.Authorization import *
from authenticationsdk.core.MerchantConfiguration import *
import authenticationsdk.logger.Log
from authenticationsdk.util.PropertiesUtil import *
import authenticationsdk.util.ExceptionAuth


class DeleteGenerateHeaders:
    def __init__(self):
        # REQUEST TARGET [EDITABLE]
        self.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest"
        # REQUEST-TYPE [NOT-EDITABLE]
        self.request_type = "DELETE"
        self.merchant_config = None
        self.date = None

    def delete_generate_header(self):
        try:
            util_obj = PropertiesUtil()
            util_obj.cybs_path = os.path.join(os.getcwd(), "samples/authentication/Resources", "cybs.json")
            details_dict1 = util_obj.properties_util()
            
            mconfig = MerchantConfiguration()
            mconfig.set_merchantconfig(details_dict1)
            
            mconfig.validate_merchant_details(details_dict1, mconfig)

            self.merchant_config = mconfig
            self.merchant_config.request_host = mconfig.request_host
            self.merchant_config.request_type_method = self.request_type
            mconfig.request_target = self.request_target
            self.date = mconfig.get_time()
            self.delete_method_headers()
        except ApiException as e:
            print(e)
        except KeyError as e:
            print(GlobalLabelParameters.NOT_ENTERED + str(e))
        except IOError as e:
            print(GlobalLabelParameters.FILE_NOT_FOUND + str(e.filename))

    # This method prints values obtained in our code by connecting to AUTH sdk
    def delete_method_headers(self):
        logger = self.merchant_config.log
        try:
            auth = Authorization()
            authentication_type = self.merchant_config.authentication_type
            
            print("Request Type    :" + self.request_type)
            print(GlobalLabelParameters.CONTENT_TYPE + "       :" + GlobalLabelParameters.APPLICATION_JSON)
            
            if authentication_type.upper() == GlobalLabelParameters.HTTP.upper():
                print(" " + GlobalLabelParameters.USER_AGENT + "          : " + GlobalLabelParameters.USER_AGENT_VALUE)
                print(" MerchantID          : " + self.merchant_config.merchant_id)
                print(" Date                : " + self.merchant_config.get_time())

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
    post_generate_obj = DeleteGenerateHeaders()
    post_generate_obj.delete_generate_header()
