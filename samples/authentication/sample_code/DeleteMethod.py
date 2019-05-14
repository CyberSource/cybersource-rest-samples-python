from lib.sampleapiclient.controller.ApiController import *
from Post_Generate_Headers import *
from authenticationsdk.util.PropertiesUtil import *
from authenticationsdk.core.ExceptionHandling import *

class DeleteMethod:
    def __init__(self):
        # REQUEST TARGET [EDITABLE]
        self.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest"
        # REQUEST-TYPE [NOT-EDITABLE]
        self.request_type = "DELETE"
        self.url = GlobalLabelParameters.HTTP_URL_PREFIX

    def delete_method(self):
        try:
            util_obj = PropertiesUtil()
            util_obj.cybs_path = os.path.join(os.getcwd(), "samples/authentication/Resources", "cybs.json")
            details_dict1 = util_obj.properties_util()
            
            mconfig = MerchantConfiguration()
            mconfig.set_merchantconfig(details_dict1)
            
            mconfig.validate_merchant_details(details_dict1, mconfig)
            
            mconfig.request_type_method = self.request_type
            mconfig.request_target = self.request_target
            mconfig.url = self.url + mconfig.request_host + mconfig.request_target
            
            self.process(mconfig)
        except ApiException as e:
            print(e)
        except KeyError as e:
            print(GlobalLabelParameters.NOT_ENTERED + str(e))
        except IOError as e:
            print(GlobalLabelParameters.FILE_NOT_FOUND + str(e.filename))
        except Exception as e:
            print((e))

    # noinspection PyMethodMayBeStatic
    def process(self, mconfig):
        api_controller = ApiController()
		
        api_controller.payment_delete(mconfig)
        
        print(" URL                : " + mconfig.url)
        print(" Response Code      : " + str(mconfig.response_code))
        print(" Response Message   : " + mconfig.response_message.decode("utf-8"))
        print(" V-C-Correlation ID : " + mconfig.v_c_correlation_id)

if __name__ == "__main__":
    sample_obj = DeleteMethod()
    sample_obj.delete_method()
