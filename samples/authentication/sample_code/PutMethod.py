from lib.sampleapiclient.controller.ApiController import *
from Post_Generate_Headers import *
from authenticationsdk.util.PropertiesUtil import *
from authenticationsdk.core.ExceptionHandling import *
from pathlib import Path

request_file = os.path.join(os.getcwd(), "samples/authentication/data", "RequestData.py")
request_data = SourceFileLoader("module.name", request_file).load_module()

class PutMethod:
    def __init__(self):
        # REQUEST TARGET [EDITABLE]
        self.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest"
        # REQUEST-TYPE [NOT-EDITABLE]
        self.request_type = "PUT"
        # REQUEST-JSON-PATH [NOT-EDITABLE]
        self.request_json_path = "samples/authentication/Resources/trr_report.json"
        self.url = GlobalLabelParameters.HTTP_URL_PREFIX

    def put_method(self):
        try:
            util_obj = PropertiesUtil()
            util_obj.cybs_path = os.path.join(os.getcwd(), "samples/authentication/Resources", "cybs.json")
            details_dict1 = util_obj.properties_util()

            mconfig = MerchantConfiguration()
            mconfig.set_merchantconfig(details_dict1)

            mconfig.validate_merchant_details(details_dict1, mconfig)

            mconfig.request_json_path_data = request_data.json_file_data(self.request_json_path, mconfig)

            mconfig.request_type_method = self.request_type
            mconfig.request_target = self.request_target
            mconfig.url = self.url + mconfig.request_host + mconfig.request_target

            self.process(mconfig)
            write_log_audit(200)
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
            print((e))
            write_log_audit(400)

    # noinspection PyMethodMayBeStatic
    def process(self, mconfig):
        api_controller = ApiController()

        api_controller.payment_put(mconfig)

        print(" URL                : " + mconfig.url)
        print(" Response Code      : " + str(mconfig.response_code))
        print(" Response Message   : " + mconfig.response_message.decode("utf-8"))
        print(" V-C-Correlation ID : " + mconfig.v_c_correlation_id)

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    sample_obj = PutMethod()
    sample_obj.put_method()
