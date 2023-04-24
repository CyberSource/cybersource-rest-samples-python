from lib.sampleapiclient.controller.ApiController import *
from Post_Generate_Headers import *
from authenticationsdk.util.PropertiesUtil import *
from authenticationsdk.core.ExceptionHandling import *
from munch import DefaultMunch
from pathlib import Path

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
            details_dict1 = DefaultMunch.fromDict(details_dict1)

            mconfig = MerchantConfiguration()
            mconfig.set_merchantconfig(details_dict1)
            mconfig.validate_merchant_details(details_dict1, mconfig)

            mconfig.request_type_method = self.request_type
            mconfig.request_target = self.request_target
            mconfig.url = self.url + mconfig.request_host + mconfig.request_target

            response_code = self.process(mconfig)
            write_log_audit(response_code)
        except ApiException as e:
            print(e)
            write_log_audit(400)
        except KeyError as e:
            print(GlobalLabelParameters.NOT_ENTERED + str(e))
            write_log_audit(400)
        except IOError as e:
            print(GlobalLabelParameters.FILE_NOT_FOUND + str(e.filename))
            write_log_audit(400)
        except Exception as e:
            print(e)
            write_log_audit(400)

    # noinspection PyMethodMayBeStatic
    def process(self, mconfig):
        api_controller = ApiController()

        api_controller.payment_delete(mconfig)

        print(" URL                : " + mconfig.url)
        print(" Response Code      : " + str(mconfig.response_code))
        print(" Response Message   : " + mconfig.response_message.decode("utf-8"))
        print(" V-C-Correlation ID : " + mconfig.v_c_correlation_id)

        if mconfig.response_code == 200 or mconfig.response_code == 404:
            return 200
        return mconfig.response_code

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    sample_obj = DeleteMethod()
    sample_obj.delete_method()
